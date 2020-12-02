import allure
import json
import logging
import pytest
import requests
import time

from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from pages.admin_login_page import AdminLoginPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

logging.basicConfig(level=logging.INFO, filename=f"tests/logs/selenium_{time.strftime('%Y-%m-%d-%H-%M-%S')}.log")


class MyListener(AbstractEventListener):
    def after_navigate_to(self, url, driver):
        logging.info(f"We are on {url}")

    def before_quit(self, driver):
        logging.info(f"Getting ready to terminate {driver}")

    def after_quit(self, driver):
        logging.info(f"Quited.")

    def on_exception(self, exception, driver):
        logging.error(f'Got exception: {exception}')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--bversion", action="store", default="87.0")
    parser.addoption("--url", action="store", default="https://demo.opencart.com", help="URL for test")
    parser.addoption("--is_remote", action="store_true", default=False)
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--mobile", action="store_true")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def driver(request):
    logger = logging.getLogger('BrowserLogger')

    browser = request.config.getoption("--browser")
    version = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    executor_url = f"http://{executor}:4444/wd/hub"
    mobile = request.config.getoption("--mobile")
    is_remote = request.config.getoption("--is_remote")

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1280x720",
        "name": "Tester",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs,
        },
        'acceptSslCerts': True,
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {
            'args': []
        }
    }

    mobile_emulation = {"deviceName": "iPhone 5/SE"}

    if is_remote:
        if browser == "chrome" and mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = mobile_emulation

        driver = wd.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
    else:
        if browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.headless = True
            driver = wd.Firefox(options=firefox_options)
        elif browser == "opera":
            opera_options = OperaOptions()
            opera_options.add_argument("headless")
            driver = wd.Opera(options=opera_options)
        elif browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("headless")
            if mobile:
                chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            driver = wd.Chrome(options=chrome_options)
        else:
            raise ValueError(f"{browser} browser not supported")

    if not mobile:
        driver.maximize_window()

    logger.info(f"Browser {browser} started.")
    driver = EventFiringWebDriver(driver, MyListener())

    # Attach browser data
    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.desired_capabilities),
        attachment_type=allure.attachment_type.JSON)

    # Add environment info to allure-report
    with open("allure-report/environment.xml", "w+") as file:
        file.write(f"""<environment>
                    <parameter>
                        <key>Browser</key>
                        <value>{browser}</value>
                    </parameter>
                    <parameter>
                        <key>Browser.Version</key>
                        <value>{version}</value>
                    </parameter>
                    <parameter>
                        <key>Executor</key>
                        <value>{executor}</value>
                    </parameter>
                </environment>
                """)

    def teardown():
        driver.quit()
        logger.info(f"Browser {browser} closed")

    request.addfinalizer(teardown)
    return driver


@pytest.fixture(autouse=True)
def test_name(request):
    logger = logging.getLogger('Test Logger')
    logger.info(f"===> Test {request.node.name} <===")


@allure.step("Open main page")
@pytest.fixture()
def main_page(driver, url):
    main_page = MainPage(driver, url)
    main_page.open()
    return main_page


@allure.step("Open catalog page")
@pytest.fixture(params=[20])
def catalog_page(request, driver, url):
    catalog_page = CatalogPage(driver, url, request.param)
    catalog_page.open()
    return catalog_page


@allure.step("Open page for product with path_id: {path_id} product_id:{product_id}")
@pytest.fixture(params=[{"path_id": 57, "product_id": 49}])
def product_page(request, driver, url):
    product_page = ProductPage(driver, url, **request.param)
    product_page.open()
    return product_page


@allure.step("Open login page")
@pytest.fixture()
def login_page(driver, url):
    login_page = LoginPage(driver, url)
    login_page.open()
    return login_page


@allure.step("Open admin page")
@pytest.fixture()
def admin_login_page(driver, url):
    admin_login_page = AdminLoginPage(driver, url)
    admin_login_page.open()
    return admin_login_page
