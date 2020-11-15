def test_are_thumbnail_images_present(product_page):
    product_page.are_thumbnail_images_present()


def test_is_description_present(product_page):
    product_page.is_description_present()


def test_is_product_info_present(product_page):
    product_page.is_product_info_present()


def test_is_add_to_wishlist_button_present(product_page):
    product_page.is_add_to_wishlist_button_present()


def test_is_add_to_cart_button_present(product_page):
    product_page.is_add_to_cart_button_present()


def test_open_preview_for_thumbnail_image(product_page):
    product_page.click_thumbnail_image()
    product_page.is_preview_opened()


def test_item_name_in_alert(product_page):
    product_name = product_page.get_item_name()
    product_page.add_to_cart()
    product_page.is_text_in_alert(product_name)
