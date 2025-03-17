#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ITERATORS EXERCISE - SOLUTION

This file contains solutions to the iterator exercises, demonstrating
proper implementation of iterator protocols and patterns in Python.
"""

from typing import List, Dict, Any, Iterator, Iterable
from datetime import datetime, timedelta
import itertools
import json

# -----------------------------------------------------------------------------
# EXERCISE 1: OPPORTUNITY PIPELINE ITERATOR - SOLUTION
# -----------------------------------------------------------------------------

class OpportunityPipelineIterator:
    """Iterator for processing opportunities by stage."""
    
    def __init__(self, opportunities: List[Dict[str, Any]], batch_size: int = 2):
        self.opportunities = sorted(opportunities, key=lambda x: x['Stage'])
        self.batch_size = batch_size
        self.stage_groups = None
        self.current_stage = None
        self.current_batch = []
        self.stage_opportunities = None
    
    def __iter__(self):
        """Initialize the iterator."""
        # Group opportunities by stage
        self.stage_groups = itertools.groupby(
            self.opportunities,
            key=lambda x: x['Stage']
        )
        return self
    
    def __next__(self):
        """Return next batch of opportunities with stage summary."""
        # If we have opportunities in the current batch, return them
        if self.current_batch:
            batch = self.current_batch[:self.batch_size]
            self.current_batch = self.current_batch[self.batch_size:]
            
            # Calculate stage summary
            stage_total = sum(opp['Amount'] for opp in batch)
            
            return {
                'stage': self.current_stage,
                'opportunities': batch,
                'batch_total': stage_total,
                'batch_count': len(batch)
            }
        
        # Try to get the next stage group
        try:
            if self.stage_groups is None:
                raise StopIteration
            
            # Get next stage and its opportunities
            self.current_stage, opportunities = next(self.stage_groups)
            self.current_batch = list(opportunities)
            
            # Recursively call next() to handle this new batch
            return self.__next__()
            
        except StopIteration:
            raise StopIteration

def process_opportunity_pipeline():
    """Process opportunities using the custom iterator."""
    pipeline = OpportunityPipelineIterator(opportunities)
    
    total_value = 0
    total_count = 0
    
    print("Processing opportunity pipeline:")
    for batch in pipeline:
        stage = batch['stage']
        opps = batch['opportunities']
        batch_total = batch['batch_total']
        batch_count = batch['batch_count']
        
        print(f"\nStage: {stage}")
        print(f"Batch Total: ${batch_total:,}")
        print(f"Opportunities in batch: {batch_count}")
        print("Opportunities:")
        for opp in opps:
            print(f"- {opp['Name']}: ${opp['Amount']:,}")
        
        total_value += batch_total
        total_count += batch_count
    
    print(f"\nPipeline Summary:")
    print(f"Total Value: ${total_value:,}")
    print(f"Total Opportunities: {total_count}")

# -----------------------------------------------------------------------------
# EXERCISE 2: SALES FORECAST ITERATOR - SOLUTION
# -----------------------------------------------------------------------------

class SalesForecastIterator:
    """Iterator that generates sales forecasts for future months."""
    
    def __init__(self, start_date: datetime, months: int, growth_rate: float = 0.05):
        self.current_date = start_date
        self.months_remaining = months
        self.growth_rate = growth_rate
        self.base_revenue = 100000  # Starting monthly revenue
        self.current_revenue = self.base_revenue
    
    def __iter__(self):
        """Return iterator object."""
        return self
    
    def __next__(self):
        """Generate next month's forecast."""
        if self.months_remaining <= 0:
            raise StopIteration
        
        # Calculate forecast for current month
        forecast = {
            'month': self.current_date.strftime('%Y-%m'),
            'forecast_amount': self.current_revenue,
            'growth_amount': self.current_revenue * self.growth_rate,
            'growth_rate': self.growth_rate * 100  # Convert to percentage
        }
        
        # Update state for next month
        self.current_revenue *= (1 + self.growth_rate)
        self.current_date += timedelta(days=32)  # Approximate month
        self.current_date = self.current_date.replace(day=1)  # Reset to first of month
        self.months_remaining -= 1
        
        return forecast

def process_sales_forecast(iterator: SalesForecastIterator):
    """Process and display sales forecast."""
    print("Monthly Sales Forecast:")
    print("Month      | Forecast Amount | Growth Amount | Growth Rate")
    print("-" * 60)
    
    total_forecast = 0
    for forecast in iterator:
        month = forecast['month']
        amount = forecast['forecast_amount']
        growth = forecast['growth_amount']
        rate = forecast['growth_rate']
        
        print(f"{month:10} | ${amount:13,.2f} | ${growth:11,.2f} | {rate:8.1f}%")
        total_forecast += amount
    
    print("-" * 60)
    print(f"Total Forecast: ${total_forecast:,.2f}")

# -----------------------------------------------------------------------------
# EXERCISE 3: ACCOUNT DATA PIPELINE - SOLUTION
# -----------------------------------------------------------------------------

