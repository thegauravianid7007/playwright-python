import pytest
from playwright.sync_api import sync_playwright
from utils.JSONReader import JSONReader
import constants

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def read_credentials() -> dict:
    reader = JSONReader()
    return reader.read_json()

@pytest.fixture(scope="function")
def get_base_url(read_credentials) -> str:
    return read_credentials[constants.BASE_URL]