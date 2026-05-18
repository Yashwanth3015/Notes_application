from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    # Login Button
    login_btn = (
        By.CSS_SELECTOR,
        "[data-testid='open-login-view'] a"
    )

    # Load Application
    def load(self, url):

        self.driver.get(url)

        self.wait.until(

            lambda d:
            d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    # Click Login
    def click_login(self):

        # IMPORTANT
        # Uses BasePage.click()
        # → Agentic AI enabled
        self.click(self.login_btn)