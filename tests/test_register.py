import pytest
from pages.register_page import RegisterPage
from selenium import webdriver



@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestRegister:
    def test_valid_register(self, setup):  # Pass setup as a parameter
        register_page = RegisterPage(setup)  # Use setup (driver)
        register_page.register(username="erletatest1", password="letaleta1", confirm_password="letaleta1", dropdown_option="Host")
        assert "Welcome back" in register_page.get_headline()