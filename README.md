Project Title:
Automation Testing of EdTech platform web application

Project Description :
 This project automates the testing of the GUVI web application using Selenium WebDriver with Python and PyTest.

The automation framework follows the Page Object Model (POM) design pattern to improve maintainability and scalability of test scripts.

The project validates core functionalities of the GUVI website such as login, signup, navigation, chatbot presence,menu items presence and logout functionality.

Preconditions:
This explains what conditions must exist before tests run.
Example:
Preconditions
• Python must be installed
• Chrome browser must be installed
• Internet connection required
• Required Python packages installed
• GUVI website should be accessible


Test Environment:
Operating System : Windows 11
Browser          : Google Chrome
Automation Tool  : Selenium WebDriver
Programming Lang : Python
Test Framework   : PyTest
IDE              : PyCharm


Technologies Used:
Tool                    	Purpose
Python               	Programming language
Selenium	            Browser automation
PyTest	                Test execution framework
POM	                    Framework design pattern
WebDriver Manager	    Browser driver management

TABLE OF CONTENT:
1.Project structure
2.Detailed Project Architecture
3.Project feature 
4.Project Usage
5.UI under test
6.Test design techniques
7.Test cases covered in project
8.Advantages of this framework
9.CI/CD integration
10.Future Enhancements

Project Structure:
GUVI_Automation_Project
│
├── pages
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── register_page.py
│   └── dashboard_page.py
│
├── tests
│   ├── test_login.py
│   ├── test_register.py
│   ├── test_navigation.py
│   └── test_dashboard.py
│
├── utilities
│   ├── config_reader.py
│   ├── logger.py
│   └── wait_utils.py
│
├── config
│   └── config.ini
|
│---allure.results
|
├── reports
│
├── logs
│
├── conftest.py
│
├── requirements.txt
│
└── README.md

pages/ → contains page object classes

tests/ → contains PyTest test cases

utilities/ → reusable modules (waits, logging, config)

config/ → configuration file

reports/ → test execution reports

logs/ → framework logs
Detailed explanation is given under Architecture.

-----------------------------------

Detailed Project Architecture:
GUVI Web Automation Framework
The automation framework is designed using the Page Object Model (POM) architecture with Selenium + Python + PyTest.

Architecture goal:
1.Maintainable code
2.Reusable components
3.Separation of responsibilities
4.Scalable automation framework

High Level Architecture Flow:
Before going into folders, understand the execution flow.

Test Case (PyTest)
        ↓
Page Object Method
        ↓
Base Page Reusable Methods
        ↓
Wait Utilities / Logger / Config
        ↓
Selenium WebDriver
        ↓
Browser

Automation Framework Architecture Diagram:
                 ┌─────────────────────────────┐
                 │        Test Layer           │
                 │  (PyTest Test Cases)       │
                 │                             │
                 │  test_login.py              │
                 │  test_register.py           │
                 │  test_navigation.py         │
                 │  test_dashboard.py          │
                 └──────────────┬──────────────┘
                                │
                                ▼
                 ┌─────────────────────────────┐
                 │      Page Object Layer      │
                 │        (POM Design)         │
                 │                             │
                 │  home_page.py               │
                 │  login_page.py              │
                 │  register_page.py           │
                 │  dashboard_page.py          │
                 └──────────────┬──────────────┘
                                │
                                ▼
                 ┌─────────────────────────────┐
                 │        Base Layer           │
                 │        (BasePage)           │
                 │                             │
                 │  common Selenium methods    │
                 │  click_element()            │
                 │  enter_text()               │
                 │  get_text()                 │
                 │  is_visible()               │
                 └──────────────┬──────────────┘
                                │
                                ▼
                 ┌─────────────────────────────┐
                 │        Utility Layer        │
                 │                             │
                 │  wait_utils.py              │
                 │  logger.py                  │
                 │  config_reader.py           │
                 └──────────────┬──────────────┘
                                │
                                ▼
                 ┌─────────────────────────────┐
                 │     Selenium WebDriver      │
                 │                             │
                 │ ChromeDriver / FirefoxDriver│
                 └──────────────┬──────────────┘
                                │
                                ▼
                 ┌─────────────────────────────┐
                 │           Browser           │
                 │                             │
                 │        Chrome / Edge        │
                 └─────────────────────────────┘

Framework Architecture:
The automation framework follows a layered architecture based on the Page Object Model (POM) design pattern.
The framework consists of the following layers:

1. Test Layer
Contains PyTest test cases that execute automation scenarios and perform assertions.

2. Page Object Layer
Represents UI pages of the application. Each page contains locators and methods to interact with elements.

3. Base Layer
Provides reusable Selenium actions such as clicking elements and entering text.

4. Utility Layer
Contains reusable modules such as WaitUtils, Logger, and ConfigReader.

5. Selenium WebDriver Layer
Handles communication between automation scripts and the browser.

6. Browser Layer
The actual browser where test execution takes place.

Explanation of Each Architecture Layer:
1️⃣ Test Layer (Top Layer)
This layer contains the actual automation test cases.
test_login.py
test_register.py
test_navigation.py
test_dashboard.py

Responsibilities:
This layer:
1.Executes test scenarios
2.Calls page object methods
3.Performs assertions

Example test flow:

def test_valid_login(driver):

    login = LoginPage(driver)

    login.login("testuser","password123")

    assert "Dashboard" in driver.title

Important rule:
1Test layer should not contain Selenium locators.
2.It should only:
call page methods
verify results

2️⃣ Page Object Layer
This layer represents UI pages of the application.
home_page.py
login_page.py
register_page.py
dashboard_page.py

Each page object contains:
1. Locators

username_field
password_field
login_button

2. Page Methods

