import pytest
from selenium import webdriver
from pages.flights_page import FlightPage 
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
    def test_add_flight(self, setup):
        flight_page = FlightPage(setup)

        flight_page.login(username="testing1", password="test12")


        time.sleep(3)
        # Step 2: Click on "Flights" in the navbar
        flight_page.click_flight_nav()



        time.sleep(3)

        # Step 3: Click on "Add Flight" button
        flight_page.click_add_flight_button()



        time.sleep(2)

        # Step 4: Fill in airline details
        flight_page.submit(flight_number="FL1123", departure_airport=2, arrival_airport=4, departure_days_ahead=5, arrival_days_ahead=6, airline="Test Airline", duration="120", price="299.99")

        # Step 5: Validate the page after submitting
        assert "Flight List" in flight_page.get_headline()