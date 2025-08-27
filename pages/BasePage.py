from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect
import time


def wait_for_seconds(seconds):
    time.sleep(seconds)


class BasePage:
    left_menu = "#react-burger-menu-btn"
    logout_left_menu = "#logout_sidebar_link"

    def __init__(self, page: Page):
        self.page = page

    def go_to_page(self, url):
        self.page.goto(url)

    def is_element_visible(self, selector, timeout: int = 5000) -> bool:
        """
        Returns True if the element is visible, False otherwise.
        :param selector:
        :param timeout:
        :return:
        """
        try:
            self.page.locator(selector).wait_for(state = "visible", timeout = timeout)
            return True
        except PlaywrightTimeoutError:
            return False

    def get_current_url(self) -> str:
        return self.page.url

    def open_left_menu(self):
        self.page.locator(self.left_menu).wait_for(state = "visible")
        self.page.locator(self.left_menu).click()
        self.page.locator(self.logout_left_menu).wait_for(state = "visible")

    def logout_user(self):
        #self.page.locator(self.logout_left_menu).wait_for(state = "visible")
        self.page.locator(self.logout_left_menu).click()

    def wait_for_element_contains_text(self, locator: str, text: str, timeout: int = 5, poll_time: float = 0.5):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                element = self.page.locator(locator)
                if element.is_visible():
                    current_text = element.inner_text().strip()
                    if text in current_text:
                        return True
            except Exception:
                pass
            time.sleep(poll_time)

        return False

