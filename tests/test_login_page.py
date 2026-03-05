import logging  ## Import logging module to generate logs for test execution
from pages.home_page import HomePage ##Import the homepage class so we can call homepage actions and validations
from pages.login_page import LoginPage  ##Import the Login page class so we can call Login page actions and validations
from pages.dashboard_page import DashboardPage  ##Import the Dashboard page class so we can call dashboard page actions and validations
from utils.data_reader import get_test_data  ##importing the data from test data file using the utils
import pytest  ## Importing pytest module

## Create logger instance for this test file
logger = logging.getLogger(__name__)

### TEST CASE 6: Verify Login works with valid credentials
def test_login_with_valid_credentials(driver):
    ## Define test function for login functionality with valid credentials

    ## To get the data from the test data file
    data = get_test_data("valid_login")

    logger.info("TEST CASE STARTED: Verify login with valid credentials")  ##LOG


    ##Create homepage object using webdriver instance
    logger.info("Creating HomePage object")

  ##Create homepage object using webdriver instance
    home_page = HomePage(driver)

    ##Click on the login button from the homepage
    logger.info("Clicking login button on homepage")  ##LOG

  ##Click on the login button from the homepage
    home_page.click_login()


    logger.info("Creating LoginPage object")  ##LOG

## Create Login page object to interact with login form
    login_page = LoginPage(driver)

    ##Enter valid email and password then submit login form
    logger.info("Entering valid login credentials")  ##LOG

  ##Enter valid email and password then submit login form from test data file
    login_page.login(data["email"],data["password"])

    ## Create Dashboard page object after successful login
    logger.info("Creating DashboardPage object after successful login") ##LOG

 ## Create Dashboard page object after successful login
    dashboard_page = DashboardPage(driver)

    logger.info("Verifying that dashboard page is loaded")  ##LOG

  ## Assert that dashboard is loaded ,confirming succesful login
    assert dashboard_page.is_dashboard_loaded() is True

    logger.info("TEST PASSED: Login with valid credentials successful")  ##LOG

##Parametrization for two invalid data sets
@pytest.mark.parametrize("data_key", ["invalid_login_1","invalid_login_2"])
### TEST CASE 7: Verify Login does not work with invalid credentials and shows up error message
def test_login_with_invalid_credentials(driver,data_key):
    ## Define test function for login functionality with invalid credentials

    ## To get the data from the test data file
    data = get_test_data(data_key)
    logger.info("TEST CASE STARTED: Verify login with invalid credentials")  ##LOG

    ##Create homepage object using webdriver instance
    logger.info("Creating HomePage object")  ##LOG

    ##Create homepage object using webdriver instance
    home_page = HomePage(driver)

    ##Click on the login button from the homepage
    logger.info("Clicking login button on homepage")   ##LOG

    ##Click on the login button from the homepage
    home_page.click_login()

    ## Create Login page object to interact with login form
    logger.info("Creating LoginPage object")  ##LOG

    ## Create Login page object to interact with login form
    login_page = LoginPage(driver)

    ##Enter invalid email and password then submit login form
    logger.info("Entering invalid login credentials")  ##LOG

    ##Enter invalid email and password taken from test data file then submit login form

    login_page.login(data["email"], data["password"])

    ## capture the error message displayed for invalid login
    logger.info("Fetching error message displayed for invalid login")  ##LOG

    ## capture the error message displayed for invalid login
    error_message = login_page.get_error_message()

    ## Assert that an error message is displayed on the screen
    logger.info("Verifying error message is displayed for invalid login")  ##LOG

    ## Assert that an error message is displayed on the screen
    assert error_message is not None

    logger.info("TEST PASSED: Error message displayed for invalid login")  ##LOG



#####-----------ADDITIONAL TESTCASE-------------------EDGE CASE----------------
#### TEST CASE 8: Verify login fails when username/email field is empty
def test_login_with_empty_email(driver):
    ## To get the data from the test data file
    data = get_test_data("invalid_login_empty_field")

    ## LOG: Starting the empty email login validation test
    logger.info("TEST CASE STARTED: Verify login with empty email")

    logger.info("Creating HomePage object")  ## LOG

    ## Create homepage object using webdriver instance
    home_page = HomePage(driver)

    logger.info("Clicking login button from homepage")  ## LOG

    ## Click login button on homepage to navigate to login page
    home_page.click_login()

    logger.info("Creating LoginPage object")  ## LOG

    ## Create LoginPage object to interact with login form elements
    login_page = LoginPage(driver)

    ## Attempt login with empty email but valid password
    logger.info("Attempting login with EMPTY email and valid password")  ## LOG

    ##Entering the empty email and password from test data
    login_page.login(data["email"], data["password"])

    logger.info("Verifying login failed because email field was empty")  ## LOG

    logger.info("Login button is still visible thereby confirming Login is unsuccessful due to empty username field")  ## LOG

    assert login_page.is_login_button_visible()
     ## ## Assert that an login button is visible

    ## LOG: Test completed successfully
    logger.info("TEST PASSED: Application correctly handled empty email login attempt")


