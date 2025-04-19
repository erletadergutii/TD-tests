from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta



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

    def select_option(self, by, value: str, option: str):
        element = self.find_element(by, value)
        select = Select(element)
        select.select_by_visible_text(option)

    def select_option_by_index(self, by, value: str, index: int):
        element = self.find_element(by, value)
        select = Select(element)
        select.select_by_index(index)


    def enter_future_datetime(self, by, value: str, days_ahead: int = 5):
        future_date = datetime.now() + timedelta(days=days_ahead)

        print(by, value, days_ahead)
        month = future_date.strftime('%m')  # 2 digits
        day = future_date.strftime('%d')    # 2 digits
        year = future_date.strftime('%Y')   # 4 digits
        hour = future_date.strftime('%I')   # 2 digits, 12-hour format (01-12)
        minute = future_date.strftime('%M') # 2 digits
        am_pm = future_date.strftime('%p')  # AM or PM

        # Determine AM (0) or PM (1)
        am_pm_flag = '0' if am_pm == 'AM' else '1'

        # Build the final string
        final_string = f"{month}{day}00{year}{hour}{minute}{am_pm_flag}"

        element = self.driver.find_element(by, value)
        element.clear()
        element.send_keys(final_string)



    def login(self):
        self.enter_text(By.XPATH, '//*[@id=":R6cm:-form-item"]', USERNAME)
        self.enter_text(By.XPATH, '//*[@id=":Racm:-form-item"]', PASSWORD)
        self.click(By.XPATH, '//*[@id="__next"]/main/div[1]/div/form/button')

    
