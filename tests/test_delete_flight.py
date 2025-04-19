import pytest
from selenium import webdriver
from pages.flights_delete_page import FlightDeletePage
import time


@pytest.fixture
def setup():
    """Fixture to initialize and quit the WebDriver"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")  # Replace with actual login page URL
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestDeleteFlight:
    def test_delete_flight(self, setup):
        flight_delete_page = FlightDeletePage(setup)

        flight_delete_page.login(username="testing1", password="test12")


        time.sleep(3)
        # Step 2: Click on "Flights" in the navbar
        flight_delete_page.click_flight_nav()

        time.sleep(3)

        # Step 3: Click on "Delete Flight" button
        flight_delete_page.click_delete_button()

        time.sleep(2)

        flight_delete_page.click_delete_flight_button()

        # Step 5: Validate the page after submitting
        assert "Flight List" in flight_delete_page.get_headline()