import logging
import os
from datetime import datetime


def setup_multiple_handlers():
    """Configure logging with multiple handlers for different purposes."""
    # Create logger
    logger = logging.getLogger('salesforce.sync')
    logger.setLevel(logging.DEBUG)
    
    # Create formatters
    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - '
        '%(pathname)s:%(lineno)d - %(message)s'
    )
    
    # Console handler (INFO and above)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # File handler (DEBUG and above)
    file_handler = logging.FileHandler('debug.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    
    # Error file handler (ERROR and above)
    error_handler = logging.FileHandler('error.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(detailed_formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    
    # Example usage
    logger.debug("Debug message - check detailed log file")
    logger.info("Info message - visible in console and log file")
    logger.warning("Warning message - visible in console and log file")
    logger.error("Error message - visible everywhere including error log")
    
    return logger


logger = setup_multiple_handlers()
logger.info("This is an info message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
logger.error("This is an error message")

