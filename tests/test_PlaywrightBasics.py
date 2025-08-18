def test_open_saucedemo(page):
    page.goto("https://www.saucedemo.com/")
    assert "Swag Labs" in page.title()

def test_valid_login(page):
    page.goto("https://www.saucedemo.com/")
    