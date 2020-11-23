import re
from selenium.common.exceptions import NoSuchElementException
from locators.catalog_page_locators import CatalogPageLocators
from pages.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, driver, url, path_id):
        super().__init__(driver, f"{url}/index.php?route=product/category&path={path_id}")

    def is_sort_by_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.SORT_BY_INPUT) is not None
        self.logger.info("Sort by input present")

    def is_show_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.SHOW_INPUT) is not None
        self.logger.info("Show input present")

    def is_list_view_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.LIST_VIEW_BUTTON) is not None
        self.logger.info("List view input present")

    def is_grid_view_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.GRID_VIEW_BUTTON) is not None
        self.logger.info("Grid view input present")

    def is_side_menu_present(self):
        assert self.wait_for_element(CatalogPageLocators.SIDE_MENU) is not None
        self.logger.info("Side menu present")

    def get_item_with_num(self, item_num):
        items = self.wait_for_elements(CatalogPageLocators.PRODUCT_THUMB)
        try:
            item = items[item_num]
        except IndexError:
            message = f"No item with number {item_num}"
            self.logger.exception(message)
            raise NoSuchElementException(message)
        return item

    def get_item_price(self, item_num=0):
        item = self.get_item_with_num(item_num)
        price = item.find_element(*CatalogPageLocators.PRICE)
        price_elements = price.split()
        item_price = price_elements[0]
        self.logger.info(f"Item price: {item_price}")
        return item_price

    def add_item_to_cart(self, item_num=0):
        item = self.get_item_with_num(item_num)
        add_button = item.find_element(*CatalogPageLocators.ADD_TO_CART_ICON)
        add_button.click()
        self.logger.info("Item added to cart")

    def add_item_to_compare(self, item_num=0):
        item = self.get_item_with_num(item_num)
        compare_button = item.find_element(*CatalogPageLocators.COMPARE_ICON)
        compare_button.click()
        self.logger.info("Item added to compare")

    def add_item_to_fav(self, item_num=0):
        item = self.get_item_with_num(item_num)
        fav_button = item.find_element(*CatalogPageLocators.ADD_TO_FAV_ICON)
        fav_button.click()
        self.logger.info("Item added to favorites")

    def get_product_compare_num(self):
        compare_link_text = self.wait_for_element(CatalogPageLocators.PRODUCT_COMPARE_LINK).text
        res = re.search(r"(\d{1,})", compare_link_text)
        return int(res.group(0))

    def is_compare_num_equal_to(self, num):
        assert self.get_product_compare_num() == num
        self.logger.info(f"Number of items to compare is {num}")
