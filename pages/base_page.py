from selenium.webdriver.support.ui import WebDriverWait  ##Importing webdriver wait to apply explicit waits in selenium
from selenium.webdriver.support import expected_conditions as EC   ##Importing selenium  expected conditions as EC for readability
import logging   # Import logging module

class BasePage:
    """
    Basepage acts as the parent class for all page classes,it contains common wait and action methods reused across
    pages i.e homepage,dashboard page,login page and register page
    """

#Constructor method -- runs automatically when a page object is created
    def __init__(self, driver):
    ##Stores the webdriver instance so child pages can use it
        self.driver = driver

        ##Creates a reusable explicit wait with a timeout of 10secs
        self.wait = WebDriverWait(driver, 10)

    # ===================== LOGGER SETUP =====================

        self.logger = logging.getLogger(self.__class__.__name__)
    #  Creates a logger named after the page class (HomePage, RegisterPage, etc.)

        if not self.logger.handlers:
        #  Prevents duplicate log lines when tests run multiple times

         self.logger.setLevel(logging.INFO)
        #  Sets logging level (INFO is enough for automation projects)

        console_handler = logging.StreamHandler()
        #  Sends logs to terminal / PyCharm run console

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        #  Log format: time | page name | log level | message

        console_handler.setFormatter(formatter)
        #  Apply format to console output

        self.logger.addHandler(console_handler)
        #  Attach console handler to logger

    # ========================================================


    def wait_for_presence(self, locator):
        """
        Wait until the element is present in the DOM.
        Presence means element exists but may not be visible yet.
        Used when visibility is not mandatory
        """
        self.logger.info(f"Waiting for presence of element: {locator}")  #  LOG
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )          ###The return statement sends back the web element once selenium confirms it exists in the DOM


##Wait until an element is visible on the ui
    def wait_for_visibility(self, locator):
    ##Explicitly wait until the element is both present and visible to the user on the screen
        self.logger.info(f"Waiting for visibility of element: {locator}")  # LOG
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )      ##Returning the web element after it becomes visible

##Wait until an element is clickable(visible+enabled)
    def wait_for_clickable(self, locator):
    ##Explicitly wait until the element is visible and enabled, so can be clicked safely

        self.logger.info(f"Waiting for element to be clickable: {locator}")  #  LOG
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )   ##Returning the webelemnet once it is ready for clicking

##Generic click method to click any element safely
    def click(self, locator):
     ##Wait until the element is clickable
        self.logger.info(f"Clicking element: {locator}")  #  LOG
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()   ##perform the click action on the element

 ##Generic click method to enter text into input fields
    def enter_text(self, locator, text):
     ##Wait until the input field is visible
        self.logger.info(f"Entering text into element: {locator}")  #  LOG
        element = self.wait_for_visibility(locator)
    ##Clear any existing text inside the input
        element.clear()
    ##Type the given text into the input field
        element.send_keys(text)

 ##Generic method to fetch visible text from any element
    def get_text(self, locator):
    ##Wait until the element becomes visible
        self.logger.info(f"Fetching text from element: {locator}")  #  LOG
        element = self.wait_for_visibility(locator)
    ##Return the text content of the element
        return element.text






