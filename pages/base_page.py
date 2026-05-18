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

        # Faster execution
        self.wait = WebDriverWait(
            driver,
            5
        )

    # =====================================================
    # AGENTIC AI CLICK METHOD
    # =====================================================

    def click(self, locator):

        logger.info(
            f"Clicking on : {locator}"
        )

        # -----------------------------------------
        # ACTION FUNCTION
        # -----------------------------------------

        def action():

            try:

                # ---------------------------------
                # ORIGINAL LOCATOR
                # ---------------------------------

                element = self.wait.until(
                    EC.element_to_be_clickable(
                        locator
                    )
                )

                element.click()

                logger.info(
                    "Original locator worked"
                )

                return True

            except Exception as e:

                # ---------------------------------
                # FAILURE ANALYSIS
                # ---------------------------------

                failure_type = (
                    FailureAnalyzer.analyze(e)
                )

                print("\n")
                print("=" * 60)
                print(
                    "AGENTIC AI FAILURE DETECTED"
                )
                print("=" * 60)

                print("\nFailure Type:")
                print(failure_type)

                print("\nOriginal Locator:")
                print(locator)

                logger.warning(
                    "Original locator failed. "
                    "Trying LongCat AI healing..."
                )

                # ---------------------------------
                # LONGCAT HEALING
                # ---------------------------------

                healed_element = (
                    LocatorHealer.heal(
                        self.driver,
                        locator,
                        e
                    )
                )

                # ---------------------------------
                # SCROLL
                # ---------------------------------

                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);",
                    healed_element
                )

                import time
                time.sleep(1)

                # ---------------------------------
                # JS CLICK
                # ---------------------------------

                self.driver.execute_script(
                    "arguments[0].click();",
                    healed_element
                )

                print("\nHealing Status:")
                print("SUCCESS")

                logger.info(
                    "AI self-healing successful"
                )

                return True

        # -----------------------------------------
        # RETRY ENGINE
        # -----------------------------------------

        try:

            RetryEngine.execute(
                action,
                retries=1,
                delay=1
            )

            print("\nRetry Status:")
            print("PASSED")

            print("=" * 60)
            print("\n")

        except Exception as final_error:

            print("\nRetry Status:")
            print("FAILED")

            print("=" * 60)
            print("\n")

            raise final_error

    # =====================================================
    # AGENTIC AI INPUT METHOD
    # =====================================================

    def enter_text(self, locator, value):

        logger.info(
            f"Entering text : {value}"
        )

        try:

            # -----------------------------------------
            # ORIGINAL INPUT LOCATOR
            # -----------------------------------------

            element = IntelligentWait.visible(
                self.driver,
                locator
            )

            element.clear()

            element.send_keys(value)

            logger.info(
                "Original input locator worked"
            )

        except Exception as e:

            print("\n")
            print("=" * 60)
            print(
                "AGENTIC AI INPUT FAILURE DETECTED"
            )
            print("=" * 60)

            print("\nFailure:")
            print(str(e))

            print("\nOriginal Locator:")
            print(locator)

            logger.warning(
                "Input locator failed. "
                "Trying LongCat AI healing..."
            )

            # -----------------------------------------
            # LONGCAT HEALING
            # -----------------------------------------

            healed_element = (
                LocatorHealer.heal(
                    self.driver,
                    locator,
                    e
                )
            )

            healed_element.clear()

            healed_element.send_keys(value)

            print("\nHealing Status:")
            print("SUCCESS")

            print("\nRetry Status:")
            print("PASSED")

            print("=" * 60)
            print("\n")

            logger.info(
                "AI input healing successful"
            )

    # =====================================================
    # GET TEXT METHOD
    # =====================================================

    def get_text(self, locator):

        element = IntelligentWait.visible(
            self.driver,
            locator
        )

        return element.text

    # =====================================================
    # VISIBILITY CHECK
    # =====================================================

    def is_visible(self, locator):

        try:

            IntelligentWait.visible(
                self.driver,
                locator
            )

            return True

        except Exception:

            return False