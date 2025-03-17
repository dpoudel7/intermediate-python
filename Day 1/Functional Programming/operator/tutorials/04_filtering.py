from operator import (
    add, sub, mul, truediv, floordiv,
    itemgetter, attrgetter, methodcaller,
    lt, le, eq, ne, ge, gt
)
from functools import reduce
from typing import List, Dict, Any
from decimal import Decimal


# Sample contact data
contacts = [
    {
        'Name': 'John Doe',
        'Title': 'CEO',
        'Department': 'Executive',
        'LastActivityDate': '2024-01-15',
        'LeadScore': 95
    },
    {
        'Name': 'Jane Smith',
        'Title': 'VP Sales',
        'Department': 'Sales',
        'LastActivityDate': '2024-02-01',
        'LeadScore': 85
    },
    {
        'Name': 'Bob Johnson',
        'Title': 'Developer',
        'Department': 'IT',
        'LastActivityDate': '2024-01-20',
        'LeadScore': 75
    }
]
