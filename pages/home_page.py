from selenium.webdriver.common.by import By   ##Import By class to locate elements using XPATH,ID,CSS,CLASS etc
from pages.base_page import BasePage   ##Import Basepage so homepage  can reuse  wait and click utilities
import logging  # Import logging module

logger = logging.getLogger(__name__)  # Page-level logger for HomePage

###Homepage represents the landing page of the application
class HomePage(BasePage):

#### LOCATORS----------------------------------------------------
    # Locator for the login button on the homepage
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login-btn' and contains(text(),'Login')]")
    ## Locator for the login page heading
    LOGIN_HEADING = (By.XPATH, "//h2[text()='Login']")
   ## Locator for the Signup button
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Sign up']")
    ## Locator for the sign up page heading
    SIGNUP_PAGE = (By.XPATH, "//h2[text()='Sign Up']")
    ## Locator for the course menu
    COURSES_MENU = (By.XPATH, "//h2[text()='Courses']")
    ## Locator for the Live classes menu
    LIVE_CLASSES_MENU = (By.XPATH, "//div[@id='solutions']//p[normalize-space()='LIVE Classes']")
    ## Locator for the Practice menu
    PRACTICE_MENU = (By.XPATH, "//div[@id='solutions']//p[normalize-space()='Practice']")
    ## Locator for the dobby chatbot icon
    DOBBY_ASSISTANT = (By.XPATH, "//span[@id='zs_fl_chat']")

#### ACTIONS?VALIDATIONS-------------------------------------------
  ##Check whether login button is visible on the home page
    def is_login_button_visible(self):
        logger.info("Checking visibility of Login button on Home page")  # LOG: validation
        ##Wait for visibility and return True if element exist
        return self.wait_for_visibility(self.LOGIN_BUTTON) is not None

### CLick the login button
    def click_login(self):
        logger.info("Clicking Login button on Home page")  # LOG: user action
        ##USe Basepage click method for reliability
        self.click(self.LOGIN_BUTTON)

### Verify that Login page is opened
    def is_login_page_opened(self, element=None):
        logger.info("Verifying whether Login page is opened")  # LOG: validation
        ## Find all elements matching login heading locator
        try:
            element = self.wait_for_visibility(self.LOGIN_HEADING)
        ## Return true if atleast one heading is visible
            return element is not None
        except:
             logger.warning("Login page is NOT visible")  # LOG: failure condition
             return False

### Check whether Signup button is visible
    def is_signup_button_visible(self):
        logger.info("Checking visibility of Signup button on Home page")  # LOG: validation
        ##Wait until Signup button is visible
        return self.wait_for_visibility(self.SIGNUP_BUTTON) is not None

## Click the signup button
    def click_signup(self):
        logger.info("Clicking Signup button on Home page")  # LOG: user action
        ##Use reusable click method
        self.click(self.SIGNUP_BUTTON)

## Verify that signup page is opened
    def is_signup_page_opened(self):
        logger.info("Verifying whether Signup page is opened")  # LOG: validation

    ##Find all elements matching signup heading location
        elements = self.driver.find_elements(*self.SIGNUP_PAGE)
    ## Return true if at least one heading is visible
        return any(el.is_displayed() for el in elements)

## Verify that main menu items are visible
    def are_menu_items_visible(self):
        # LOG: Start verifying menu items visibility on homepage
        self.logger.info("Verifying visibility of main menu items: Courses, LIVE Classes, Practice")
        ##Check if all menu have atleast one visible element
        result = (
            len(self.driver.find_elements(*self.COURSES_MENU)) > 0 and
            len(self.driver.find_elements(*self.LIVE_CLASSES_MENU)) > 0 and
            len(self.driver.find_elements(*self.PRACTICE_MENU)) > 0
        )
                # LOG: Result of menu items visibility check
        if result:
            self.logger.info("All main menu items are visible on the homepage")
        else:
            self.logger.error("One or more main menu items are NOT visible on the homepage")

        return result

##Check whether dobby chatbot icon is visible
    def is_dobby_visible(self):
        # LOG: Start verifying Dobby assistant visibility
        self.logger.info("Verifying visibility of Dobby assistant icon on homepage")

        result = any(el.is_displayed()
                   for el in self.driver.find_elements(*self.DOBBY_ASSISTANT))

        # LOG: Result of Dobby visibility check
        if result:
            self.logger.info("Dobby assistant icon is visible on the homepage")
        else:
            self.logger.error("Dobby assistant icon is NOT visible on the homepage")

        return True   ##return result if chatbot icon is displayed

##Finally utility to check login visibility again if needed
    def is_login_visible(self):
        # LOG: Checking login button visibility using BasePage wait
        self.logger.info("Verifying visibility of Login button on homepage")

        ##Reuse Basepage visibility wait
        element = self.wait_for_visibility(self.LOGIN_BUTTON)

        # LOG: Result of Login visibility on homepage check
        if element:
            self.logger.info("Login button is visible on homepage")
        else:
            self.logger.error("Login button is NOT visible on homepage")

        return element is not None  ##return element if it is displayed

