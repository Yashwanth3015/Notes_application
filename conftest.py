import pytest
import allure
import logging
import os

from datetime import datetime

from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage

from utils.config import UI_URL, EMAIL, PASSWORD


# =====================================================
# CREATE FOLDERS
# =====================================================

os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)


# =====================================================
# LOGGING SETUP
# =====================================================

logging.basicConfig(            #configures framework logging system
    filename="logs/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()    #creates reusable logger objects


# =====================================================
# PYTEST CUSTOM OPTION
# =====================================================

def pytest_addoption(parser):

    parser.addoption(
        "--env",
        action="store",
        default="local",
        help="Execution environment: local or remote"
    )


# =====================================================
# SELENIUM DRIVER FIXTURE
# =====================================================

@pytest.fixture(scope="function") #creates browser session for each test function and ensures cleanup after test execution
def driver(request):

    execution_env = request.config.getoption("--env") #reads the custom command-line option to determine execution environment 

    chrome_options = Options()  #creates browser configuration object 

    # -----------------------------------------
    # COMMON OPTIONS
    # -----------------------------------------

    chrome_options.add_argument("--disable-notifications")

    chrome_options.add_argument("--disable-popup-blocking")

    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--disable-gpu")

    chrome_options.add_argument("--window-size=1920,1080")

    chrome_options.add_argument("--disable-extensions")

    chrome_options.add_argument("--remote-allow-origins=*")

    prefs = {
        "profile.default_content_setting_values.notifications": 2   #permanently blocks notifications for the browser session
    }

    chrome_options.add_experimental_option(
        "prefs",
        prefs
    )

    # =================================================
    # LOCAL EXECUTION
    # =================================================

    if execution_env == "local":

        logger.info("Starting LOCAL Chrome browser")

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=chrome_options
        )

    # =================================================
    # REMOTE EXECUTION (SELENIUM GRID / DOCKER)
    # =================================================

    elif execution_env == "remote":

        logger.info("Connecting to Selenium Grid")

        chrome_options.add_argument("--headless=new")

        driver = webdriver.Remote(

            command_executor="http://localhost:4444/wd/hub",

            options=chrome_options
        )

    else:

        raise ValueError(
            f"Invalid environment: {execution_env}"
        )

    logger.info("Browser session started")

    yield driver

    logger.info("Closing browser session")

    driver.quit()


# =====================================================
# LOGIN FIXTURE
# =====================================================

@pytest.fixture(scope="function") #creates a logged-in user fixture for each test function
def logged_in_user(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    with allure.step("Open application"):

        logger.info("Opening application")

        home.load(UI_URL)

    with allure.step("Navigate to login page"):

        logger.info("Clicking login button")

        home.click_login()

    with allure.step("Perform login"):

        logger.info("Performing login")

        login.login(EMAIL, PASSWORD)

    logger.info("Login successful")

    return driver


# =====================================================
# SCREENSHOT + LOGS ON FAILURE
# =====================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):   #hook implementation that executes after each test to check if it failed and capture screenshot

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed: #it checks if acutal test execution phase failed (not setup or teardown)

        driver = item.funcargs.get("driver", None)   #funcrags contains fixture values used in the test

        # -----------------------------------------
        # SCREENSHOT
        # -----------------------------------------

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_name = (
                f"{item.name}_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )

            screenshot_path = os.path.join(
                "screenshots",
                screenshot_name
            )

            driver.save_screenshot(screenshot_path)

            logger.error(
                f"Screenshot captured: {screenshot_path}"
            )

            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG
            )

        # -----------------------------------------
        # LOG FILE ATTACHMENT TO ALLURE REPORT
        # -----------------------------------------

        log_file = "logs/test.log"

        if os.path.exists(log_file):   #checks if log file exists before attaching to report

            allure.attach.file(
                log_file,
                name="Execution Logs",
                attachment_type=AttachmentType.TEXT
            )