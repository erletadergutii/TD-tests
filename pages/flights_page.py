from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class FlightPage(LoginPage):
    # Locators
    HEADLINE_TEXT = (By.TAG_NAME, "h1")
    FLIGHT_NAV = (By.XPATH, "//*[@id='__next']/nav/div[1]/div/div[2]/div/a[3]")
    ADD_FLIGHT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[1]/a')
    SELECT_AIRLINE = (By.ID, 'airline')
    FLIGHT_NUMBER_INPUT = (By.CSS_SELECTOR, "input[name='flight_number']")
    DEPARTURE_AIRPORT_SELECT= (By.ID, 'departure')
    ARRIVAL_AIRPORT_SELECT = (By.ID, 'arrival')
    DEPARTURE_TIME_INPUT = (By.CSS_SELECTOR, "input[name='departure_time']")
    ARRIVAL_TIME_INPUT = (By.CSS_SELECTOR, "input[name='arrival_time']")
    DURATION_INPUT = (By.CSS_SELECTOR, "input[name='duration_minutes']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price_per_ticket']")
    SUBMIT_BUTTON = (By.ID, 'submit')


    def click_flight_nav(self):
        self.click(*self.FLIGHT_NAV)

    def click_add_flight_button(self):
        self.click(*self.ADD_FLIGHT_BUTTON)

    def select_airline(self, airline: str):
        self.select_option(*self.SELECT_AIRLINE, airline)

    def enter_flight_number(self, flight_number: str):
        self.enter_text(*self.FLIGHT_NUMBER_INPUT, flight_number)
    
    def enter_departure_airport(self, departure_airport: str):
        self.select_option_by_index(*self.DEPARTURE_AIRPORT_SELECT, departure_airport)
    

    def enter_arrival_airport(self, arrival_airport: str):
        self.select_option_by_index(*self.ARRIVAL_AIRPORT_SELECT, arrival_airport)
    
    def enter_duration(self, duration: str):
        self.enter_text(*self.DURATION_INPUT, duration)
    
    def enter_price(self, price: str):
        self.enter_text(*self.PRICE_INPUT, price)


    def click_submit_button(self):
        self.click(*self.SUBMIT_BUTTON)

    def submit(self, flight_number: str, departure_airport: str, arrival_airport: str, 
              departure_days_ahead: int, arrival_days_ahead: int, airline: str, duration: str, price: str):
        self.select_airline(airline)
        self.enter_flight_number(flight_number)
        self.enter_departure_airport(departure_airport)
        self.enter_arrival_airport(arrival_airport)
        self.enter_future_datetime(*self.DEPARTURE_TIME_INPUT, days_ahead=departure_days_ahead)
        self.enter_future_datetime(*self.ARRIVAL_TIME_INPUT, days_ahead=arrival_days_ahead)
        self.enter_duration(duration)
        self.enter_price(price)
        self.click_submit_button()


    def get_title(self):
        return self.driver.title
    
    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text
