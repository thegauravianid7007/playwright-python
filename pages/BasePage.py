from playwright.sync_api import Page
import time


def wait_for_seconds(seconds):
    time.sleep(seconds)


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_page(self, url):
        self.page.goto(url)