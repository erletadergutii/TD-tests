import pytest
from pages.login_page import LoginPage
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self, setup):  # Pass setup as a parameter
        login_page = LoginPage(setup)  # Use setup (driver)
        login_page.login("leta1", "leta1")
        assert "Find Your Perfect Stay" in login_page.get_headline()