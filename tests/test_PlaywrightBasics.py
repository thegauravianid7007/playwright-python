def test_open_saucedemo(page):
    page.goto("https://www.saucedemo.com/")
    assert "Swag Labs" in page.title()