enter_username()
enter_password()
click_login()
login()

Example method:

def login(self, username, password):

    self.enter_username(username)

    self.enter_password(password)

    self.click_login()

Purpose:
Encapsulates UI interactions.


3️⃣ Base Layer (BasePage)
This layer contains common reusable Selenium operations.
base_page.py

Example methods:

click_element()
enter_text()
get_text()
is_visible()

Example:

def click_element(self, locator):

    element = self.wait.wait_for_clickable(locator)

    element.click()

Purpose:
Avoid repeating Selenium code in every page.
Instead of writing this everywhere:
driver.find_element(By.ID,"login").click()

we write:
self.click_element(login_button)

4️⃣ Utility Layer
Utility modules provide support functions used by the framework.

utilities/
Contains:
wait_utils.py
logger.py
config_reader.py
Wait Utilities

Handles explicit waits.

wait_for_visibility()
wait_for_clickable()
wait_for_presence()

Purpose:
Ensures element is ready before interacting.

Logger
Handles logging of test execution.

Example logs:

INFO : Browser launched
INFO : Login button clicked
INFO : User logged in successfully
ERROR : Login failed

Logs help debugging failed tests.

Config Reader
Reads data from config.ini.

Example config:
base_url = https://www.guvi.in
browser = chrome
timeout = 10

Instead of hardcoding values, the framework reads them from config.


5️⃣ Selenium WebDriver Layer:
This layer connects the automation framework with the browser.
ChromeDriver
FirefoxDriver
EdgeDriver

WebDriver:
sends commands to browser
executes UI actions

Example:
click()
send_keys()
navigate()


6️⃣ Browser Layer (Bottom Layer):
The browser is where actual UI execution happens.
Chrome
Firefox
Edge

All commands finally execute here.
Example:
open URL
click login button
enter username
submit form

---------------------------------------------

Project Features:
Automation Framework Features

1️⃣ Page Object Model (POM) design
Separates test logic and page locators
Makes scripts easier to maintain

2️⃣ Explicit Wait Implementation
Using reusable WaitUtils:
wait_for_visibility()
wait_for_clickable()
wait_for_presence()

Benefits:
avoids flaky tests
handles dynamic elements

3️⃣ Logging System

Custom logger captures:
test execution steps like test started to test finished
failures
debug information

4️⃣ Configuration Driven
Using config.ini

Example:

[DEFAULT]
base_url = https://www.guvi.in
browser = chrome
timeout = 10

Benefits:
avoids hardcoding values
easy environment change

5️⃣ Modular Framework
Components separated into:

Pages
Tests
Utilities
Config

-----------

Project Usage:
Step 1 — Install Dependencies
pip install -r requirements.txt

Step 2 — Open Project in PyCharm
Open the project folder.

Step 3 — Configure Browser
Update config.ini

Step 4 — Run Test Suite
Run using PyTest:
pytest -v

or run individual test file
pytest tests/test_login.py

Step 5 — View Results
Execution results available in:

reports/ -- report.html + allure results/visual report
logs/  --- Can be seen as 'automation log'

-------------------------------------

UI Under Test:
The automation project tests core UI components of the GUVI website.
Main UI Pages Tested

1️⃣ Home Page
2️⃣ Login Page
3️⃣ Register Page
4️⃣ Dashboard Page

1.UI Elements Tested
2.UI Component	Validation
3.URL	Correct website loading
4.Title	Page title validation
5.Login Button	Visibility and functionality
6.Signup Button	Navigation validation
7.Menu Items	Proper navigation
8.Chatbot	Presence verification
9.Logout	Successful logout
10.Example UI Validation

-----------------------------------------------
Test Design Techniques Used:

This project uses **Black Box Testing techniques**.

1️⃣ Positive Testing
Testing valid inputs.

Example:
Valid username
Valid password
Expected: Login successful

2️⃣ Negative Testing
Testing invalid inputs.

Example:

Invalid username
Invalid password
Expected: Error message displayed

3️⃣ UI Validation Testing
Verify UI components.

Example:

Verify login button visible
Verify page title
Verify chatbot exists

4️⃣ Navigation Testing
Verify correct page navigation.

Example:

Home → Login
Home → Signup
Dashboard → Logout

5️⃣ Functional Testing
Verify system behaves as expected.

Example:

Login functionality
Logout functionality
Menu navigation

5️⃣ Boundary Value Testing
Checking empty field

example:
 
Empty username field
Giving password
Expected -Login fails

-------------------------------------------

Test Cases Covered in Project:

 manual + automation tests include:

Test Case	Description
TC01	Validate website URL
TC02	Validate page title
TC03	Verify login button presence
TC04	Verify signup button navigation
TC05	Verify menu navigation
TC06	Verify valid login
TC07	Verify invalid login
TC08	Verify invalid login(2)
TC09	Verify invalid login with empty field
TC10    Menu items visible
TC11	Chatbot visible
TC12   Verify logout functionality

------------------------------------

 Advantages of This Framework:
1.Reusable automation code
2.Maintainable project structure
3.Easy debugging using logs
4.Reliable automation with explicit waits
5.Scalable framework for future test cases

-------------
CI/CD Integration:
The automation framework supports CI integration to enable automated test execution.
The framework can be integrated with CI/CD tools such as:
GitHub Actions

Simple Workflow of CI:
Push code to GitHub
      ↓
GitHub Actions starts
      ↓
Python installed
      ↓
Dependencies installed
      ↓
pytest executed
      ↓
Test report generated

---------------------------------------

Future Enhancements:
• Integrate CI/CD pipeline using Jenkins
• Add cross-browser testing
• Implement parallel test execution
• Integrate with Docker for containerized testing

Test Report link - 