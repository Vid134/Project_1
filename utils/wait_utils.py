from selenium.webdriver.support.ui import WebDriverWait  ##Importing webdriver wait to apply explicit waits in selenium
from selenium.webdriver.support import expected_conditions as EC  ##Importing selenium  expected conditions as EC for readability

## Define a utility  class that contains reusable wait methods
class WaitUtils:
## This class helps avoid repeating wait logic across page objects

## Constructor method that initialises the wait utility
## Oy receives the webdriver instance and an optional timeout value
    def __init__(self, driver, timeout=10):
        ## create  a webdriver object using the driver and timeout
        ## This wait object will be reused in all wait methods
        self.wait = WebDriverWait(driver, timeout)

## method to wait until the element is visible on ui
## Visibility means the element is present and displayed on the screen
    def wait_for_visibility(self, locator):
        ## wait until the element located by the given locator becomes visible
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

## method to wait until the element becomes clickable
## Clickable means the element is visible and enabled for interaction
    def wait_for_clickable(self, locator):
        ## wait until the element located by the given locator becomes clickable
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

## Method to wait until the element to be present in the DOM
## Presence does not guarantee visibility on the ui
    def wait_for_presence(self, locator):
        ## Wait until the element is present in the DOM structure
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

