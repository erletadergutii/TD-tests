from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class BookFlightPage(LoginPage):
    HEADLINE_TEXT = (By.TAG_NAME, "h1")
    BOOK_FLIGHT_NAV = (By.XPATH, '//*[@id="__next"]/nav/div[1]/div/div[2]/a[3]')
    BOOK_FLIGHT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/div/a/div/div[3]/button')
    YOUR_NAME_INPUT = (By.CSS_SELECTOR, "input[name='customerName']")
    NUMBER_OF_SEATS_INPUT = (By.CSS_SELECTOR, "input[name='seats']")
    IFRAME = (By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame']")  # ✅ Dynamic iframe selector
    PAY_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/div/div[2]/div[2]/form/div[4]/button')

    def click_flight_nav(self):
        self.click(*self.BOOK_FLIGHT_NAV)

    def click_book_flight_button(self):
        self.click(*self.BOOK_FLIGHT_BUTTON)

    def enter_your_name(self, your_name: str):
        self.enter_text(*self.YOUR_NAME_INPUT, your_name)

    def enter_number_of_seats(self, number_of_seats: str):
        self.enter_text(*self.NUMBER_OF_SEATS_INPUT, number_of_seats)

    def switch_to_card_iframe(self):
        iframe = self.find_element(*self.IFRAME)
        self.driver.switch_to.frame(iframe)  # ✅ Switch into iframe

    def enter_card_number(self, card_number: str):
        self.switch_to_card_iframe()  # ✅ Step 1
        card_input = self.find_element(By.CSS_SELECTOR, "input[name='cardnumber']")
        card_input.send_keys(card_number)  # ✅ Step 2
        self.driver.switch_to.default_content()  # ✅ Step 3

    def click_pay_button(self):
        self.click(*self.PAY_BUTTON)

    def submit(self, your_name: str, number_of_seats: str, card_number: str):
        self.enter_your_name(your_name)
        self.enter_number_of_seats(number_of_seats)
        self.enter_card_number(card_number)
        self.click_pay_button()

    def get_title(self):
        return self.driver.title

    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text
