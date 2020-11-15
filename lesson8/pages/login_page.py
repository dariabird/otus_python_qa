from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, f"{url}/index.php?route=account/login")

    def is_new_customer_section_present(self):
        assert self.wait_for_elements(LoginPageLocators.NEW_CUSTOMER_SECTION) is not None

    def is_returning_customer_section_present(self):
        assert self.wait_for_elements(LoginPageLocators.RETURNING_CUSTOMER_SECTION) is not None

    def is_email_input_present(self):
        assert self.wait_for_elements(LoginPageLocators.EMAIL_INPUT) is not None

    def is_password_input_present(self):
        assert self.wait_for_elements(LoginPageLocators.PASSWORD_INPUT) is not None

    def is_login_button_present(self):
        assert self.wait_for_elements(LoginPageLocators.LOGIN_BUTTON) is not None
