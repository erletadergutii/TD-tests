from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MakeAvailablePage(LoginPage):
    """Page Object Model for clicking 'Make Available' button"""

    # Locators
    PROPERTY_NAV = (By.XPATH, '//*[@id="__next"]/nav/div[1]/div/div[2]/div/a')  # Property nav button
    MAKE_AVAILABLE_BUTTON = (By.XPATH, "//*[contains(text(), 'Make Available')]")  # Correct button locator
    UNAVAILABLE_BADGE = (By.XPATH, "//td/span[contains(text(), 'Unavailable')]")  # Before clicking
    AVAILABLE_BADGE = (By.XPATH, "//td/span[contains(text(), 'Available')]")  # After clicking

    def click_property_nav(self):
        """Navigate to the Property List page"""
        self.click(*self.PROPERTY_NAV)

    def click_make_available_button(self):
        try: 
            self.find_element(*self.MAKE_AVAILABLE_BUTTON).click()
            return True
        except:
            return False

    def is_property_available(self):
        """Check if property status changed to 'Available'"""
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.AVAILABLE_BADGE))

    def is_property_unavailable(self):
        """Check if property status is 'Unavailable' before clicking"""
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.UNAVAILABLE_BADGE))
