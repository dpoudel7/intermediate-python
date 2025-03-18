#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCISE 1: IMPROVING BASIC LOGGING

In this exercise, you'll improve the logging in a Salesforce data
synchronization script. The current code uses print statements and
has poor error handling. Your task is to implement proper logging.

Tasks:
1. Replace print statements with appropriate logging calls
2. Add proper log formatting with timestamps
3. Implement file logging
4. Use appropriate log levels
5. Add error handling with logging

The code below synchronizes Salesforce accounts with a local database.
It currently uses print statements for output. Your task is to improve it
by implementing proper logging.
"""

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

def fetch_salesforce_accounts() -> List[Dict]:
    """Simulate fetching accounts from Salesforce."""
    print(f"Fetching Salesforce accounts at {datetime.now()}")
    
    # Simulate API delay
    time.sleep(1)
    
    if random.random() < 0.2:  # 20% chance of failure
        print("Error: Failed to connect to Salesforce API")
        return []
    
    print(f"Successfully fetched {len(SAMPLE_ACCOUNTS)} accounts")
    return SAMPLE_ACCOUNTS

def process_account(account: Dict) -> bool:
    """Process a single account (simulate database update)."""
    try:
        # Simulate processing
        time.sleep(0.5)
        
        if random.random() < 0.1:  # 10% chance of failure
            raise Exception(f"Failed to process account {account['id']}")
        
        print(f"Processed account: {account['name']}")
        return True
        
    except Exception as e:
        print(f"Error processing account: {str(e)}")
        return False

def sync_accounts():
    """Main function to sync accounts."""
    print("\nStarting account synchronization...")
    print(f"Start time: {datetime.now()}")
    
    # Fetch accounts
    accounts = fetch_salesforce_accounts()
    if not accounts:
        print("No accounts to process")
        return
    
    # Process accounts
    successful = 0
    failed = 0
    
    for account in accounts:
        if process_account(account):
            successful += 1
        else:
            failed += 1
            print(f"Warning: Failed to process account {account['id']}")
    
    # Print summary
    print("\nSync completed!")
    print(f"End time: {datetime.now()}")
    print(f"Results: {successful} successful, {failed} failed")

def main():
    """Main entry point."""
    # TODO: Setup logging configuration here
    
    try:
        sync_accounts()
    except Exception as e:
        print(f"Critical error during sync: {str(e)}")

if __name__ == "__main__":
    main() 