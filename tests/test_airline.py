import pytest
from selenium import webdriver
from pages.airline_page import AirlinePage 
import time

@pytest.fixture
def setup():
    """Fixture to initialize and quit the WebDriver"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")  # Replace with actual login page URL
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestAirline:
    def test_add_airline(self, setup):
        """Test logging in and adding a new airline"""
        airline_page = AirlinePage(setup)

        # Step 1: Log in
        airline_page.login(username="testing1", password="test12")

        time.sleep(3)
        # Step 2: Click on "Airline" in the navbar
        airline_page.click_airline_text()

        time.sleep(3)

        # Step 3: Click on "Add Airline" button
        airline_page.click_add_airline_button()

        time.sleep(2)

        # Step 4: Fill in airline details
        airline_page.submit(iatcode="EER", airline_name="Test Airline211")

        # Step 5: Validate the page after submitting
        assert "Airline List" in airline_page.get_headline()