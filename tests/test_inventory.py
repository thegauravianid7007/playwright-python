from conftest import get_base_url, read_credentials
from utils.JSONReader import JSONReader
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from constants.auth import USERNAME, PASSWORD
import pytest

test_data = JSONReader.get_value_from_json("../testdata/products.json", "products")

@pytest.mark.parametrize("product_data", test_data)
def test_add_items_to_cart(page, product_data, read_credentials, get_base_url):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.go_to_page(get_base_url)
    login_page.login_user(read_credentials[USERNAME], read_credentials[PASSWORD])
    for product in product_data["names"]:
        inventory_page.add_item_to_cart(product)

    assert inventory_page.get_cart_count() == len(product_data["names"])