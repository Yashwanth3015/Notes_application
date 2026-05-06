from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    email_input = (
        By.NAME,
        "email"
    )

    password_input = (
        By.NAME,
        "password"
    )

    login_btn = (
        By.XPATH,
        "//button[@type='submit']"
    )

    add_note_btn = (
        By.XPATH,
        "//button[contains(text(),'Add Note')]"
    )

    error_message = (
        By.XPATH,
        "//*[contains(text(),'Incorrect')]"
    )

    loading_spinner = (
        By.CLASS_NAME,
        "loading"
    )

    def login(self, email, password):

        self.enter_text(
            self.email_input,
            email
        )

        self.enter_text(
            self.password_input,
            password
        )

        self.click(self.login_btn)

    def is_login_successful(self):

        try:

            # wait until page completely loads
            self.wait.until(
                lambda d: d.execute_script(
                    "return document.readyState"
                ) == "complete"
            )

            # wait until Add Note button appears
            self.wait.until(
                EC.visibility_of_element_located(
                    self.add_note_btn
                )
            )

            return True

        except Exception as e:

            print(f"Login validation failed: {e}")

            return False

    def is_error_displayed(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.error_message
                )
            )

            return True

        except Exception as e:

            print(f"Error validation failed: {e}")

            return False