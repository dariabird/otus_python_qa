from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, driver, url, path_id, product_id):
        super().__init__(driver, f"{url}/index.php?route=product/product&path={path_id}&product_id={product_id}")

    def are_thumbnail_images_present(self):
        assert self.wait_for_elements(ProductPageLocators.THUMBNAILS_IMAGES) is not None

    def is_description_present(self):
        assert self.wait_for_element(ProductPageLocators.DESCRIPTION) is not None

    def is_product_info_present(self):
        assert self.wait_for_element(ProductPageLocators.PRODUCT_INFO) is not None

    def is_add_to_wishlist_button_present(self):
        assert self.wait_for_element(ProductPageLocators.ADD_TO_WISHLIST_BUTTON) is not None

    def is_add_to_cart_button_present(self):
        assert self.wait_for_element(ProductPageLocators.ADD_TO_CART_BUTTON) is not None

