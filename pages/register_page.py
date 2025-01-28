from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegisterPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//*[@id=":R6cm:-form-item"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id=":Racm:-form-item"]')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//*[@id=":Recm:-form-item"]')    
    DROPDOWN = (By.XPATH, "//*[@id='__next']/main/div[1]/div/form/div[4]/select")
    SIGN_UP_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/form/button')
    HEADLINE_TEXT = (By.TAG_NAME, "h2")

    def enter_username(self, username: str):
        self.enter_text(*self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.enter_text(*self.PASSWORD_INPUT, password)

    def confirm_password(self, password: str):
        self.enter_text(*self.CONFIRM_PASSWORD_INPUT, password)

    def select_dropdown_option(self, option_text: str):
        self.select_option(*self.DROPDOWN, option_text)  

    def click_sign_up_button(self):
        self.click(*self.SIGN_UP_BUTTON)

    def register(self, username: str, password: str, confirm_password: str, dropdown_option: str):
        self.enter_username(username)
        self.enter_password(password)
        self.confirm_password(confirm_password)
        self.select_dropdown_option(dropdown_option)
        self.click_sign_up_button()

    def get_title(self):
        return self.driver.title
    
    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text
