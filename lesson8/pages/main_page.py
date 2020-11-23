from selenium.common.exceptions import NoSuchElementException
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def check_open_cart(self):
        assert self.wait_for_element(MainPageLocators.POWERED_BY_OPEN_CART) is not None
        self.logger.info("Powered by opencart")

    def is_slideshow_present(self):
        assert self.wait_for_element(MainPageLocators.SLIDESHOW) is not None
        self.logger.info("Slideshow present")

    def is_featured_products_present(self):
        assert self.wait_for_element(MainPageLocators.FEATURED_PRODUCTS) is not None
        self.logger.info("Featured products present")

    def is_brend_carousel_present(self):
        assert self.wait_for_element(MainPageLocators.BRENDS_CAROUSEL) is not None
        self.logger.info("Brend carousel present")

    def get_item_with_num(self, item_num):
        featured_products = self.wait_for_elements(MainPageLocators.FEATURED_PRODUCTS)
        try:
            featured_product = featured_products[item_num]
        except IndexError:
            message = f"No element with number {item_num}"
            self.logger.exception(message)
            raise NoSuchElementException(message)
        return featured_product

    def add_featured_to_fav(self, item_num=0):
        featured_product = self.get_item_with_num(item_num)
        featured_product.find_element(*MainPageLocators.FAV_ICON).click()
        self.logger.info("Product added to favorites")

    def add_featured_to_cart(self, item_num=0):
        featured_product = self.get_item_with_num(item_num)
        featured_product.find_element(*MainPageLocators.ADD_TO_CART_ICON).click()
        self.logger.info("Product added to cart")
