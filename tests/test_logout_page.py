import time  ## Import time module to use explicit sleep
from pages.home_page import HomePage  ##Import the homepage class so we can call homepage actions and validations
from pages.login_page import LoginPage   ##Import the Login page class so we can call Login page actions and validations
from pages.dashboard_page import DashboardPage   ##Import the Dashboard page class so we can call dashboard page actions and validations
import logging  ## Import logging module to generate logs

## Create logger object for this test file
logger = logging.getLogger(__name__)

#### TEST CASE 11: Verify logout functionality after successful login
def test_logout_functionality(driver):
    ##Define test function for logout functionality

    logger.info("TEST STARTED: Logout functionality test")  ##LOG

    ##Create homepage object using webdriver instance
    home_page = HomePage(driver)

    logger.info("Clicking login button on homepage")  ##LOG

    ##Click on the login button from the homepage
    home_page.click_login()

    logger.info("Entering valid login credentials")  ##LOG

    ## Create Login page object to interact with login form
    login_page = LoginPage(driver)

    ##Enter valid email and password then submit login form
    login_page.login("vidhya.venkruk@gmail.com", "Ganesha@2021")

    logger.info("Login submitted, navigating to dashboard")   ##LOG

## Create Dashboard page object after successful login
    dashboard_page = DashboardPage(driver)

    logger.info("Verifying that Dashboard is loaded succesfull")   ##LOG

    ## Assert that dashboard is loaded ,confirming successful login
    assert dashboard_page.is_dashboard_loaded()

    logger.info("Dashboard loaded succesfully")  ##LOG

    logger.info("Opening profile dropdown menu")  ##LOG

## Click on the profile icon to open the account dropdown menu
    dashboard_page.open_Profile_icon()

    logger.info("Waiting for dropdown menu to appear")  ##LOG

    ##pause execution for 5seconds ,here i have used it to observe UI behaviour
    time.sleep(5)

    logger.info("Clicking logout option")  ##LOG

    ## Click the logout option from the dropdown menu
    dashboard_page.click_logout()

    logger.info("Verifying user is logged out")  ##LOG

  ## Assert that login button is visible again confirming successful logout
    assert home_page.is_login_visible()

    logger.info("Test Passed: Logout functionality working correctly")  ##LOG
