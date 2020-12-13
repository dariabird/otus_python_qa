import allure


@allure.feature('Product Page')
@allure.story('Presence of elements')
@allure.title('Presence of thumbnail images')
def test_are_thumbnail_images_present(product_page):
    product_page.are_thumbnail_images_present()


@allure.feature('Product Page')
@allure.story('Presence of elements')
@allure.title('Presence of description')
def test_is_description_present(product_page):
    product_page.is_description_present()


@allure.feature('Product Page')
@allure.story('Presence of elements')
@allure.title('Presence of product info')
def test_is_product_info_present(product_page):
    product_page.is_product_info_present()


@allure.feature('Product Page')
@allure.story('Presence of elements')
@allure.title('Presence of adding to wishlist button')
def test_is_add_to_wishlist_button_present(product_page):
    product_page.is_add_to_wishlist_button_present()


@allure.feature('Product Page')
@allure.story('Presence of elements')
@allure.title('Presence of adding to cart button')
def test_is_add_to_cart_button_present(product_page):
    product_page.is_add_to_cart_button_present()


@allure.feature('Product Page')
@allure.story('Gallery for product')
@allure.title('Presence of preview opened from thumbnail')
def test_open_preview_for_thumbnail_image(product_page):
    product_page.click_thumbnail_image()
    product_page.is_preview_opened()


@allure.feature('Product Page')
@allure.story('Adding to cart')
@allure.title('Presence of product name in alert')
def test_item_name_in_alert(product_page):
    product_name = product_page.get_item_name()
    product_page.add_to_cart()
    product_page.is_text_in_alert(product_name)
