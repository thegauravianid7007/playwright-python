import pytest

from pages.LoginPage import LoginPage
from utils.JSONReader import JSONReader
import constants

@pytest.fixture
def credentials() -> dict:
    reader = JSONReader()
    return reader.read_json()

def test_valid_login(page, credentials):
    login_page = LoginPage(page)
    login_page.go_to_page(credentials[constants.BASE_URL])
    login_page.login_user(credentials[constants.USERNAME], credentials[constants.PASSWORD])

    assert login_page.get_current_url().endswith(constants.INVENTORY_URL)

def test_invalid_login(page, credentials):
    login_page = LoginPage(page)
    login_page.go_to_page(credentials[constants.BASE_URL])
    login_page.login_user(credentials[constants.INVALID_USERNAME], credentials[constants.INVALID_PASSWORD])

    assert login_page.is_login_error_displayed()

def test_locked_out_user(page, credentials):
    login_page = LoginPage(page)
    login_page.go_to_page(credentials[constants.BASE_URL])
    login_page.login_user(credentials[constants.LOCKED_USERNAME], credentials[constants.LOCKED_USER_PASSWORD])

    assert login_page.is_user_locked_message_displayed()
