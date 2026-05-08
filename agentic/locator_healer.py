from selenium.webdriver.common.by import By

from utils.logger import logger


class LocatorHealer:

    @staticmethod
    def heal(driver, locator):

        logger.warning(
            f"Trying to heal locator : {locator}"
        )

        possible_locators = [

            (By.XPATH, "//button[@type='submit']"),

            (By.XPATH, "//button[contains(text(),'Login')]"),

            (By.CSS_SELECTOR, "button[type='submit']"),

            (By.TAG_NAME, "button")
        ]

        for new_locator in possible_locators:

            try:

                element = driver.find_element(
                    *new_locator
                )

                logger.info(
                    f"Healed locator found : {new_locator}"
                )

                return element

            except Exception:
                continue

        raise Exception(
            "Unable to heal locator"
        )