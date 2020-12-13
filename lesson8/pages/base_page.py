import allure
import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Open page")
    def open(self):
        self.driver.get(self.url)
        self.logger.info(f"Opening {self.url}")

    def get_title(self):
        return self.driver.title

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Checking if element is present")
    def is_element_present(self, locator):
        try:
            self.logger.info(f"Trying to find element {locator}")
            self.driver.find_element(*locator)
        except NoSuchElementException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="no_element_present",
                attachment_type=allure.attachment_type.PNG)
            self.logger.exception(f"Can't find element {locator} but element should be present")
            return False
        self.logger.info(f"Element {locator} found")
        return True

    @allure.step("Checking if element is not present")
    def is_not_element_present(self, locator, timeout=3):
        try:
            self.logger.info(f"Element {locator} should not be found")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="element_present",
                attachment_type=allure.attachment_type.PNG)
            self.logger.exception(f"Find element {locator} but element should not be present")
            return True
        self.logger.info(f"Element {locator} not found as expected")
        return False

    @allure.step("Checking if elements are present")
    def are_elements_present(self, locator):
        try:
            self.logger.info(f"Trying to find elements {locator}")
            self.driver.find_elements(*locator)
        except NoSuchElementException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="no_elements_present",
                attachment_type=allure.attachment_type.PNG)
            self.logger.exception(f"Can't find elements {locator} but elements should be present")
            return False
        self.logger.info(f"Elements {locator} found")
        return True

    @allure.step("Wait for element to be present")
    def wait_for_element(self, locator, timeout=20):
        try:
            self.logger.info(f"Waiting for element {locator}")
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="no_element_present_after_waiting",
                attachment_type=allure.attachment_type.PNG)
            message = f"Cannot find element {locator}"
            self.logger.exception(message)
            raise NoSuchElementException(message)
        self.logger.info(f"Element {locator} found")
        return el

    @allure.step("Wait for elements to be present")
    def wait_for_elements(self, locator, timeout=10):
        try:
            self.logger.info(f"Waiting for elements {locator}")
            els = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="no_elements_present",
                attachment_type=allure.attachment_type.PNG)
            message = f"Cannot find elements {locator}"
            self.logger.exception(message)
            raise NoSuchElementException(message)
        self.logger.info(f"Elements {locator} found")
        return els

    @allure.step("Wait for element to be visible")
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        try:
            self.logger.info(f"Waiting for element {locator} to be visible")
            els = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="element_not_visible_after_waiting",
                attachment_type=allure.attachment_type.PNG)
            message = f"Cannot find elements {locator}"
            self.logger.exception(message)
            raise NoSuchElementException(message)
        self.logger.info(f"Element {locator} visible")
        return els

    def is_top_menu_present(self):
        assert self.wait_for_element(BasePageLocators.TOP_MENU) is not None
        self.logger.info("Top menu present")

    def is_search_input_present(self):
        assert self.wait_for_element(BasePageLocators.SEARCH_INPUT) is not None
        self.logger.info("Search input present")

    def is_search_button_present(self):
        assert self.wait_for_element(BasePageLocators.SEARCH_BUTTON) is not None
        self.logger.info("Search button present")

    def is_cart_button_present(self):
        assert self.wait_for_element(BasePageLocators.CART_BUTTON) is not None
        self.logger.info("Cart button present")

    def is_navigation_bar_present(self):
        assert self.wait_for_element(BasePageLocators.NAVIGATION_BAR) is not None
        self.logger.info("Navigation bar present")

    def is_footer_present(self):
        assert self.wait_for_element(BasePageLocators.FOOTER) is not None
        self.logger.info("Footer present")

    def get_cart_items_number(self):
        cart_items_total = self.wait_for_element(BasePageLocators.CART_TOTAL)
        cart_items = cart_items_total.text.split(" - ")[0]
        self.logger.info(f"Number of items in cart: {cart_items}")
        return cart_items

    def get_cart_total(self):
        cart_items_total = self.wait_for_element(BasePageLocators.CART_TOTAL)
        cart_total = cart_items_total.text.split(" - ")[1]
        self.logger.info(f"Cart total: {cart_total}")
        return cart_total

    @allure.step("Click cart button")
    def click_cart(self):
        self.wait_for_element(BasePageLocators.CART_BUTTON).click()
        self.logger.info("Cart clicked")

    @allure.step("Checking if number of items in cart is equal to {number}")
    def is_items_num_in_cart_equal_to(self, number):
        assert f"{number} item(s)" == self.get_cart_items_number()
        self.logger.info(f"{number} items in cart as expected")

    @allure.step("Checking if total in cart is equal to {cart_sum}")
    def is_cart_total_equal_to(self, cart_sum):
        assert cart_sum == self.get_cart_total()
        self.logger.info(f"Cart total {cart_sum} as expected")

    def is_alert_present(self):
        assert self.wait_for_element(BasePageLocators.ALERT_SUCCESS) is not None
        self.logger.info("Alert present")

    def get_alert_text(self):
        return self.wait_for_element(BasePageLocators.ALERT_SUCCESS).text

    @allure.step("Checking text in alert contains '{text}'")
    def is_text_in_alert(self, text):
        assert text in self.get_alert_text()
        self.logger.info("Text in alert present")
