from .BasePage import BasePage

class LoginPage(BasePage):
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    invalid_login_text = "//h3[contains(text(),'Epic sadface: Username and password do not match any user in this service')]"
    locked_user_text = "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out.')]"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def login_user(self, username:str, password:str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_login_error_displayed(self):
        return self.is_element_visible(self.invalid_login_text)

    def is_user_locked_message_displayed(self):
        return self.is_element_visible(self.locked_user_text)