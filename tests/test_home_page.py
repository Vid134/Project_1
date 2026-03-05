import logging
from pages.home_page import HomePage    ##Import the homepage class so we can call homepage actions and validations

# Create a logger for this test file
logger = logging.getLogger(__name__)


### TEST CASE 1: Validate that the homepage URL is correct.
def test_home_page_url(driver):
    ## Define test function to validate that the homepage url is valid

    # LOG: Test started
    logger.info("TEST STARTED: Validate homepage URL")

    #Store the expected URL of the application homepage
    expected_url = "https://www.guvi.in/"
    logger.info(f"Expected URL: {expected_url}")   ##LOG
    logger.info(f"Actual URL: {driver.current_url}")    ##LOG

    ##Compare the current browser URl with the expected URL
    assert driver.current_url == expected_url

    # LOG: Test passed
    logger.info("TEST PASSED: Homepage URL is correct")



### TEST CASE 2: Validate that the homepage title is correct
def test_home_page_title(driver):
    ## Define test function to validate that the homepage title is valid

    logger.info("TEST STARTED: Validate homepage title")  ##LOG

    # Store the expected title of the application homepage
    expected_title = "HCL GUVI | Learn to code in your native language"
    logger.info(f"Expected title: {expected_title}")  ##LOG
    logger.info(f"Actual title: {driver.title}")    ##LOG

    assert driver.title == expected_title

    logger.info("TEST PASSED: Homepage title is correct")    ##LOG



### TEST CASE 3: Verify login button is visible and clickable
def test_login_button_visibility_and_clickability(driver):
    ## Define test function for login button visibility and clickability

    logger.info("TEST STARTED: Login button visibility & clickability")  ##LOG

    # Create an object of Homepage using the current driver
    home_page = HomePage(driver)

    logger.info("Checking if Login button is visible")   ##LOG

    # Verify that the login button is visible on the homepage
    assert home_page.is_login_button_visible()

    logger.info("Clicking Login button")   ##LOG

  #Click on the login button
    home_page.click_login()

    logger.info("Verifying Login page is opened")   ##LOG

    # Verify that upon clicking login,opens the login page
    assert home_page.is_login_page_opened() is True

    logger.info("TEST PASSED: Login button works correctly")  ##LOG



### TEST CASE 4: Verify Signup button is visible and clickable
def test_signup_button_visibility_and_clickability(driver):
    ## Define test function for signup button visibility and clickability

    logger.info("TEST STARTED: Signup button visibility & clickability")  ##LOG

    # Create an object of Homepage using current driver
    home_page = HomePage(driver)

    logger.info("Checking if Signup button is visible")  ##LOG

   # Verify that the Signup button is visible on the homepage
    assert home_page.is_signup_button_visible()

    logger.info("Clicking Signup button")   ##LOG
    # Click on the signup button

    home_page.click_signup()

    logger.info("Verifying Signup page is opened")  ##LOG

    # Verify that upon clicking signup,opens the signup page
    assert home_page.is_signup_page_opened()

    logger.info("TEST PASSED: Signup button works correctly")  ##LOG



### TEST CASE 9: Verify that menu items like “Courses”, “LIVE Classes”, and “Practice” are displayed.
def test_menu_items_visible(driver):
    ## Define test function for menu items visibility

    logger.info("TEST STARTED: Menu items visibility")   ##LOG

    # Create an object of Homepage using current driver
    home_page = HomePage(driver)

    logger.info("Checking Courses, LIVE Classes, Practice menus")  ##LOG

    ## Verify that all the menu items are visible
    assert home_page.are_menu_items_visible()

    logger.info("TEST PASSED: Menu items are visible")  ##LOG



### TEST CASE 10: Verify Dobby assistant icon is visible on the homepage
def test_dobby_assistant_visible(driver):
    ## Define test function for visibility of dobby assistant icon

    logger.info("TEST STARTED: Dobby assistant visibility")  ##LOG

    # Create an object of Homepage using current driver
    home_page = HomePage(driver)

    logger.info("Checking Dobby assistant icon")  ##LOG

    # Verify that the Dobby assistant is displayed on the page
    assert home_page.is_dobby_visible()

    logger.info("TEST PASSED: Dobby assistant icon is visible")  ##LOG


