from locators.admin_dashboard_page_locators import AdminDashboardPageLocators
from pages.base_page import BasePage


class AdminDashboardPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url + "/admin/index.php?route=common/dashboard")

    def is_user_profile_present(self):
        assert self.wait_for_element(AdminDashboardPageLocators.USER_PROFILE) is not None

    def is_logout_button_present(self):
        assert self.wait_for_element(AdminDashboardPageLocators.LOGOUT_BUTTON) is not None

    def click_logout(self):
        logout_btn = self.wait_for_element(AdminDashboardPageLocators.LOGOUT_BUTTON)
        logout_btn.click()

    def click_catalog(self):
        catalog_item = self.wait_for_element(AdminDashboardPageLocators.CATALOG)
        catalog_item.click()

    def click_products_in_catalog(self):
        products_item = self.wait_for_element_to_be_visible(AdminDashboardPageLocators.PRODUCTS_IN_CATALOG)
        products_item.click()

    def is_products_table_present(self):
        assert self.wait_for_element(AdminDashboardPageLocators.PRODUCTS_TABLE) is not None
