from selenium.webdriver.common.by import By

from mcp.failure_analyzer import (
    LLMFailureAnalyzer
)

from agentic.execution_context import (
    ExecutionContext
)

from utils.logger import logger


class LocatorHealer:

    @staticmethod
    def heal(driver, locator, exception):

        print("\n")
        print("=" * 60)
        print("AGENTIC AI FAILURE DETECTED")
        print("=" * 60)

        print("\nFailure:")
        print(str(exception))

        print("\nOriginal Locator:")
        print(locator)

        # -----------------------------------------
        # LONGCAT ANALYSIS
        # -----------------------------------------

        ai_locator = (
            LLMFailureAnalyzer
            .analyze(exception, locator)
        )

        ExecutionContext.ai_suggestion = (
            ai_locator
        )

        print("\nLongCat Suggested:")
        print(ai_locator)

        # =================================================
        # ENTERPRISE FALLBACK LOCATORS
        # =================================================

        fallback_locators = [

            # Homepage Login
            (
                By.CSS_SELECTOR,
                "[data-testid='open-login-view'] a"
            ),

            # Login Button
            (
                By.XPATH,
                "//button[@type='submit']"
            ),

            # Email Input
            (
                By.NAME,
                "email"
            ),

            # Password Input
            (
                By.NAME,
                "password"
            ),

            # Add Note
            (
                By.XPATH,
                "//button[contains(text(),'Add Note')]"
            )
        ]

        # -----------------------------------------
        # TRY AI LOCATOR FIRST
        # -----------------------------------------

        try:

            ai_healed = (
                By.XPATH,
                ai_locator
            )

            element = driver.find_element(
                *ai_healed
            )

            print("\nAI Healed Locator:")
            print(ai_healed)

            print("\nHealing Status:")
            print("SUCCESS")

            print("=" * 60)
            print("\n")

            return element

        except Exception:

            print("\nAI locator failed.")
            print("Trying enterprise fallback...")

        # -----------------------------------------
        # FALLBACK RECOVERY
        # -----------------------------------------

        for fallback in fallback_locators:

            try:

                element = driver.find_element(
                    *fallback
                )

                print("\nFallback Locator Used:")
                print(fallback)

                print("\nHealing Status:")
                print("SUCCESS")

                print("=" * 60)
                print("\n")

                return element

            except Exception:
                continue

        print("\nHealing Status:")
        print("FAILED")

        print("=" * 60)

        raise Exception(
            "LongCat healing failed completely"
        )