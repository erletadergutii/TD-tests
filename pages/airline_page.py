from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AirlinePage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//*[@id=":R6cm:-form-item"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id=":Racm:-form-item"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/form/button')
    HEADLINE_TEXT = (By.TAG_NAME, "h1")
    AIRLINE = (By.XPATH, "//*[@id='__next']/nav/div[1]/div/div[2]/div/a[2]")
    ADD_AIRLINE_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[1]/a')
    IATA_CODE_INPUT = (By.XPATH, "//*[@id=':rb:-form-item']")
    AIRLINE_NAME_INPUT = (By.XPATH, "//*[@id=':rc:-form-item']")
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/form/button')

    def enter_username(self, username: str):
        self.enter_text(*self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.enter_text(*self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)


    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def click_airline_text(self):
        self.click(*self.AIRLINE)

    def click_add_airline_button(self):
        self.click(*self.ADD_AIRLINE_BUTTON)

    def enter_iatcode(self, iatcode: str):
        self.enter_text(*self.IATA_CODE_INPUT, iatcode)
    
    def enter_airline_name(self, airline_name: str):
        self.enter_text(*self.AIRLINE_NAME_INPUT, airline_name)

    def click_submit_button(self):
        self.click(*self.SUBMIT_BUTTON)

    def submit(self, iatcode: str, airline_name: str):
        self.enter_iatcode(iatcode)
        self.enter_airline_name(airline_name)
        self.click_submit_button()

    def get_title(self):
        return self.driver.title
    
    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text
