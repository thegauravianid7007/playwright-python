from constants.auth import USERNAME, PASSWORD, INVENTORY_URL, INVALID_USERNAME, INVALID_PASSWORD, LOCKED_USERNAME, \
    LOCKED_USER_PASSWORD
from pages.LoginPage import LoginPage

def test_valid_login(page, read_credentials, get_base_url):
    login_page = LoginPage(page)
    login_page.go_to_page(get_base_url)
    login_page.login_user(read_credentials[USERNAME], read_credentials[PASSWORD])

    assert login_page.get_current_url().endswith(INVENTORY_URL)
    login_page.open_left_menu()
    login_page.logout_user()
    assert not login_page.get_current_url().endswith(INVENTORY_URL)

def test_invalid_login(page, read_credentials, get_base_url):
    login_page = LoginPage(page)
    login_page.go_to_page(get_base_url)
    login_page.login_user(read_credentials[INVALID_USERNAME], read_credentials[INVALID_PASSWORD])

    assert login_page.is_login_error_displayed()

def test_locked_out_user(page, read_credentials, get_base_url):
    login_page = LoginPage(page)
    login_page.go_to_page(get_base_url)
    login_page.login_user(read_credentials[LOCKED_USERNAME], read_credentials[LOCKED_USER_PASSWORD])

    assert login_page.is_user_locked_message_displayed()
