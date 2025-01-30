import pytest
from selenium import webdriver
from pages.airports_page import AirportsPage 
import time

@pytest.fixture
def setup():
    """Fixture to initialize and quit the WebDriver"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")  
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestAirport:
    def test_add_airport(self, setup):
        airport_page = AirportsPage(setup)

        # Step 1: Log in
        airport_page.login(username="testing1", password="test12")

        time.sleep(3)
        # Step 2: Click on "Airline" in the navbar
        airport_page.click_airport_text()

        time.sleep(3)

        # Step 3: Click on "Add Airline" button
        airport_page.click_add_airport_button()

        time.sleep(2)

        # Step 4: Fill in airline details
        airport_page.submit(code="ERL", airport_name="ERLETA", airport_city="ERLETA", airport_country="ERLETA")

        # Step 5: Validate the page after submitting
        assert "Airport List" in airport_page.get_headline()