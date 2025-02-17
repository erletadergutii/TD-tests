from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class AddPropertyPage(LoginPage):
    
    HEADLINE_TEXT = (By.TAG_NAME, "h1")
    PROPERTY = (By.XPATH, '//*[@id="__next"]/nav/div[1]/div/div[2]/div/a')
    ADD_PROPERTY_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[1]/a')
    PROPERTY_NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    PROPERTY_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PROPERTY_LOCATION_INPUT = (By.CSS_SELECTOR, "input[name='location']")
    PROPERTY_PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price_per_night']")
    PROPERTY_GUESTS_INPUT = (By.CSS_SELECTOR, "input[name='max_guests']")
    PROPERTY_TYPE_INPUT = (By.XPATH, '//*[@id="__next"]/main/div[1]/form/div[6]/select')
    PROPERTY_IMAGE_INPUT = (By.CSS_SELECTOR, "input[name='image_url']")
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div[1]/form/button')


    def click_property_text(self):
        self.click(*self.PROPERTY)

    def click_add_property_button(self):
        self.click(*self.ADD_PROPERTY_BUTTON)

    def enter_property_name(self, property_name: str):
        self.enter_text(*self.PROPERTY_NAME_INPUT, property_name)
    
    def enter_property_description(self, property_description: str):
        self.enter_text(*self.PROPERTY_DESCRIPTION_INPUT, property_description)


    def enter_property_location(self, property_location: str):
        self.enter_text(*self.PROPERTY_LOCATION_INPUT, property_location)

    def enter_property_price(self, property_price: str):
        self.enter_text(*self.PROPERTY_PRICE_INPUT, property_price) 

    def enter_property_guests(self, property_guests: str):
        self.enter_text(*self.PROPERTY_GUESTS_INPUT, property_guests)

    def select_dropdown_option(self, option_text: str):
        self.select_option(*self.PROPERTY_TYPE_INPUT, option_text)
    
    def enter_property_image(self, property_image: str):
        self.enter_text(*self.PROPERTY_IMAGE_INPUT, property_image)

    def click_submit_button(self):
        self.click(*self.SUBMIT_BUTTON)

    def submit(self, property_name: str, property_description: str, property_location: str, property_price: str, property_guests: str, dropdown_option: str):
        self.enter_property_name(property_name)
        self.enter_property_description(property_description)
        self.enter_property_location(property_location)
        self.enter_property_price(property_price)
        self.enter_property_guests(property_guests)
        self.select_dropdown_option(dropdown_option)
        self.click_submit_button()

    def get_title(self):
        return self.driver.title
    
    def get_headline(self):
        return self.find_element(*self.HEADLINE_TEXT).text
