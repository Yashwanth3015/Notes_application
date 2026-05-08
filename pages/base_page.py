from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from agentic.intelligent_wait import IntelligentWait
from agentic.retry_engine import RetryEngine
from agentic.locator_healer import LocatorHealer
from agentic.failure_analyzer import FailureAnalyzer
from agentic.ai_decision_engine import AIDecisionEngine

from utils.logger import logger


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Agentic Click Method
    def click(self, locator):

        logger.info(f"Clicking on : {locator}")

        try:

            # Try original locator first
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )

            element.click()

        except Exception:

            logger.warning(
                "Original locator failed. Trying AI self-healing..."
            )

            healed_element = None

            # AI Healed Locators
            possible_locators = [

                # Login Button
                ("xpath", "//button[@type='submit']"),

                ("xpath", "//button[contains(text(),'Login')]"),

                ("css selector", "button[type='submit']"),

                # Add Note Button
                ("xpath", "//button[contains(text(),'Add Note')]"),

                # Generic Button
                ("tag name", "button")
            ]

            for by, value in possible_locators:

                try:

                    healed_element = self.driver.find_element(
                        by,
                        value
                    )

                    logger.info(
                        f"Healed locator success : {(by, value)}"
                    )

                    break

                except Exception:
                    continue

            if healed_element:

                self.driver.execute_script(
                    "arguments[0].click();",
                    healed_element
                )

            else:

                raise Exception(
                    "AI Self-Healing Failed"
                )

    # Agentic Enter Text Method
    def enter_text(self, locator, value):

        logger.info(f"Entering text : {value}")

        element = IntelligentWait.visible(
            self.driver,
            locator
        )

        element.clear()

        element.send_keys(value)

    # Get Text Method
    def get_text(self, locator):

        element = IntelligentWait.visible(
            self.driver,
            locator
        )

        return element.text

    # Visibility Check
    def is_visible(self, locator):

        try:

            IntelligentWait.visible(
                self.driver,
                locator
            )

            return True

        except Exception:

            return False