from selenium.webdriver.common.by import By    ##Import By class to locate elements using XPATH,ID,CSS,CLASS etc
from pages.base_page import BasePage  ##Import the Basepage so this page can  reuse common wait and action methods

## Register page represents the Signup/Register page of the application
## It inherits Basepage to avoid rewriting common selenium logic
class RegisterPage(BasePage):

### LOCATORS -----------------------------------------
##Locator for the Signup page header text using XPATH,This helps confirm that the register page has loaded succesfully
    REGISTER_HEADER = (By.XPATH, "//h2[contains(text(),'Sign Up')]")

 #### UI VALIDATION -----------------------------
##Method to verify whether the Register page is loaded or not
    def is_register_page_loaded(self):
        # LOG: Start checking whether register page is loaded
        self.logger.info("Checking whether Register page is loaded")

        ## wait until the register header becomes visible on the screen
        is_displayed = self.wait_for_visibility(self.REGISTER_HEADER).is_displayed()

        if is_displayed:
            # LOG: Register page loaded successfully
            self.logger.info("Register page loaded successfully")
        else:
            # LOG: Register page not loaded
            self.logger.error("Register page NOT loaded")

        return is_displayed
     ## Wait for the register page header to appear and verify it is displayed
