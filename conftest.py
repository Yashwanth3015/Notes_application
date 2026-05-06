import pytest
import allure
import logging
import os
from datetime import datetime
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import UI_URL, EMAIL, PASSWORD


# ----------------------------
# Logging setup
# ----------------------------
logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


@pytest.fixture(scope="function")
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    # Stability for parallel execution
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def logged_in_user(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    with allure.step("Open application"):
        home.load(UI_URL)

    with allure.step("Navigate to login page"):
        home.click_login()

    with allure.step("Perform login"):
        login.login(EMAIL, PASSWORD)

    logger.info("Login successful")

    return driver


# ----------------------------
# Screenshot + Logs on failure
# ----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            # create folder
            os.makedirs("screenshots", exist_ok=True)

            # unique file name
            file_name = f"screenshots/{item.name}_{datetime.now().strftime('%H%M%S')}.png"

            # save screenshot
            driver.save_screenshot(file_name)

            # attach to allure
            allure.attach.file(
                file_name,
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG
            )

        # attach real logs file (if exists)
        log_file = "logs/test.log"
        if os.path.exists(log_file):
            allure.attach.file(
                log_file,
                name="Logs",
                attachment_type=AttachmentType.TEXT
            )