from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Login button from your DOM
    login_btn = (By.CSS_SELECTOR, "[data-testid='open-login-view'] a")

    def load(self, url):
        self.driver.get(url)
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"    #anonymous function to check if page is fully loaded
        )

    def click_login(self):
        element = self.wait.until(EC.element_to_be_clickable(self.login_btn))
        self.driver.execute_script("arguments[0].click();", element)