import allure

from pages.admin_dashboard_page import AdminDashboardPage
from pages.admin_login_page import AdminLoginPage


@allure.feature('Admin Login')
@allure.story('Logging in')
@allure.title('Log in as admin and quit')
def test_login_and_quit(driver, url):
    admin_login_page = AdminLoginPage(driver, url)
    admin_login_page.open()
    admin_login_page.click_login_button()
    admin_dashboard_page = AdminDashboardPage(driver, url)
    admin_dashboard_page.is_user_profile_present()
    admin_dashboard_page.is_logout_button_present()
    admin_dashboard_page.click_logout()
    admin_login_page.is_login_button_present()


@allure.feature('Admin Settings')
@allure.story('Work with catalogs')
@allure.title('Open catalog and products table')
def test_open_product_list(driver, url):
    admin_login_page = AdminLoginPage(driver, url)
    admin_login_page.open()
    admin_login_page.click_login_button()
    admin_dashboard_page = AdminDashboardPage(driver, url)
    admin_dashboard_page.click_catalog()
    admin_dashboard_page.click_products_in_catalog()
    admin_dashboard_page.is_products_table_present()
