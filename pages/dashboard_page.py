from selenium.webdriver.common.by import By  ## Import the By class to locate elements using Xpath,Id,CSS etc
from selenium.webdriver.support.wait import WebDriverWait  ##Importing webdriver wait to apply explicit waits in selenium
from pages.base_page import BasePage  ##Import the Basepage so this page can  reuse common wait and action methods
from selenium.webdriver.support import expected_conditions as EC  ##Import elenium expected conditions i.e visibility,clickability

##Dashboard page represents all actions and elements available on the dashboard screen
class DashboardPage(BasePage):

#######Locators---------------------
    # Locator for the profile icon(user avatar) in the top right corner
    PROFILE_ICON = (By.XPATH, "//img[@alt='Profile']/ancestor::div[contains(@class,'account-box-toggler')]")
    ## Locator for the dropdown container that opens after clicking the profile icon
    PROFILE_DROPDOWN = (By.XPATH, "//div[contains(@class,'account-box-toggler')]")
    ##Locator for the sign out button inside the opened profile dropdown
    SIGNOUT_BUTTON = (By.XPATH, "//ul[@id='account-boxheader']//div[contains(@class,'cursor-pointer')][last()]")

######## Validation methods------------
    # Actions / UI validations
## This method checks whether the dashboard page has loaded successfully
    def is_dashboard_loaded(self):

        self.logger.info("Checking whether Dashboard page is loaded")  ##LOG
    ##Wait until the profile icon becomes visible on the page,visibility of this icon means the dashboard is fully loaded
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.PROFILE_ICON)

        )
        self.logger.info("Dashboard page loaded successfully")  ##LOG
    ## If the wait passes without timeout, return true
        return True

######## Action methods----------------
    def open_Profile_icon(self):
        ##this method clicks the profile icon to open the account dropdown
        self.logger.info("Attempting to click Profile icon")  ##LOG
        ##Wait until the profile icon becomes clickable
        profile = self.wait.until(
            EC.element_to_be_clickable(self.PROFILE_ICON)
        )
        ## Click the profile icon
        profile.click()
        ##Wait until the dropdown becomes visible after clicking,this ensures the menu doesnot auto close immediately
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='Profile']/ancestor::div[contains(@class,'account-box-toggler')]")
            )
        )
        self.logger.info("Profile dropdown is visible")   ##LOG

## This method clicks the Signout option to log the user out
    def click_logout(self):

       self.logger.info("Attempting to click Logout button")  ##LOG

    ##Execute Javascript click because  normal selenium click fails due to overlays or react re rendering
       self.driver.execute_script("""
       document
       .querySelector("ul#account-boxheader div.cursor-pointer:last-child")
       .click();
       """)

       print("logout click executed")
    ##Print statement used only for debugging confirmation

       self.logger.info("Logout click executed successfully")   ##LOG
