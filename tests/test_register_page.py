from pages.home_page import HomePage  #Import the homepage class so we can call homepage actions and validations
from pages.register_page import RegisterPage   #Import the Register page class so we can call Register page actions and validations
import logging  # Import logging module

## Create logger instance for this test file
logger = logging.getLogger(__name__)

### TEST CASE 5: Validate navigation to register (Signup) page
def test_navigation_to_register_page(driver):
    ## Define test function to verify navigation from homepage to register page

    # LOG: Test execution started
    logger.info("TEST STARTED: Navigation to Register page")

    ##Create homepage object using webdriver instance
    home_page = HomePage(driver)

    # LOG: Clicking signup button from homepage
    logger.info("Clicking Signup button from Home page")

    home_page.click_signup()
    ##Click on the signup button from the homepage


## Create Register page object after navigation to register page
    register_page = RegisterPage(driver)

    # LOG: Verifying register page visibility
    logger.info("Verifying Register page visibility")

    ## Assert that the register page is succesfully loaded and visible
    assert register_page.is_register_page_loaded()

    # LOG: Test execution completed successfully
    logger.info("TEST PASSED: Navigation to Register page")

