from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):

        logger.info(f"Clicking on : {locator}")

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        try:
            element.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    def enter_text(self, locator, value):

        logger.info(f"Entering text : {value}")

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(value)

    def get_text(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def is_visible(self, locator):

        try:

            self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except Exception:

            return False