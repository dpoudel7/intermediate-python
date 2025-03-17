#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ITERATORS EXERCISE

In this exercise, you'll work with iterators to solve common Salesforce
development scenarios. You'll implement custom iterators, use itertools,
and create data processing pipelines.

The exercise has several parts:
1. Implement a custom iterator for processing Salesforce opportunities
2. Create a date-based iterator for sales reporting
3. Build a data processing pipeline using itertools
4. Create a paginated data iterator

This exercise builds on the concepts covered in the theory and tutorial sections.
"""

from typing import List, Dict, Any, Iterator, Iterable
from datetime import datetime, timedelta
import itertools
import json

# -----------------------------------------------------------------------------
# EXERCISE 1: OPPORTUNITY PIPELINE ITERATOR
# -----------------------------------------------------------------------------

class OpportunityPipelineIterator:
    """Iterator for processing opportunities by stage."""
    
    def __init__(self, opportunities: List[Dict[str, Any]], batch_size: int = 2):
        self.opportunities = sorted(opportunities, key=lambda x: x['Stage'])
        self.batch_size = batch_size
        self.index = 0
    
    # TODO: Implement the iterator protocol methods (__iter__ and __next__)
    # The iterator should:
    # 1. Group opportunities by stage
    # 2. Return batches of opportunities from the same stage
    # 3. Include stage summary (total value, count) with each batch
    
    # Hint: Use itertools.groupby to group by stage

# Sample opportunity data
opportunities = [
    {
        'Id': 'OPP001',
        'Name': 'New Software License',
        'Stage': 'Prospecting',
        'Amount': 50000,
        'CloseDate': '2023-06-30'
    },
    {
        'Id': 'OPP002',
        'Name': 'Service Contract',
        'Stage': 'Negotiation',
        'Amount': 75000,
        'CloseDate': '2023-07-15'
    },
    {
        'Id': 'OPP003',
        'Name': 'Hardware Upgrade',
        'Stage': 'Prospecting',
        'Amount': 25000,
        'CloseDate': '2023-06-15'
    },
    {
        'Id': 'OPP004',
        'Name': 'Consulting Project',
        'Stage': 'Closed Won',
        'Amount': 100000,
        'CloseDate': '2023-05-30'
    },
    {
        'Id': 'OPP005',
        'Name': 'Training Package',
        'Stage': 'Negotiation',
        'Amount': 30000,
        'CloseDate': '2023-07-30'
    }
]

def process_opportunity_pipeline():
    """Process opportunities using the custom iterator."""
    # TODO: Create and use the OpportunityPipelineIterator
    # Print summary for each batch of opportunities
    pass

# -----------------------------------------------------------------------------
# EXERCISE 2: SALES FORECAST ITERATOR
# -----------------------------------------------------------------------------

class SalesForecastIterator:
    """Iterator that generates sales forecasts for future months."""
    
    def __init__(self, start_date: datetime, months: int, growth_rate: float = 0.05):
        self.current_date = start_date
        self.months_remaining = months
        self.growth_rate = growth_rate
        self.base_revenue = 100000  # Starting monthly revenue
    
    # TODO: Implement the iterator protocol methods (__iter__ and __next__)
    # The iterator should:
    # 1. Generate monthly forecasts for the specified number of months
    # 2. Apply the growth rate to each month's forecast
    # 3. Return a dict with month, forecast amount, and growth details

# -----------------------------------------------------------------------------
# EXERCISE 3: ACCOUNT DATA PIPELINE
# -----------------------------------------------------------------------------

def filter_active_accounts(accounts: Iterable[Dict]) -> Iterator[Dict]:
    """Filter for active accounts."""
    # TODO: Implement filter for active accounts (Status == 'Active')
    pass

def filter_high_value(accounts: Iterable[Dict]) -> Iterator[Dict]:
    """Filter for high-value accounts (revenue > $1M)."""
    # TODO: Implement filter for high-value accounts
    pass

def enrich_account_data(accounts: Iterable[Dict]) -> Iterator[Dict]:
    """Add computed fields to account data."""
    # TODO: Add fields like:
    # - customer_tier (based on revenue)
    # - days_since_last_activity
    # - potential_upsell (boolean)
    pass

# Sample account data
accounts = [
    {
        'Id': 'ACC001',
        'Name': 'Global Tech',
        'Status': 'Active',
        'AnnualRevenue': 2000000,
        'LastActivityDate': '2023-05-15'
    },
    {
        'Id': 'ACC002',
        'Name': 'Local Shop',
        'Status': 'Inactive',
        'AnnualRevenue': 500000,
        'LastActivityDate': '2023-01-10'
    },
    {
        'Id': 'ACC003',
        'Name': 'Mega Corp',
        'Status': 'Active',
        'AnnualRevenue': 5000000,
        'LastActivityDate': '2023-05-20'
    },
    {
        'Id': 'ACC004',
        'Name': 'Startup Inc',
        'Status': 'Active',
        'AnnualRevenue': 1000000,
        'LastActivityDate': '2023-04-01'
    }
]

def process_account_pipeline():
    """Process accounts through the data pipeline."""
    # TODO: Create and use the account processing pipeline
    # Combine the filter and enrichment functions
    # Print detailed information about each processed account
    pass

# -----------------------------------------------------------------------------
# EXERCISE 4: PAGINATED QUERY ITERATOR
# -----------------------------------------------------------------------------

class QueryPaginatorIterator:
    """Iterator for handling paginated query results."""
    
    def __init__(self, query: str, page_size: int = 2):
        self.query = query
        self.page_size = page_size
        self.current_page = 1
        self.has_more = True
        
        # Simulate database records
        self._load_data()
    
    def _load_data(self):
        """Simulate loading data from database."""
        self.data = [
            {'Id': f'REC{i}', 'Name': f'Record {i}', 'Value': i * 1000}
            for i in range(1, 8)
        ]
    
    # TODO: Implement the iterator protocol methods (__iter__ and __next__)
    # The iterator should:
    # 1. Return paginated results with metadata
    # 2. Handle the last page correctly
    # 3. Include total record count and page information

def process_paginated_query():
    """Process records using the paginated query iterator."""
    # TODO: Create and use the QueryPaginatorIterator
    # Handle pagination metadata
    # Aggregate results across pages
    pass

if __name__ == "__main__":
    print("=" * 50)
    print("EXERCISE 1: OPPORTUNITY PIPELINE")
    print("=" * 50)
    process_opportunity_pipeline()
    
    print("\n" + "=" * 50)
    print("EXERCISE 2: SALES FORECAST")
    print("=" * 50)
    forecast_iterator = SalesForecastIterator(datetime.now(), 6)
    # TODO: Use the forecast iterator
    
    print("\n" + "=" * 50)
    print("EXERCISE 3: ACCOUNT PIPELINE")
    print("=" * 50)
    process_account_pipeline()
    
    print("\n" + "=" * 50)
    print("EXERCISE 4: PAGINATED QUERY")
    print("=" * 50)
    process_paginated_query() 