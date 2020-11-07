from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By


class CatalogPageLocators(BasePageLocators):
    SORT_BY_INPUT = By.CSS_SELECTOR, "#input-sort"
    SHOW_INPUT = By.CSS_SELECTOR, "#input-limit"
    LIST_VIEW_BUTTON = By.CSS_SELECTOR, "#list-view"
    GRID_VIEW_BUTTON = By.CSS_SELECTOR, "#grid-view"
    SIDE_MENU = By.CSS_SELECTOR, ".list-group"
