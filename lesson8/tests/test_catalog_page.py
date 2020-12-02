import allure


@allure.feature('Catalog Page')
@allure.story('Presence of elements')
@allure.title('Presence of top menu')
def test_is_top_menu_present(catalog_page):
    catalog_page.is_top_menu_present()


@allure.feature('Catalog Page')
@allure.story('Presence of elements')
@allure.title('Presence of search input')
def test_is_search_input_present(catalog_page):
    catalog_page.is_search_input_present()


@allure.feature('Catalog Page')
@allure.story('Presence of elements')
@allure.title('Presence of sort by input')
def test_is_sort_by_input_present(catalog_page):
    catalog_page.is_sort_by_input_present()


@allure.feature('Catalog Page')
@allure.story('Presence of elements')
@allure.title('Presence of show input')
def test_is_show_input_present(catalog_page):
    catalog_page.is_show_input_present()


@allure.feature('Catalog Page')
@allure.story('Presence of elements')
@allure.title('Presence of list view input')
def test_is_list_view_input_present(catalog_page):
    catalog_page.is_list_view_input_present()


@allure.feature('Catalog Page')
@allure.story('Presence of elements')
@allure.title('Presence of grid view input')
def test_is_grid_view_input_present(catalog_page):
    catalog_page.is_grid_view_input_present()


@allure.feature('Catalog Page')
@allure.story('Presence of elements')
@allure.title('Presence of side menu')
def test_is_side_menu_present(catalog_page):
    catalog_page.is_side_menu_present()


@allure.feature('Catalog Page')
@allure.story('Presence of elements')
@allure.title('Presence of catalog page')
def test_add_to_compare(catalog_page):
    catalog_page.add_item_to_compare()
    catalog_page.is_alert_present()
    catalog_page.is_compare_num_equal_to(1)
