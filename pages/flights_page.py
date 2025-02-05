from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class FlightPage(LoginPage):
    # Locators
    HEADLINE_TEXT = (By.TAG_NAME, "h1")
    FLIGHT_NAV = (By.XPATH, "//*[@id='__next']/nav/div[1]/div/div[2]/div/a[3]")
    ADD_FLIGHT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[1]/a')
    SELECT_AIRLINE = (By.CSS_SELECTOR, '[data-testid="airline"]')
    FLIGHT_NUMBER_INPUT = (By.XPATH, '//*[@id=":r47:-form-item"]')
    DEPARTURE_AIRPORT_SELECT= (By.XPATH, '//*[@id="__next"]/main/div[1]/form/div[3]/div[1]/select')
    ARRIVAL_AIRPORT_SELECT = (By.XPATH, '//*[@id="__next"]/main/div[1]/form/div[3]/div[2]/select')
    DEPARTURE_TIME_INPUT = (By.CSS_SELECTOR, "input[name='departure_time']")
    ARRIVAL_TIME_INPUT = (By.CSS_SELECTOR, "input[name='arrival_time']")
    DURATION_INPUT = (By.CSS_SELECTOR, "input[name='duration_minutes']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price_per_ticket']")
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/form/button')


    def click_flight_nav(self):
        self.click(*self.FLIGHT_NAV)

    def click_add_flight_button(self):
        self.click(*self.ADD_FLIGHT_BUTTON)

    def select_airline(self, airline: str):
        self.select_option(*self.SELECT_AIRLINE, airline)

    def enter_flight_number(self, flight_number: str):
        self.enter_text(*self.FLIGHT_NUMBER_INPUT, flight_number)
    
    def enter_departure_airport(self, departure_airport: str):
        self.select_option_by_index(*self.DEPARTURE_AIRPORT_SELECT, departure_airport, 1)
    

    def enter_arrival_airport(self, arrival_airport: str):
        self.select_option_by_index(*self.ARRIVAL_AIRPORT_SELECT, arrival_airport, 0)
    
    def enter_departure_time(self, departure_time: str):
        self.enter_future_datetime(*self.DEPARTURE_TIME_INPUT, days_ahead=5)
    
    def enter_arrival_time(self, arrival_time: str):
        self.enter_future_datetime(*self.ARRIVAL_TIME_INPUT, days_ahead=5)
    
    def enter_duration(self, duration: str):
        self.enter_text(*self.DURATION_INPUT, duration)
    
    def enter_price(self, price: str):
        self.enter_text(*self.PRICE_INPUT, price)



    def click_submit_button(self):
        self.click(*self.SUBMIT_BUTTON)

    def submit(self, flight_number: str, departure_airport: str, arrival_airport: str, 
              departure_time: str, arrival_time: str, airline: str, duration: str, price: str):
        self.select_airline(airline)
        self.enter_flight_number(flight_number)
        self.enter_departure_airport(departure_airport)
        self.enter_arrival_airport(arrival_airport)
        self.enter_departure_time(departure_time)
        self.enter_arrival_time(arrival_time)
        self.enter_duration(duration)
        self.enter_price(price)
        self.click_submit_button()


    def get_title(self):
        return self.driver.title
    
    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text
