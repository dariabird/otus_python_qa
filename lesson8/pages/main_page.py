from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def check_open_cart(self):
        assert self.wait_for_element(MainPageLocators.POWERED_BY_OPEN_CART) is not None

    def is_slideshow_present(self):
        assert self.wait_for_element(MainPageLocators.SLIDESHOW) is not None

    def is_featured_products_present(self):
        assert self.wait_for_element(MainPageLocators.FEATURED_PRODUCTS) is not None

    def is_brend_carousel_present(self):
        assert self.wait_for_element(MainPageLocators.BRENDS_CAROUSEL) is not None