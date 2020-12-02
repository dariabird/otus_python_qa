import allure


@allure.feature('Admin Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of username input')
def test_is_username_input_present(admin_login_page):
    admin_login_page.is_username_input_present()


@allure.feature('Admin Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of password input')
def test_is_password_input_present(admin_login_page):
    admin_login_page.is_password_input_present()


@allure.feature('Admin Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of login button')
def test_is_login_button_present(admin_login_page):
    admin_login_page.is_login_button_present()


@allure.feature('Admin Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of link for password restoring')
def test_is_forgotten_password_link_present(admin_login_page):
    admin_login_page.is_forgotten_password_link_present()


@allure.feature('Admin Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of logo in header')
def test_is_header_logo_present(admin_login_page):
    admin_login_page.is_header_logo_present()
