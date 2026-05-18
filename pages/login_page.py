from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

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
        "//button[@type='submitted']"
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

        self.enter_text(
            self.email_input,
            email
        )

        self.enter_text(
            self.password_input,
            password
        )

        # IMPORTANT
        # This now uses agentic AI self-healing
        self.click(self.login_btn)

    # Success Validation
    def is_login_successful(self):

        return self.is_visible(
            self.add_note_btn
        )

    # Error Validation
    def is_error_displayed(self):

        return self.is_visible(
            self.error_message
        )