from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By


class MainPageLocators(BasePageLocators):
    POWERED_BY_OPEN_CART = By.XPATH, "//div[@class='container']/p/a[contains(text(),'OpenCart')]"
    SLIDESHOW = By.CSS_SELECTOR, "#content #slideshow0"
    FEATURED_PRODUCTS = By.CSS_SELECTOR, "#content div.product-layout"
    BRENDS_CAROUSEL = By.CSS_SELECTOR, "div#carousel0"
