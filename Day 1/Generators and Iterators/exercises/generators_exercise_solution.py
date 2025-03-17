#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GENERATORS EXERCISE - SOLUTION

This file contains solutions to the generators exercises, demonstrating
best practices and patterns for using generators in Salesforce development.
"""

from typing import List, Dict, Any, Generator, Union
from datetime import datetime, timedelta
import json
import random
import time

# -----------------------------------------------------------------------------
# EXERCISE 1: SALESFORCE QUERY RESULT GENERATOR - SOLUTION
# -----------------------------------------------------------------------------

def process_query_results(results: List[Dict], batch_size: int = 2) -> Generator[List[Dict], None, None]:
    """
    Generator that processes Salesforce query results in batches.
    
    Args:
        results: List of query result records
        batch_size: Number of records to process in each batch
        
    Yields:
        Dictionary containing:
        - records: List of records in the current batch
        - batch_stats: Statistics for the current batch
    """
    for i in range(0, len(results), batch_size):
        batch = results[i:i + batch_size]
        batch_stats = {
            'count': len(batch),
            'total_amount': sum(record['Amount'] for record in batch),
            'avg_amount': sum(record['Amount'] for record in batch) / len(batch),
            'stages': set(record['StageName'] for record in batch)
        }
        yield {
            'records': batch,
            'batch_stats': batch_stats
        }

def exercise_1_query_results():
    """Process query results using the generator."""
    print("Processing query results in batches...")
    
    total_amount = 0
    total_records = 0
    all_stages = set()
    
    for batch in process_query_results(query_results, batch_size=2):
        records = batch['records']
        stats = batch['batch_stats']
        
        print(f"\nProcessing batch of {stats['count']} records:")
        print(f"Batch total amount: ${stats['total_amount']:,.2f}")
        print(f"Batch average amount: ${stats['avg_amount']:,.2f}")
        print(f"Stages in batch: {', '.join(stats['stages'])}")
        
        total_amount += stats['total_amount']
        total_records += stats['count']
        all_stages.update(stats['stages'])
    
    print("\nOverall Statistics:")
    print(f"Total records processed: {total_records}")
    print(f"Total amount: ${total_amount:,.2f}")
    print(f"Average amount: ${total_amount/total_records:,.2f}")
    print(f"All stages encountered: {', '.join(sorted(all_stages))}")

# -----------------------------------------------------------------------------
# EXERCISE 2: TEST DATA GENERATOR - SOLUTION
# -----------------------------------------------------------------------------

def generate_opportunity_data(
    num_records: int,
    start_date: datetime,
    growth_rate: float = 0.1
) -> Generator[Dict, None, None]:
    """
    Generator that creates test opportunity data with specific patterns.
    
    Args:
        num_records: Number of records to generate
        start_date: Starting date for opportunities
        growth_rate: Rate of increase in opportunity amounts
        
    Yields:
        Dictionary containing opportunity data
    """
    stages = [
        ('Prospecting', 0.2),
        ('Qualification', 0.4),
        ('Proposal', 0.6),
        ('Negotiation', 0.8),
        ('Closed Won', 1.0)
    ]
    
    products = ['CRM License', 'Integration Package', 'Support Contract',
                'Training Services', 'Custom Development', 'Cloud Storage']
    
    base_amount = 10000
    for i in range(num_records):
        # Calculate amount with growth
        amount = base_amount * (1 + growth_rate) ** i
        
        # Determine close date
        close_date = start_date + timedelta(days=i * 15)
        
        # Select stage based on close date proximity
        days_until_close = (close_date - datetime.now()).days
        stage_index = min(4, max(0, int(days_until_close / 30)))
        stage, probability = stages[stage_index]
        
        # Generate opportunity name
        product = random.choice(products)
        account_number = random.randint(1000, 9999)
        name = f"{product} - Account {account_number}"
        
        yield {
            'Id': f'OPP{i+1:06d}',
            'Name': name,
            'Amount': round(amount, 2),
            'StageName': stage,
            'Probability': probability,
            'CloseDate': close_date.strftime('%Y-%m-%d'),
            'Description': f"Opportunity for {product} with projected revenue of ${amount:,.2f}",
            'CreatedDate': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

def exercise_2_test_data():
    """Generate and analyze test opportunity data."""
    print("Generating test opportunity data...")
    
    start_date = datetime.now()
    opportunities = list(generate_opportunity_data(10, start_date))
    
    # Analyze stage distribution
    stage_stats = {}
    for opp in opportunities:
        stage = opp['StageName']
        if stage not in stage_stats:
            stage_stats[stage] = {
                'count': 0,
                'total_amount': 0,
                'opportunities': []
            }
        stage_stats[stage]['count'] += 1
        stage_stats[stage]['total_amount'] += opp['Amount']
        stage_stats[stage]['opportunities'].append(opp)
    
    print("\nOpportunity Analysis by Stage:")
    for stage, stats in stage_stats.items():
        avg_amount = stats['total_amount'] / stats['count']
        print(f"\n{stage}:")
        print(f"Count: {stats['count']}")
        print(f"Total Amount: ${stats['total_amount']:,.2f}")
        print(f"Average Amount: ${avg_amount:,.2f}")
        
    total_amount = sum(opp['Amount'] for opp in opportunities)
    print(f"\nTotal Opportunities: {len(opportunities)}")
    print(f"Total Pipeline: ${total_amount:,.2f}")

# -----------------------------------------------------------------------------
# EXERCISE 3: HIERARCHICAL DATA PROCESSOR - SOLUTION
# -----------------------------------------------------------------------------

def process_territory_hierarchy(
    territory: Dict,
    include_inactive: bool = False
) -> Generator[Dict, None, None]:
    """
    Generator that processes a territory hierarchy with accounts.
    
    Args:
        territory: Territory hierarchy dictionary
        include_inactive: Whether to include inactive accounts
        
    Yields:
        Dictionary containing territory and account information
    """
    # Process current territory's accounts
    active_accounts = [
        acc for acc in territory['Accounts']
        if include_inactive or acc['Active']
    ]
    
    territory_metrics = {
        'total_revenue': sum(acc['Revenue'] for acc in active_accounts),
        'account_count': len(active_accounts),
        'active_account_count': sum(1 for acc in active_accounts if acc['Active'])
    }
    
    yield {
        'territory_id': territory['Id'],
        'territory_name': territory['Name'],
        'territory_level': territory['Level'],
        'accounts': active_accounts,
        'metrics': territory_metrics
    }
    
    # Process child territories using yield from
    for child in territory['ChildTerritories']:
        yield from process_territory_hierarchy(child, include_inactive)

def exercise_3_territory_hierarchy():
    """Process territory hierarchy using the generator."""
    print("Processing territory hierarchy...")
    
    total_revenue = 0
    total_accounts = 0
    territory_summary = {}
    
    for territory_data in process_territory_hierarchy(territory_hierarchy, include_inactive=True):
        territory_name = territory_data['territory_name']
        metrics = territory_data['metrics']
        
        print(f"\nTerritory: {territory_name} (Level {territory_data['territory_level']})")
        print(f"Active Accounts: {metrics['active_account_count']}")
        print(f"Total Accounts: {metrics['account_count']}")
        print(f"Territory Revenue: ${metrics['total_revenue']:,.2f}")
        
        total_revenue += metrics['total_revenue']
        total_accounts += metrics['account_count']
        territory_summary[territory_name] = metrics
    
    print("\nHierarchy Summary:")
    print(f"Total Territories: {len(territory_summary)}")
    print(f"Total Accounts: {total_accounts}")
    print(f"Total Revenue: ${total_revenue:,.2f}")

# -----------------------------------------------------------------------------
# EXERCISE 4: CHANGE DATA CAPTURE SIMULATOR - SOLUTION
# -----------------------------------------------------------------------------

def simulate_change_stream(
    duration_seconds: int,
    error_probability: float = 0.1
) -> Generator[Dict, None, Union[Dict, Exception]]:
    """
    Generator that simulates a Change Data Capture stream with error handling.
    
    Args:
        duration_seconds: How long to run the simulation
        error_probability: Probability of generating an error
        
    Yields:
        Dictionary containing change event data or raises an exception
    """
    start_time = time.time()
    sequence = 0
    
    change_types = ['CREATE', 'UPDATE', 'DELETE']
    objects = ['Account', 'Contact', 'Opportunity']
    
    while time.time() - start_time < duration_seconds:
        sequence += 1
        
        # Simulate random errors
        if random.random() < error_probability:
            error_types = [
                ValueError("Invalid field value"),
                ConnectionError("CDC connection lost"),
                TimeoutError("Event processing timeout")
            ]
            raise random.choice(error_types)
        
        # Generate change event
        change_type = random.choice(change_types)
        object_type = random.choice(objects)
        
        event = {
            'sequence': sequence,
            'timestamp': datetime.now().isoformat(),
            'type': change_type,
            'object': object_type,
            'record_id': f"{object_type[:3]}{sequence:06d}",
            'changes': {}
        }
        
        # Add type-specific changes
        if change_type in ('CREATE', 'UPDATE'):
            if object_type == 'Account':
                event['changes'] = {
                    'Name': f"Test Account {sequence}",
                    'Industry': random.choice(['Technology', 'Finance', 'Healthcare']),
                    'BillingCountry': random.choice(['USA', 'Canada', 'UK'])
                }
            elif object_type == 'Contact':
                event['changes'] = {
                    'FirstName': f"Test{sequence}",
                    'LastName': f"Contact{sequence}",
                    'Email': f"test{sequence}@example.com"
                }
            elif object_type == 'Opportunity':
                event['changes'] = {
                    'Name': f"Test Opportunity {sequence}",
                    'Amount': round(random.uniform(1000, 100000), 2),
                    'StageName': random.choice(['Prospecting', 'Closed Won'])
                }
        
        yield event
        time.sleep(0.5)  # Simulate processing time

def exercise_4_change_stream():
    """Process simulated change data capture stream."""
    print("Starting Change Data Capture simulation...")
    
    stats = {
        'total_events': 0,
        'errors': 0,
        'changes_by_type': {},
        'changes_by_object': {}
    }
    
    try:
        for event in simulate_change_stream(duration_seconds=5):
            stats['total_events'] += 1
            
            # Update type statistics
            change_type = event['type']
            stats['changes_by_type'][change_type] = stats['changes_by_type'].get(change_type, 0) + 1
            
            # Update object statistics
            object_type = event['object']
            stats['changes_by_object'][object_type] = stats['changes_by_object'].get(object_type, 0) + 1
            
            print(f"\nProcessing event {event['sequence']}:")
            print(f"Type: {event['type']}")
            print(f"Object: {event['object']}")
            print(f"Record ID: {event['record_id']}")
            if event['changes']:
                print("Changes:", json.dumps(event['changes'], indent=2))
            
    except Exception as e:
        stats['errors'] += 1
        print(f"\nError encountered: {str(e)}")
        print("Implementing error recovery...")
    
    print("\nSimulation Statistics:")
    print(f"Total Events Processed: {stats['total_events']}")
    print(f"Errors Encountered: {stats['errors']}")
    print("\nChanges by Type:")
    for change_type, count in stats['changes_by_type'].items():
        print(f"{change_type}: {count}")
    print("\nChanges by Object:")
    for object_type, count in stats['changes_by_object'].items():
        print(f"{object_type}: {count}")

# Sample data from exercise file
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