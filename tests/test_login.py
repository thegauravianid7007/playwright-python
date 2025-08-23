from pages.LoginPage import LoginPage
import constants

def test_valid_login(page, read_credentials, get_base_url):
    login_page = LoginPage(page)
    login_page.go_to_page(get_base_url)
    login_page.login_user(read_credentials[constants.USERNAME], read_credentials[constants.PASSWORD])

    assert login_page.get_current_url().endswith(constants.INVENTORY_URL)
    login_page.open_left_menu()
    login_page.logout_user()
    assert not login_page.get_current_url().endswith(constants.INVENTORY_URL)

def test_invalid_login(page, read_credentials, get_base_url):
    login_page = LoginPage(page)
    login_page.go_to_page(get_base_url)
    login_page.login_user(read_credentials[constants.INVALID_USERNAME], read_credentials[constants.INVALID_PASSWORD])

    assert login_page.is_login_error_displayed()

def test_locked_out_user(page, read_credentials, get_base_url):
    login_page = LoginPage(page)
    login_page.go_to_page(get_base_url)
    login_page.login_user(read_credentials[constants.LOCKED_USERNAME], read_credentials[constants.LOCKED_USER_PASSWORD])

    assert login_page.is_user_locked_message_displayed()
