import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.config import UI_URL, EMAIL, PASSWORD


@allure.feature("Login")
@allure.story("Valid Login")
@pytest.mark.ui
def test_login_valid_credentials(driver):

    driver.get(UI_URL)

    wait = WebDriverWait(driver, 20)

    # Click homepage Login button
    home_login_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(text(),'Login')]"
            )
        )
    )

    home_login_btn.click()

    # Use existing working login method
    login = LoginPage(driver)

    login.login(
        EMAIL,
        PASSWORD
    )

    # Validate login success
    assert login.is_login_successful(), \
        "Login failed with valid credentials"