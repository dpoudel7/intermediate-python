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

# Example 1: Sorting with itemgetter
print("\nExample 1: Sorting Contacts")
get_score = itemgetter('LeadScore')
sorted_contacts = sorted(contacts, key=get_score, reverse=True)
print("Sorted by Lead Score:")
for contact in sorted_contacts:
    print(f"{contact['Name']}: {contact['LeadScore']}")

# Example 2: Filtering with operator functions
print("\nExample 2: Filtering Contacts")
high_value_contacts = list(filter(
    lambda x: gt(get_score(x), 80),
    contacts
))
print("\nHigh Value Contacts:")
for contact in high_value_contacts:
    print(f"{contact['Name']} (Score: {contact['LeadScore']})")