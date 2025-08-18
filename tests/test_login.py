from pages.BasePage import wait_for_seconds
from pages.LoginPage import LoginPage
from utils.JSONReader import JSONReader

def test_valid_login(page):
    login_page = LoginPage(page)
    reader = JSONReader()
    credentials = reader.read_json()

    login_page.go_to_page(credentials["base_url"])
    login_page.login_user(credentials["username"], credentials["password"])
    assert login_page.page.url.endswith("/inventory.html")
    wait_for_seconds(3)