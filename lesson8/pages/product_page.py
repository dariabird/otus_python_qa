import allure

from selenium.common.exceptions import NoSuchElementException
from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver, url, path_id, product_id):
        super().__init__(driver, f"{url}/index.php?route=product/product&path={path_id}&product_id={product_id}")

    def are_thumbnail_images_present(self):
        assert self.wait_for_elements(ProductPageLocators.THUMBNAILS_IMAGES) is not None
        self.logger.info("Thumbnail images present")

    def is_description_present(self):
        assert self.wait_for_element(ProductPageLocators.DESCRIPTION) is not None
        self.logger.info("Product description present")

    def is_product_info_present(self):
        assert self.wait_for_element(ProductPageLocators.PRODUCT_INFO) is not None
        self.logger.info("Product info present")

    def is_add_to_wishlist_button_present(self):
        assert self.wait_for_element(ProductPageLocators.ADD_TO_WISHLIST_BUTTON) is not None
        self.logger.info("Add to wishlist button present")

    def is_add_to_cart_button_present(self):
        assert self.wait_for_element(ProductPageLocators.ADD_TO_CART_BUTTON) is not None
        self.logger.info("Add to cart button present")

    @allure.step("Add to cart")
    def add_to_cart(self):
        self.wait_for_element(ProductPageLocators.ADD_TO_CART_BUTTON).click()
        self.logger.info("Product added to cart")

    def get_price(self):
        return self.wait_for_element(ProductPageLocators.PRICE).text

    def get_item_name(self):
        return self.wait_for_element(ProductPageLocators.ITEM_NAME).text

    def is_preview_opened(self):
        assert self.wait_for_element(ProductPageLocators.PREVIEW_IMAGE) is not None
        self.logger.info("Preview opened")

    @allure.step("Get thumbnail image with index {item_num}")
    def get_thumbnail_image(self, item_num=0):
        thumbnail_images = self.wait_for_elements(ProductPageLocators.THUMBNAILS_IMAGES)
        try:
            thumbnail_image = thumbnail_images[item_num]
        except IndexError:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f"no_thumbnail_with_index_{item_num}",
                attachment_type=allure.attachment_type.PNG)
            message = f"No thumbnail image with number {item_num}"
            self.logger.exception(message)
            raise NoSuchElementException(message)
        return thumbnail_image

    @allure.step("Click thumbnail image with index {item_num}")
    def click_thumbnail_image(self, item_num=0):
        thumbnail_image = self.get_thumbnail_image(item_num)
        thumbnail_image.click()
        self.logger.info("Thumbnail image clicked")
