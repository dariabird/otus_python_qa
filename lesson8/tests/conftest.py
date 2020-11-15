import pytest
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.admin_login_page import AdminLoginPage


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
    request.addfinalizer(driver.quit)
    return driver


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
