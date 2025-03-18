#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCISE 1: IMPROVING BASIC LOGGING - SOLUTION

This is the solution to the basic logging exercise. It demonstrates how to:
1. Replace print statements with appropriate logging calls
2. Add proper log formatting with timestamps
3. Implement file logging
4. Use appropriate log levels
5. Add error handling with logging
"""

import logging
import time
import random
from datetime import datetime
from typing import List, Dict

# Sample data - simulating Salesforce records
SAMPLE_ACCOUNTS = [
    {
        'id': 'SF_001',
        'name': 'Acme Corporation',
        'industry': 'Manufacturing',
        'last_modified': '2023-01-15T10:30:00Z'
    },
    {
        'id': 'SF_002',
        'name': 'TechCorp',
        'industry': 'Technology',
        'last_modified': '2023-02-20T15:45:00Z'
    },
    {
        'id': 'SF_003',
        'name': 'Global Industries',
        'industry': 'Consulting',
        'last_modified': '2023-03-10T08:15:00Z'
    }
]

def setup_logging():
    """Setup logging configuration."""
    # Create logger
    logger = logging.getLogger('salesforce.sync')
    logger.setLevel(logging.DEBUG)
    
    # Create handlers
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    file_handler = logging.FileHandler('sync.log')
    file_handler.setLevel(logging.DEBUG)
    
    # Create formatters and add it to handlers
    console_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)
    
    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def fetch_salesforce_accounts(logger: logging.Logger) -> List[Dict]:
    """Simulate fetching accounts from Salesforce."""
    logger.info("Fetching Salesforce accounts")
    logger.debug(f"Fetch started at: {datetime.now()}")
    
    # Simulate API delay
    time.sleep(1)
    
    if random.random() < 0.2:  # 20% chance of failure
        logger.error(
            "Failed to connect to Salesforce API",
            exc_info=True
        )
        return []
    
    logger.info(f"Successfully fetched {len(SAMPLE_ACCOUNTS)} accounts")
    logger.debug(f"Accounts: {SAMPLE_ACCOUNTS}")
    return SAMPLE_ACCOUNTS

def process_account(account: Dict, logger: logging.Logger) -> bool:
    """Process a single account (simulate database update)."""
    logger.debug(f"Processing account: {account}")
    
    try:
        # Simulate processing
        time.sleep(0.5)
        
        if random.random() < 0.1:  # 10% chance of failure
            raise Exception(f"Failed to process account {account['id']}")
        
        logger.info(f"Successfully processed account: {account['name']}")
        return True
        
    except Exception as e:
        logger.error(
            f"Error processing account {account['id']}: {str(e)}",
            exc_info=True,
            extra={'account_id': account['id']}
        )
        return False

def sync_accounts(logger: logging.Logger):
    """Main function to sync accounts."""
    logger.info("Starting account synchronization")
    start_time = time.time()
    
    # Fetch accounts
    accounts = fetch_salesforce_accounts(logger)
    if not accounts:
        logger.warning("No accounts to process")
        return
    
    # Process accounts
    successful = 0
    failed = 0
    
    for account in accounts:
        if process_account(account, logger):
            successful += 1
        else:
            failed += 1
            logger.warning(
                f"Failed to process account {account['id']}",
                extra={'account_id': account['id']}
            )
    
    # Log summary
    duration = time.time() - start_time
    logger.info(
        "Sync completed! Duration: %.2f seconds",
        duration
    )
    logger.info(
        f"Results: {successful} successful, {failed} failed"
    )
    
    # Log warning if there were failures
    if failed > 0:
        logger.warning(
            f"{failed} accounts failed to process",
            extra={'failed_count': failed}
        )

def main():
    """Main entry point."""
    # Setup logging
    logger = setup_logging()
    
    try:
        sync_accounts(logger)
    except Exception as e:
        logger.critical(
            "Critical error during sync process",
            exc_info=True
        )

if __name__ == "__main__":
    main() 