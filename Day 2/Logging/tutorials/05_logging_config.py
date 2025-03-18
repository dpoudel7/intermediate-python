import logging
import logging.config
import logging.handlers
import json
import os
from datetime import datetime
from typing import Dict, Any


def setup_basic_dict_config():
    """Configure logging using dictionary configuration."""
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - '
                         '%(pathname)s:%(lineno)d - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'detailed',
                'filename': 'salesforce_sync.log',
                'mode': 'a'
            }
        },
        'loggers': {
            'salesforce': {
                'level': 'DEBUG',
                'handlers': ['console', 'file'],
                'propagate': False
            }
        }
    }
    
    # Apply the configuration
    logging.config.dictConfig(config)
    
    # Get a logger
    logger = logging.getLogger('salesforce')
    
    # Example usage
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    return logger


logger = setup_basic_dict_config()
logger.info("This is an info message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
logger.error("This is an error message")

