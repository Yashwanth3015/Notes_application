from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
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
        "//*[contains(text(),'Incorrect email address or password')]"
    )

    # Login Method
    def login(self, email, password):

        email_field = self.wait.until(
            EC.presence_of_element_located(
                self.email_input
            )
        )

        email_field.clear()
        email_field.send_keys(email)

        password_field = self.wait.until(
            EC.presence_of_element_located(
                self.password_input
            )
        )

        password_field.clear()
        password_field.send_keys(password)

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.login_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_button
        )

    # Success Validation
    def is_login_successful(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.add_note_btn
                )
            )

            return True

        except:
            return False

    # Error Validation
    def is_error_displayed(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.error_message
                )
            )

            return True

        except:
            return False