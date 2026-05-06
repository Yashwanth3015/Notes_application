import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
def test_logout(logged_in_user):

    driver = logged_in_user

    # Wait for logout button
    logout_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@data-testid='logout']"
            )
        )
    )

    # Click using JavaScript
    driver.execute_script(
        "arguments[0].click();",
        logout_btn
    )

    # Wait until logout button disappears
    WebDriverWait(driver, 20).until_not(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@data-testid='logout']"
            )
        )
    )

    # Final validation
    assert "Logout" not in driver.page_source