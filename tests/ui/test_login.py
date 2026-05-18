import pytest
import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage

from utils.config import (
    UI_URL,
    EMAIL,
    PASSWORD
)


@allure.feature("Login")
@allure.story("Valid Login")
@pytest.mark.ui
def test_login_valid_credentials(driver):

    # Home Page Object
    home = HomePage(driver)

    # Login Page Object
    login = LoginPage(driver)

    # Open Application
    home.load(UI_URL)

    # IMPORTANT 😄
    # Uses BasePage.click()
    # LongCat healing enabled

    home.click_login()

    # Perform Login
    login.login(
        EMAIL,
        PASSWORD
    )

    # Validate Login
    assert login.is_login_successful()