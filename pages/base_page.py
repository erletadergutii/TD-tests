from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, by, value: str):
        return self.wait.until(EC.visibility_of_element_located((by, value)))
    
    def click(self, by, value: str):
        element = self.find_element(by, value)
        element.click()

    def enter_text(self, by, value: str, text: str):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)
