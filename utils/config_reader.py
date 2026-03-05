import configparser  # Import configparser module to read values from a .ini configuration file
import os  # Import os module to work with file paths in an OS-independent way

# Define a ConfigReader class to centralize all configuration access
# This avoids hard-coding values like URL, waits, browser, etc.
class ConfigReader:

    # Constructor method that runs automatically when the class is instantiated
    def __init__(self):
        # Create a ConfigParser object to read key-value pairs from config.ini
        self.config = configparser.ConfigParser()

        # Build the absolute path to config.ini file
        # os.path.dirname(__file__) gives the directory of this file
        # os.path.dirname(os.path.dirname(__file__)) moves one level up
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config.ini"
        )

        # Read the configuration values from the config.ini file
        self.config.read(config_path)

    # Method to get the base URL of the application
    def get_base_url(self):
        # Return the base_url value from the DEFAULT section of config.ini
        return self.config["DEFAULT"]["base_url"]

    # Method to get the browser name (chrome, firefox, etc.)
    def get_browser(self):
        # Return the browser value from the DEFAULT section
        return self.config["DEFAULT"]["browser"]

    # Method to get the implicit wait time
    def get_implicit_wait(self):
        # Read implicit_wait value, convert it to integer, and return it
        return int(self.config["DEFAULT"]["implicit_wait"])

    # Method to get the explicit wait time
    def get_explicit_wait(self):
        # Read explicit_wait value, convert it to integer, and return it
        return int(self.config["DEFAULT"]["explicit_wait"])

