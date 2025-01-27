from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//*[@id=":R6cm:-form-item"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id=":Racm:-form-item"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/form/button')
    HEADLINE_TEXT = (By.TAG_NAME, "h1")

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


    def get_title(self):
        return self.driver.title
    
    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text
