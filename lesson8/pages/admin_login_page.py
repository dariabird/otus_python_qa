from locators.admin_login_page_locators import AdminLoginPageLocators
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url + "/admin")

    def is_username_input_present(self):
        assert self.wait_for_element(AdminLoginPageLocators.USERNAME_INPUT) is not None
        self.logger.info("Username input present")

    def is_password_input_present(self):
        assert self.wait_for_element(AdminLoginPageLocators.PASSWORD_INPUT) is not None
        self.logger.info("Password input present")

    def is_login_button_present(self):
        assert self.wait_for_element(AdminLoginPageLocators.LOGIN_BUTTON) is not None
        self.logger.info("Login button present")

    def is_forgotten_password_link_present(self):
        assert self.wait_for_element(AdminLoginPageLocators.FORGOTTEN_PASSWORD_LINK) is not None
        self.logger.info("Forgotten password link present")

    def is_header_logo_present(self):
        assert self.wait_for_element(AdminLoginPageLocators.HEADER_LOGO) is not None
        self.logger.info("Logo in header present")

    def input_username(self, username="demo"):
        username_input = self.wait_for_element(AdminLoginPageLocators.USERNAME_INPUT)
        username_input.send_keys(username)
        self.logger.info("Inputted username")

    def input_password(self, password="demo"):
        password_input = self.wait_for_element(AdminLoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        self.logger.info("Inputted password")

    def click_login_button(self):
        login_btn = self.wait_for_element(AdminLoginPageLocators.LOGIN_BUTTON)
        login_btn.click()
        self.logger.info("Login button clicked")
