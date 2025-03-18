import logging
import logging.handlers

def setup_rotating_logs():
    """Configure logging with rotating file handlers."""
    logger = logging.getLogger('salesforce.sync')
    logger.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Size-based rotation (1MB per file, keep 5 backup files)
    size_handler = logging.handlers.RotatingFileHandler(
        'sync_size.log',
        maxBytes=1024*1024,  # 1MB
        backupCount=5
    )
    size_handler.setLevel(logging.DEBUG)
    size_handler.setFormatter(formatter)
    
    # Time-based rotation (rotate at midnight, keep 7 days)
    time_handler = logging.handlers.TimedRotatingFileHandler(
        'sync_time.log',
        when='midnight',
        interval=1,
        backupCount=7
    )
    time_handler.setLevel(logging.INFO)
    time_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(size_handler)
    logger.addHandler(time_handler)
    
    # Example usage - simulate lots of logs
    for i in range(100):
        logger.debug(f"Debug message {i}")
        logger.info(f"Info message {i}")
        if i % 10 == 0:
            logger.warning(f"Warning message {i}")
        if i % 20 == 0:
            logger.error(f"Error message {i}")
    
    return logger


logger = setup_rotating_logs()
logger.info("This is an info message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
logger.error("This is an error message")


