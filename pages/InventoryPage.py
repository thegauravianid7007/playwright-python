from .BasePage import BasePage, wait_for_seconds
from constants import products

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    product_add_to_cart_locators = {
        products.BACKPACK: "#add-to-cart-sauce-labs-backpack",
        products.BIKE_LIGHT: "#add-to-cart-sauce-labs-bike-light",
        products.BOLT_TSHIRT: "#add-to-cart-sauce-labs-bolt-t-shirt",
        products.FLEECE_JACKET: "#add-to-cart-sauce-labs-fleece-jacket",
        products.ONESIE: "#add-to-cart-sauce-labs-onesie",
        products.RED_TSHIRT: "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']",
    }

    cart_count_locator = "//span[contains(@class,'shopping_cart_badge')]"

    def add_item_to_cart(self, item_name: str):
        locator = self.product_add_to_cart_locators[item_name]
        self.page.locator(locator).click()

    def get_cart_count(self) -> int:
        print(f"Cart count is {self.page.locator(self.cart_count_locator).inner_text()}")
        self.page.locator(self.cart_count_locator).wait_for(state="visible")
        return int(self.page.locator(self.cart_count_locator).inner_text())

