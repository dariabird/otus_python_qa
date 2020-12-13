import allure


@allure.feature('Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of new customer section')
def test_is_new_customer_section_present(login_page):
    login_page.is_new_customer_section_present()


@allure.feature('Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of returning customer section')
def test_is_returning_customer_section_present(login_page):
    login_page.is_returning_customer_section_present()


@allure.feature('Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of email input')
def test_is_email_input_present(login_page):
    login_page.is_email_input_present()


@allure.feature('Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of password input')
def test_is_password_input_present(login_page):
    login_page.is_password_input_present()


@allure.feature('Login Page')
@allure.story('Presence of elements')
@allure.title('Presence of login button')
def test_is_login_button_present(login_page):
    login_page.is_login_button_present()
