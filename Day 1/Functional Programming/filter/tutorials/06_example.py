from typing import List, Dict, Optional, Callable, Iterator
from datetime import datetime

# Sample record structure
Record = Dict[str, str | int | float | datetime]

# Sample Salesforce-like records
opportunity_records = [
    {
        'id': 'OPP001',
        'name': 'Enterprise Deal',
        'amount': 150000,
        'stage': 'Negotiation',
        'probability': 75,
        'close_date': '2024-06-30'
    },
    {
        'id': 'OPP002',
        'name': 'SMB Package',
        'amount': 25000,
        'stage': 'Prospecting',
        'probability': 25,
        'close_date': '2024-04-15'
    },
    {
        'id': 'OPP003',
        'name': 'Strategic Partnership',
        'amount': 500000,
        'stage': 'Closed Won',
        'probability': 100,
        'close_date': '2024-03-01'
    },
    {
        'id': 'OPP004',
        'name': 'Maintenance Contract',
        'amount': 75000,
        'stage': 'Negotiation',
        'probability': 60,
        'close_date': '2024-05-15'
    }
]

def analyze_opportunities(records: List[Record]) -> Dict:
    """Analyze opportunities using filter for different criteria."""
    # Filter high-value opportunities (amount > 100000)
    high_value = list(filter(
        lambda x: x['amount'] > 100000,
        records
    ))
    
    # Filter likely to close (probability >= 70)
    likely_to_close = list(filter(
        lambda x: x['probability'] >= 70,
        records
    ))
    
    # Filter active negotiations
    in_negotiation = list(filter(
        lambda x: x['stage'] == 'Negotiation',
        records
    ))
    
    # Combine filters using generator expressions
    high_value_negotiations = list(filter(
        lambda x: x['amount'] > 100000 and x['stage'] == 'Negotiation',
        records
    ))
    
    return {
        'high_value': high_value,
        'likely_to_close': likely_to_close,
        'in_negotiation': in_negotiation,
        'high_value_negotiations': high_value_negotiations
    }

print(analyze_opportunities(opportunity_records))



