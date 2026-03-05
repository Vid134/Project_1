### Import Python's built-in logging module to generate logs
import logging

## Import os module to work with file system paths and directories
import os


###Function to create and return a logger object
###logger_name allows different files/classes to have their own logger
def get_logger(logger_name):

    ## Create or fetch a logger instance with the given name
    logger = logging.getLogger(logger_name)

    ##Set the logging level to INFO
    ## This means INFO, WARNING, ERROR, and CRITICAL logs will be captured
    logger.setLevel(logging.INFO)

    ###Construct the logs directory path
    # os.path.dirname(__file__) gives the current file's directory
    # os.path.dirname(os.path.dirname(__file__)) moves one level up
    if not logger.handlers:
      log_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "logs"
    )

    # Check whether the logs directory already exists
    if not os.path.exists(log_dir):
        # Create the logs directory if it does not exist
        os.makedirs(log_dir)

    # Create the full path for the log file inside the logs directory
    log_file = os.path.join(log_dir, "automation.log")

    # Create a FileHandler to write logs into the automation.log file
    file_handler = logging.FileHandler(log_file)

    # Define the format in which each log message should be written
    # asctime   -> timestamp
    # levelname -> INFO / ERROR / etc.
    # name      -> logger name
    # message   -> actual log message
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Attach the formatter to the file handler
    file_handler.setFormatter(formatter)

    ##Check if handlers are already attached to the logger
    ##This prevents duplicate log entries
    if not logger.handlers:
        ##Attach the file handler to the logger
        logger.addHandler(file_handler)

    ##Return the configured logger object
    return logger