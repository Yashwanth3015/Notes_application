import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
def test_logout(logged_in_user):

    driver = logged_in_user

    # Wait for logout button
    logout_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Logout')]")
        )
    )

    # Click logout
    logout_btn.click()

    # Wait until logout button disappears
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Logout')]")
        )
    )

    # Final validation
    assert "Logout" not in driver.page_source