def filter_active_accounts(accounts: Iterable[Dict]) -> Iterator[Dict]:
    """Filter for active accounts."""
    return filter(lambda x: x['Status'] == 'Active', accounts)

def filter_high_value(accounts: Iterable[Dict]) -> Iterator[Dict]:
    """Filter for high-value accounts (revenue > $1M)."""
    return filter(lambda x: x['AnnualRevenue'] > 1000000, accounts)

def enrich_account_data(accounts: Iterable[Dict]) -> Iterator[Dict]:
    """Add computed fields to account data."""
    def enrich_account(account: Dict) -> Dict:
        # Calculate customer tier
        revenue = account['AnnualRevenue']
        if revenue > 5000000:
            tier = 'Platinum'
        elif revenue > 2000000:
            tier = 'Gold'
        elif revenue > 1000000:
            tier = 'Silver'
        else:
            tier = 'Bronze'
        
        # Calculate days since last activity
        last_activity = datetime.strptime(
            account['LastActivityDate'],
            '%Y-%m-%d'
        )
        days_since = (datetime.now() - last_activity).days
        
        # Determine upsell potential
        potential_upsell = (
            days_since < 90 and  # Recent activity
            account['Status'] == 'Active' and  # Active account
            revenue < 5000000  # Room for growth
        )
        
        # Return enriched account data
        return {
            **account,
            'customer_tier': tier,
            'days_since_last_activity': days_since,
            'potential_upsell': potential_upsell
        }
    
    return map(enrich_account, accounts)

def process_account_pipeline():
    """Process accounts through the data pipeline."""
    # Create processing pipeline
    pipeline = enrich_account_data(
        filter_high_value(
            filter_active_accounts(accounts)
        )
    )
    
    # Process and display results
    print("High-Value Active Accounts:")
    print("Name         | Tier     | Revenue    | Last Activity | Upsell")
    print("-" * 70)
    
    for account in pipeline:
        name = account['Name'][:10].ljust(10)
        tier = account['customer_tier'].ljust(8)
        revenue = f"${account['AnnualRevenue']:,}"
        days = f"{account['days_since_last_activity']} days"
        upsell = "Yes" if account['potential_upsell'] else "No"
        
        print(f"{name} | {tier} | {revenue:10} | {days:12} | {upsell}")

# -----------------------------------------------------------------------------
# EXERCISE 4: PAGINATED QUERY ITERATOR - SOLUTION
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
        self.total_records = len(self.data)
        self.total_pages = (self.total_records + self.page_size - 1) // self.page_size
    
    def __iter__(self):
        """Return iterator object."""
        return self
    
    def __next__(self):
        """Return next page of results with metadata."""
        if not self.has_more:
            raise StopIteration
        
        # Calculate slice indices
        start_idx = (self.current_page - 1) * self.page_size
        end_idx = start_idx + self.page_size
        
        # Get records for current page
        page_records = self.data[start_idx:end_idx]
        
        # Update pagination state
        self.has_more = end_idx < self.total_records
        
        # Create response with metadata
        response = {
            'records': page_records,
            'page_number': self.current_page,
            'page_size': self.page_size,
            'total_pages': self.total_pages,
            'total_records': self.total_records,
            'has_next_page': self.has_more
        }
        
        self.current_page += 1
        return response

def process_paginated_query():
    """Process records using the paginated query iterator."""
    # Create paginator with sample query
    query = "SELECT Id, Name, Value FROM Records"
    paginator = QueryPaginatorIterator(query)
    
    total_value = 0
    all_records = []
    
    print(f"Executing query: {query}")
    
    # Process each page
    for page in paginator:
        records = page['records']
        page_num = page['page_number']
        total_pages = page['total_pages']
        
        print(f"\nPage {page_num} of {total_pages}")
        print(f"Records in page: {len(records)}")
        
        # Process records
        for record in records:
            print(f"- {record['Name']}: ${record['Value']:,}")
            total_value += record['Value']
            all_records.append(record)
        
        # Show pagination info
        print(f"Has more pages: {page['has_next_page']}")
    
    # Show summary
    print(f"\nQuery Summary:")
    print(f"Total Records: {len(all_records)}")
    print(f"Total Value: ${total_value:,}")
    print(f"Average Value: ${total_value/len(all_records):,.2f}")

if __name__ == "__main__":
    print("=" * 50)
    print("EXERCISE 1: OPPORTUNITY PIPELINE")
    print("=" * 50)
    process_opportunity_pipeline()
    
    print("\n" + "=" * 50)
    print("EXERCISE 2: SALES FORECAST")
    print("=" * 50)
    forecast_iterator = SalesForecastIterator(datetime.now(), 6)
    process_sales_forecast(forecast_iterator)
    
    print("\n" + "=" * 50)
    print("EXERCISE 3: ACCOUNT PIPELINE")
    print("=" * 50)
    process_account_pipeline()
    
    print("\n" + "=" * 50)
    print("EXERCISE 4: PAGINATED QUERY")
    print("=" * 50)
    process_paginated_query() 