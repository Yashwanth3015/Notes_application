from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from agentic.locator_healer import LocatorHealer


class IntelligentWait:

    @staticmethod
    def clickable(driver, locator, timeout=10):   #waits for element to be clickable, if not found tries healing

        try:

            return WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)      # continuously checks for element to be clickable until timeout
            )

        except Exception:

            # Self-healing ONLY for click actions
            return LocatorHealer.heal(
                driver,
                locator
            )

    @staticmethod
    def visible(driver, locator, timeout=10):

        # NO self-healing here
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator) #continuously checks for element visibility until timeout
        )