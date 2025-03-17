#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GENERATORS EXERCISE

In this exercise, you'll work with generators to solve common Salesforce
development scenarios. You'll implement generator functions, use generator
expressions, and create data processing pipelines.

The exercise has several parts:
1. Create a generator for processing Salesforce query results
2. Implement a test data generator with specific patterns
3. Build a hierarchical data processor using yield from
4. Create a change data capture simulator

This exercise builds on the concepts covered in the theory and tutorial sections.
"""

from typing import List, Dict, Any, Generator, Union
from datetime import datetime, timedelta
import json
import random

# -----------------------------------------------------------------------------
# EXERCISE 1: SALESFORCE QUERY RESULT GENERATOR
# -----------------------------------------------------------------------------

def process_query_results(results: List[Dict], batch_size: int = 2) -> Generator[List[Dict], None, None]:
    """
    Generator that processes Salesforce query results in batches.
    
    TODO:
    1. Implement a generator that yields batches of records
    2. Each batch should be of size batch_size (except possibly the last batch)
    3. Calculate and include batch statistics (total amount, count) with each batch
    """
    pass

# Sample query results
query_results = [
    {
        'Id': 'OPP001',
        'Name': 'New Software License',
        'Amount': 50000,
        'StageName': 'Prospecting',
        'CloseDate': '2023-06-30'
    },
    {
        'Id': 'OPP002',
        'Name': 'Service Contract',
        'Amount': 75000,
        'StageName': 'Negotiation',
        'CloseDate': '2023-07-15'
    },
    {
        'Id': 'OPP003',
        'Name': 'Hardware Upgrade',
        'Amount': 25000,
        'StageName': 'Prospecting',
        'CloseDate': '2023-06-15'
    },
    {
        'Id': 'OPP004',
        'Name': 'Consulting Project',
        'Amount': 100000,
        'StageName': 'Closed Won',
        'CloseDate': '2023-05-30'
    },
    {
        'Id': 'OPP005',
        'Name': 'Training Package',
        'Amount': 30000,
        'StageName': 'Negotiation',
        'CloseDate': '2023-07-30'
    }
]

def exercise_1_query_results():
    """Process query results using the generator."""
    # TODO: Use the process_query_results generator to:
    # 1. Process results in batches
    # 2. Print batch statistics
    # 3. Calculate and print overall statistics
    pass

# -----------------------------------------------------------------------------
# EXERCISE 2: TEST DATA GENERATOR
# -----------------------------------------------------------------------------

def generate_opportunity_data(
    num_records: int,
    start_date: datetime,
    growth_rate: float = 0.1
) -> Generator[Dict, None, None]:
    """
    Generator that creates test opportunity data with specific patterns.
    
    TODO:
    1. Generate opportunities with increasing amounts (apply growth_rate)
    2. Assign stages based on close date (earlier = later stage)
    3. Include probability based on stage
    4. Add realistic names and descriptions
    """
    pass

def exercise_2_test_data():
    """Generate and analyze test opportunity data."""
    # TODO: Use the generate_opportunity_data generator to:
    # 1. Create test opportunities
    # 2. Analyze stage distribution
    # 3. Calculate average amount by stage
    # 4. Print summary statistics
    pass

# -----------------------------------------------------------------------------
# EXERCISE 3: HIERARCHICAL DATA PROCESSOR
# -----------------------------------------------------------------------------

def process_territory_hierarchy(
    territory: Dict,
    include_inactive: bool = False
) -> Generator[Dict, None, None]:
    """
    Generator that processes a territory hierarchy with accounts.
    
    TODO:
    1. Implement a recursive generator using yield from
    2. Process territory data before child territories
    3. Optionally filter inactive accounts
    4. Calculate and include territory metrics
    """
    pass

# Sample territory hierarchy
territory_hierarchy = {
    'Id': 'TER001',
    'Name': 'North America',
    'Level': 1,
    'Accounts': [
        {
            'Id': 'ACC001',
            'Name': 'Global Corp',
            'Active': True,
            'Revenue': 5000000
        },
        {
            'Id': 'ACC002',
            'Name': 'Local Shop',
            'Active': False,
            'Revenue': 100000
        }
    ],
    'ChildTerritories': [
        {
            'Id': 'TER002',
            'Name': 'West Coast',
            'Level': 2,
            'Accounts': [
                {
                    'Id': 'ACC003',
                    'Name': 'Tech Giant',
                    'Active': True,
                    'Revenue': 3000000
                }
            ],
            'ChildTerritories': []
        },
        {
            'Id': 'TER003',
            'Name': 'East Coast',
            'Level': 2,
            'Accounts': [
                {
                    'Id': 'ACC004',
                    'Name': 'Big Bank',
                    'Active': True,
                    'Revenue': 4000000
                },
                {
                    'Id': 'ACC005',
                    'Name': 'Old Factory',
                    'Active': False,
                    'Revenue': 500000
                }
            ],
            'ChildTerritories': []
        }
    ]
}

def exercise_3_territory_hierarchy():
    """Process territory hierarchy using the generator."""
    # TODO: Use the process_territory_hierarchy generator to:
    # 1. Process all territories and accounts
    # 2. Calculate revenue by territory
    # 3. Show active vs inactive accounts
    # 4. Print hierarchical summary
    pass

# -----------------------------------------------------------------------------
# EXERCISE 4: CHANGE DATA CAPTURE SIMULATOR
# -----------------------------------------------------------------------------

def simulate_change_stream(
    duration_seconds: int,
    error_probability: float = 0.1
) -> Generator[Dict, None, Union[Dict, Exception]]:
    """
    Generator that simulates a Change Data Capture stream with error handling.
    
    TODO:
    1. Generate realistic change events
    2. Simulate occasional errors
    3. Include different change types
    4. Add metadata about changes
    """
    pass

def exercise_4_change_stream():
    """Process simulated change data capture stream."""
    # TODO: Use the simulate_change_stream generator to:
    # 1. Process changes for specified duration
    # 2. Handle errors appropriately
    # 3. Calculate change statistics
    # 4. Show error recovery behavior
    pass

if __name__ == "__main__":
    print("=" * 50)
    print("EXERCISE 1: QUERY RESULT PROCESSING")
    print("=" * 50)
    exercise_1_query_results()
    
    print("\n" + "=" * 50)
    print("EXERCISE 2: TEST DATA GENERATION")
    print("=" * 50)
    exercise_2_test_data()
    
    print("\n" + "=" * 50)
    print("EXERCISE 3: TERRITORY HIERARCHY")
    print("=" * 50)
    exercise_3_territory_hierarchy()
    
    print("\n" + "=" * 50)
    print("EXERCISE 4: CHANGE DATA CAPTURE")
    print("=" * 50)
    exercise_4_change_stream() 