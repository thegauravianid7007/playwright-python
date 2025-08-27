from .BasePage import BasePage
class CartPage(BasePage):
    page_title_locator = "[data-test='title']"
    expected_page_title = "Your Cart"
    cart_items_locator = "[data-test='inventory-item']"
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def wait_for_cart_to_open(self):
        return self.wait_for_element_contains_text(self.page_title_locator, self.expected_page_title)

    def get_cart_items(self) -> list[str]:
        elements = self.page.locator(self.cart_items_locator).all_inner_texts()
        return [e.strip() for e in elements]