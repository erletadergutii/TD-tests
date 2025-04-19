from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class FlightDeletePage(LoginPage):
    # Locators
    HEADLINE_TEXT = (By.TAG_NAME, "h1")
    FLIGHT_NAV = (By.XPATH, "//*[@id='__next']/nav/div[1]/div/div[2]/div/a[3]")
    CLICK_DELETE_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[2]/div/table/tbody/tr[1]/td[7]/div/button')
    DELETE_FLIGHT = (By.ID, 'delete')


    def click_flight_nav(self):
        self.click(*self.FLIGHT_NAV)

    def click_delete_button(self):
        self.click(*self.CLICK_DELETE_BUTTON)

    def click_delete_flight_button(self):
        self.click(*self.DELETE_FLIGHT)

    def get_title(self):
        return self.driver.title
    
    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text