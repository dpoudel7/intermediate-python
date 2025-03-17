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

