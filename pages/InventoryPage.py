from .BasePage import BasePage, wait_for_seconds
from constants import products

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    product_add_to_cart_locators = {
        products.BACKPACK: "[data-test='add-to-cart-sauce-labs-backpack']",
        products.BIKE_LIGHT: "[data-test='add-to-cart-sauce-labs-bike-light']",
        products.BOLT_TSHIRT: "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']",
        products.FLEECE_JACKET: "[data-test='add-to-cart-sauce-labs-fleece-jacket']",
        products.ONESIE: "[data-test='add-to-cart-sauce-labs-onesie']",
        products.RED_TSHIRT: "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']",
    }

    product_remove_from_cart_locators = {
        products.BACKPACK: "[data-test='remove-sauce-labs-backpack']",
        products.BIKE_LIGHT: "[data-test='remove-sauce-labs-bike-light']",
        products.BOLT_TSHIRT: "[data-test='remove-sauce-labs-bolt-t-shirt']",
        products.FLEECE_JACKET: "[data-test='remove-sauce-labs-fleece-jacket']",
        products.ONESIE: "[data-test='remove-sauce-labs-onesie']",
        products.RED_TSHIRT: "[data-test='remove-test.allthethings()-t-shirt-(red)']",
    }

    cart_count_locator = "//span[contains(@class,'shopping_cart_badge')]"
    open_cart_button = "[data-test='shopping-cart-link']"

    page_title_locator = "[data-test='title']"
    expected_page_title = "Products"

    def wait_for_shopping_page_to_open(self):
        return self.wait_for_element_contains_text(self.page_title_locator, self.expected_page_title)

    def add_item_to_cart(self, item_name: str):
        locator = self.product_add_to_cart_locators[item_name]
        if not locator:
            raise ValueError(f"No locator found for {item_name}")
        self.page.locator(locator).click()

    def get_cart_count(self) -> int:
        cart_badge = self.page.locator(self.cart_count_locator)
        try:
            if cart_badge.is_visible():
                text = int(self.page.locator(self.cart_count_locator).inner_text())
                print(f"Cart count is {text}")
                return text
        except Exception:
            pass
        print("Cart is empty")
        return 0

    def open_cart(self):
        self.page.locator(self.open_cart_button).wait_for(state = "visible")
        self.page.locator(self.open_cart_button).click()

    def remove_product_from_cart(self, item_name:str):
        locator = self.product_remove_from_cart_locators[item_name]
        if not locator:
            raise ValueError(f"No locator found for {item_name}")
        self.page.locator(locator).click()



