from locators.admin_dashboard_page_locators import AdminDashboardPageLocators
from pages.base_page import BasePage


class AdminDashboardPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url + "/admin/index.php?route=common/dashboard")

    def is_user_profile_present(self):
        assert self.wait_for_element(AdminDashboardPageLocators.USER_PROFILE) is not None
        self.logger.info("User profile present")

    def is_logout_button_present(self):
        assert self.wait_for_element(AdminDashboardPageLocators.LOGOUT_BUTTON) is not None
        self.logger.info("Log out button present")

    def click_logout(self):
        logout_btn = self.wait_for_element(AdminDashboardPageLocators.LOGOUT_BUTTON)
        logout_btn.click()
        self.logger.info("Log out clicked")

    def click_catalog(self):
        catalog_item = self.wait_for_element(AdminDashboardPageLocators.CATALOG)
        catalog_item.click()
        self.logger.info("Catalog clicked")

    def click_products_in_catalog(self):
        products_item = self.wait_for_element_to_be_visible(AdminDashboardPageLocators.PRODUCTS_IN_CATALOG)
        products_item.click()
        self.logger.info("Product section clicked")

    def is_products_table_present(self):
        assert self.wait_for_element(AdminDashboardPageLocators.PRODUCTS_TABLE) is not None
        self.logger.info("Product table present")
