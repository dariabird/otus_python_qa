from pages.base_page import BasePage
from locators.catalog_page_locators import CatalogPageLocators


class CatalogPage(BasePage):
    def __init__(self, driver, url, path_id):
        super().__init__(driver, f"{url}/index.php?route=product/category&path={path_id}")

    def is_sort_by_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.SORT_BY_INPUT) is not None

    def is_show_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.SHOW_INPUT) is not None

    def is_list_view_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.LIST_VIEW_BUTTON) is not None

    def is_grid_view_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.GRID_VIEW_BUTTON) is not None

    def is_side_menu_present(self):
        assert self.wait_for_element(CatalogPageLocators.SIDE_MENU) is not None
