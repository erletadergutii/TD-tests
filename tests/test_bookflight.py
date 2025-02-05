import pytest
from selenium import webdriver
from pages.book_flight_page import BookFlightPage 
import time


@pytest.fixture
def setup():
    """Fixture to initialize and quit the WebDriver"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")  # Replace with actual login page URL
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestBookFlight:
    def test_book_flight(self, setup):
        """Test logging in and adding a new airline"""
        book_flight_page = BookFlightPage(setup)


        # Step 1: Log in
        book_flight_page.login(username="testing1", password="test12")


        time.sleep(3)
        # Step 2: Click on "Book Flight" in the navbar
        book_flight_page.click_flight_nav()


        time.sleep(3)

        # Step 3: Click on "Book Flight" button
        book_flight_page.click_book_flight_button()


        time.sleep(2)

        # Step 4: Fill in flight details
        book_flight_page.submit(your_name="Erleta", number_of_seats="0", card_number="4242424242424242122911110001")  

        time.sleep(5)


        # Step 5: Validate the page after submitting
        assert "Find Your Perfect Stay" in book_flight_page.get_headline()