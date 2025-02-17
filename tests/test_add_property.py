import pytest
from selenium import webdriver
from pages.add_property_page import AddPropertyPage 
import time

@pytest.fixture
def setup():
    """Fixture to initialize and quit the WebDriver"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")  # Replace with actual login page URL
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestProperty:
    def test_add_property(self, setup):
        """Test logging in and adding a new property"""
        add_property_page = AddPropertyPage(setup)

        # Step 1: Log in
        add_property_page.login(username="propertytest", password="test1234")

        time.sleep(3)
        # Step 2: Click on "Property" in the navbar
        add_property_page.click_property_text()

        time.sleep(3)

        # Step 3: Click on "Add Airline" button
        add_property_page.click_add_property_button()

        time.sleep(2)

        # Step 4: Fill in airline details
        add_property_page.submit(property_name="Test Property", property_description="Test Description", property_location="Test Location", property_price="100", property_guests="2", dropdown_option="Hotel")

        # Step 5: Validate the page after submitting
        assert "Property List" in add_property_page.get_headline()