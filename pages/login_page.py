from selenium.webdriver.common.by import By   ##Import By class to locate elements using XPATH,ID,CSS,CLASS etc
from pages.base_page import BasePage   ##Import Basepage so Login page  can reuse  wait and click utilities

##Login page represents the login screen of the application
##it inherits Basepage to use shared selenium utilities
class LoginPage(BasePage):

#### LOCATORS----------------------------------------------------
    # Locator for the email input field using its html id attribute
    EMAIL_FIELD = (By.ID, "email")
# Locator for the password input field using its html id attribute
    PASSWORD_FIELD = (By.ID, "password")
# Locator for the login button using its html id attribute
    LOGIN_BUTTON = (By.ID, "login-btn")
# Locator for the error message shown when login fails basically due to invalid credentials
    ERROR_MESSAGE = (By.CLASS_NAME, "invalid-feedback")


#### ACTIONS / VALIDATIONS -----------------------------------------------
##Method to enter email into the email input field
    def enter_email(self, email):

        ## LOG: recording that email input action is starting
        self.logger.info("Entering email into login email field")

        ##Use basepage utility to wait for visibility and type the email value
        self.enter_text(self.EMAIL_FIELD, email)

##Method to enter password into the password input field
    def enter_password(self, password):

        ## LOG: recording that password input action is starting
        self.logger.info("Entering password into login password field")

        ##Use basepage utility to wait for visibility and type the password value
        self.enter_text(self.PASSWORD_FIELD, password)

##Method to click the login button
    def click_login(self):
        ## LOG: recording login button click action
        self.logger.info("Clicking login button")

        ##Use Basepage click method which waits until the button is clickable
        self.click(self.LOGIN_BUTTON)

##Combined method to perform complete login action
    def login(self, email, password):
        ## LOG: starting complete login workflow
        self.logger.info("Starting login process with provided credentials")

        ##Enter email value into the email field
        self.enter_email(email)

        ##Enter password value into the password field
        self.enter_password(password)

        ##Click the login button to submit the login form
        self.click_login()

         ## LOG: login form submission completed
        self.logger.info("Login form submitted")

##Method to fetch the error message displayed after a failed login attempt
    def get_error_message(self):
        ## LOG: checking for invalid login error message
        self.logger.info("Fetching login error message for invalid login attempt")

        ##Wait until the error message becomes visible and return its text content
        return self.wait_for_visibility(self.ERROR_MESSAGE).text

### Method to check the visibility of login button
    def is_login_button_visible(self):
        ## Wait until the Login button is visible
        return self.wait_for_visibility(self.LOGIN_BUTTON)
