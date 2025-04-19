import pytest
from selenium import webdriver
from pages.make_available_page import MakeAvailablePage
import time

@pytest.fixture
def setup():
    """Fixture to initialize and quit the WebDriver"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")  # Replace with actual login page URL
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestMakeAvailable:
    def test_make_property_available(self, setup):
        """Test clicking 'Make Available' and verifying status change"""
        make_available_page = MakeAvailablePage(setup)

        # Step 1: Log in
        make_available_page.login(username="propertytest", password="test1234")

        # Step 2: Navigate to Property List Page
        make_available_page.click_property_nav()
        time.sleep(3)  # Wait for the page to load
 
        test_passed = make_available_page.click_make_available_button()
        time.sleep(3)  # Wait for status update

        # Step 5: Verify the property is now marked as available
        assert test_passed
