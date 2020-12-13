import allure

from selenium.common.exceptions import NoSuchElementException
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Checking the link in footer - should be Powered by opencart")
    def check_open_cart(self):
        assert self.wait_for_element(MainPageLocators.POWERED_BY_OPEN_CART) is not None
        self.logger.info("Powered by opencart")

    def is_slideshow_present(self):
        assert self.wait_for_element(MainPageLocators.SLIDESHOW) is not None
        self.logger.info("Slideshow present")

    def is_featured_products_present(self):
        assert self.wait_for_element(MainPageLocators.FEATURED_PRODUCTS) is not None
        self.logger.info("Featured products present")

    def is_brand_carousel_present(self):
        assert self.wait_for_element(MainPageLocators.BRANDS_CAROUSEL) is not None
        self.logger.info("Brand carousel present")

    @allure.step("Get item with number {item_num}")
    def get_item_with_num(self, item_num):
        featured_products = self.wait_for_elements(MainPageLocators.FEATURED_PRODUCTS)
        try:
            featured_product = featured_products[item_num]
        except IndexError:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f"no_element_with_num_{item_num}",
                attachment_type=allure.attachment_type.PNG)
            message = f"No element with number {item_num}"
            self.logger.exception(message)
            raise NoSuchElementException(message)
        return featured_product

    @allure.step("Add featured product to favorites")
    def add_featured_to_fav(self, item_num=0):
        featured_product = self.get_item_with_num(item_num)
        try:
            fav_icon = featured_product.find_element(*MainPageLocators.FAV_ICON)
            fav_icon.click()
        except NoSuchElementException as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="no_element_found",
                attachment_type=allure.attachment_type.PNG)
            self.logger.exception(e.msg)
            raise NoSuchElementException
        self.logger.info("Product added to favorites")

    @allure.step("Add featured product to cart")
    def add_featured_to_cart(self, item_num=0):
        featured_product = self.get_item_with_num(item_num)
        try:
            add_to_cart_btn = featured_product.find_element(*MainPageLocators.ADD_TO_CART_ICON)
            add_to_cart_btn.click()
        except NoSuchElementException as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="no_element_found",
                attachment_type=allure.attachment_type.PNG)
            self.logger.exception(e.msg)
            raise NoSuchElementException
        self.logger.info("Product added to cart")
