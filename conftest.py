import pytest   ## Import pytest framework to use fixtures and test features
from selenium import webdriver  ## Import selenium webdriver module to control the browser
from selenium.webdriver.chrome.service import Service ##Import Chrome service class to manage chrome driver service
from selenium.webdriver.chrome.options import Options  ##Import chrome options class to customize browser behaviour
from utils.config_reader import ConfigReader ## Import config reader class to read values like URl and wait time from config file
import logging
import os                        # Import os module to handle file paths and folders
from datetime import datetime    # Import datetime to generate unique timestamps for screenshots

#### ---------------- LOGGER CONFIGURATION ----------------
# This config runs ONCE before any test starts
# It captures logs for all test case executions

logging.basicConfig(
    filename="automation.log",                     # Log file name
    level=logging.INFO,                            # Capture INFO, WARNING, ERROR
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

## Declare this function as a pytest fixture so it can be reused across test files
@pytest.fixture
def driver():

    logging.info("========== TEST STARTED ==========")
    # Log when a test starts
    ## Create an object of Config Reader to access configuration values
    config = ConfigReader()

## Create chrome options object to set browser options
    chrome_options = Options()

## Add argument to start the chrome browser in maximized mode
    chrome_options.add_argument("--start-maximized")
## Create a service object to manage chrome driver execution
    service = Service()
    ##Create a chrome webdriver instance with service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)
## Set implicit wait using value read from configuration file
    driver.implicitly_wait(config.get_implicit_wait())
    ## Navigate to the base URL read from configuration file
    driver.get(config.get_base_url())

## Yield the driver instance to the test case
    ##test execution happens at this point
    yield driver
## Quit the browser after the test execution is completed
    driver.quit()

    logging.info("========== TEST FINISHED ==========")
    # Log when a test finishes


### we are using this because if the test fails then the screenshot is captured inorder to figure out
@pytest.hookimpl(hookwrapper=True)
# This decorator tells pytest that this function is a hook implementation.
# hookwrapper=True allows us to run code before and after the test execution.

def pytest_runtest_makereport(item):
    # This is a pytest hook that runs after every test phase (setup, call, teardown).
    # We use it to check whether the test has passed or failed.

    outcome = yield
    # yield allows pytest to run the actual test first before we process the result.

    report = outcome.get_result()
    # get_result() fetches the test execution result (pass or fail information).

    if report.when == "call" and report.failed:
        # "call" means the actual test execution phase.
        # report.failed checks whether the test has failed.

        driver = item.funcargs.get("driver", None)
        # Retrieve the Selenium WebDriver instance from the test fixture.
        # If the driver fixture exists, we store it in 'driver'.

        if driver:
            # Ensure the WebDriver exists before capturing screenshot.

            screenshots_dir = "Screenshots"
            # Define the folder name where screenshots will be stored.

            os.makedirs(screenshots_dir, exist_ok=True)
            # Create the Screenshots folder if it does not already exist.
            # exist_ok=True prevents errors if the folder already exists.

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Generate a timestamp so each screenshot file name is unique.

            screenshot_name = f"{item.name}_{timestamp}.png"
            # Create the screenshot file name using the test name and timestamp.

            screenshot_path = os.path.join(screenshots_dir, screenshot_name)
            # Combine the folder path and file name to create the full screenshot path.

            driver.save_screenshot(screenshot_path)
            # Use Selenium WebDriver to capture the screenshot and save it to the folder.

