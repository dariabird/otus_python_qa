def test_open_open_cart(main_page):
    """
    тест, который открывает основную страницу opencart и проверяет,
    что мы находимся именно на странице приложения opencart.
    """
    main_page.check_open_cart()


def test_is_slideshow_present(main_page):
    main_page.is_slideshow_present()


def test_is_featured_products_present(main_page):
    main_page.is_featured_products_present()


def test_is_brend_carousel_present(main_page):
    main_page.is_brend_carousel_present()


def test_is_top_menu_present(main_page):
    main_page.is_top_menu_present()


def test_is_search_input_present(main_page):
    main_page.is_search_input_present()
