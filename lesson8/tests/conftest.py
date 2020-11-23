import logging
import pytest
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

logging.basicConfig(level=logging.INFO, filename=f"logs/selenium_{time.strftime('%Y-%m-%d-%H-%M-%S')}.log")


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
    parser.addoption(
        "--browser", action="store", default="chrome", help="permitted values: chrome, firefox, opera"
    )
    parser.addoption(
        "--url", action="store", default="https://demo.opencart.com", help="URL for test"
    )


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def driver(request, browser):
    logger = logging.getLogger('BrowserLogger')

    if browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.headless = True
        driver = wd.Firefox(options=firefox_options)
    elif browser == "opera":
        opera_options = OperaOptions()
        opera_options.add_argument("headless")
        driver = wd.Opera(options=opera_options)
    else:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("headless")
        driver = wd.Chrome(options=chrome_options)
    driver.maximize_window()
    logger.info(f"Browser {browser} started.")
    driver = EventFiringWebDriver(driver, MyListener())

    def teardown():
        driver.quit()
        logger.info(f"Browser {browser} closed")
    request.addfinalizer(teardown)
    return driver


@pytest.fixture(autouse=True)
def test_name(request):
    logger = logging.getLogger('Test Logger')
    logger.info(f"===> Test {request.node.name} <===")


@pytest.fixture()
def main_page(driver, url):
    main_page = MainPage(driver, url)
    main_page.open()
    return main_page


@pytest.fixture(params=[20])
def catalog_page(request, driver, url):
    catalog_page = CatalogPage(driver, url, request.param)
    catalog_page.open()
    return catalog_page


@pytest.fixture(params=[{"path_id": 57, "product_id": 49}])
def product_page(request, driver, url):
    product_page = ProductPage(driver, url, **request.param)
    product_page.open()
    return product_page


@pytest.fixture()
def login_page(driver, url):
    login_page = LoginPage(driver, url)
    login_page.open()
    return login_page


@pytest.fixture()
def admin_login_page(driver, url):
    admin_login_page = AdminLoginPage(driver, url)
    admin_login_page.open()
    return admin_login_page
