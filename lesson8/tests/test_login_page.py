def test_is_new_customer_section_present(login_page):
    login_page.is_new_customer_section_present()


def test_is_returning_customer_section_present(login_page):
    login_page.is_returning_customer_section_present()


def test_is_email_input_present(login_page):
    login_page.is_email_input_present()


def test_is_password_input_present(login_page):
    login_page.is_password_input_present()


def test_is_login_button_present(login_page):
    login_page.is_login_button_present()
