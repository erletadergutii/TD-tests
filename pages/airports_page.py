from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class AirportsPage(LoginPage):
    
    HEADLINE_TEXT = (By.TAG_NAME, "h1")
    AIRPORT = (By.XPATH, "//*[@id='__next']/nav/div[1]/div/div[2]/div/a[1]")
    ADD_AIRPORT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[1]/a')
    CODE_INPUT = (By.CSS_SELECTOR, "input[name='code']")
    AIRPORT_NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    AIRPORT_CITY_INPUT = (By.CSS_SELECTOR, "input[name='city']")
    AIRPORT_COUNTRY_INPUT =(By.CSS_SELECTOR, "input[name='country']") 
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/form/button')


    def click_airport_text(self):
        self.click(*self.AIRPORT)

    def click_add_airport_button(self):
        self.click(*self.ADD_AIRPORT_BUTTON)

    def enter_code(self, code: str):
        self.enter_text(*self.CODE_INPUT, code)
    
    def enter_airport_name(self, airport_name: str):
        self.enter_text(*self.AIRPORT_NAME_INPUT, airport_name)

    def enter_airport_city(self, airport_city: str):
        self.enter_text(*self.AIRPORT_CITY_INPUT, airport_city)

    def enter_airport_country(self, airport_country: str):
        self.enter_text(*self.AIRPORT_COUNTRY_INPUT, airport_country)

    def click_submit_button(self):
        self.click(*self.SUBMIT_BUTTON)

    def submit(self, code: str, airport_name: str, airport_city: str, airport_country: str):
        self.enter_code(code)
        self.enter_airport_name(airport_name)
        self.enter_airport_city(airport_city)
        self.enter_airport_country(airport_country)
        self.click_submit_button()

    def get_title(self):
        return self.driver.title
    
    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text
