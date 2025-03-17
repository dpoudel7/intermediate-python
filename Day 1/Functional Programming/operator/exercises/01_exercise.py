from operator import (
    add, sub, mul, truediv, floordiv,
    itemgetter, attrgetter, methodcaller,
    lt, le, eq, ne, ge, gt
)
from functools import reduce
from typing import List, Dict, Any

problematic_leads = [
    {
        'Name': 'John Doe',
        'Email': 'john.doe@email.com',
        'Phone': '(555) 123-4567',
        'LeadScore': '95',
        'LastActivityDate': '2024-01-15'
    },
    {
        'Name': 'Jane Smith',
        'Email': 'invalid-email',
        'Phone': '5551234567',
        'LeadScore': 'High',
        'LastActivityDate': '2024-02-01'
    },
    {
        'Name': 'Bob Johnson',
        'Email': 'bob.j@email.com',
        'Phone': '555.123.4567',
        'LeadScore': '75',
        'LastActivityDate': 'Yesterday'
    }
]

def exercise():
    """Data validation with operator functions."""
    print("\nExercise: Data Validation")
    
    # TODO 1: Validate lead scores
    # Check if score is numeric and between 0-100
    # Return: {"name": "John Doe", "score": 95, "is_valid": True}
    validated_scores = None  # Replace with your solution
    
    # TODO 2: Extract and standardize phone numbers
    # Remove non-digits and format as (XXX) XXX-XXXX
    # Use operator functions where possible
    formatted_phones = None  # Replace with your solution
    
    # TODO 3: Filter valid leads and sort by score
    # Valid leads have valid score and properly formatted email
    # Sort by score in descending order
    valid_leads = None  # Replace with your solution
    
    # Test your solutions
    if validated_scores and formatted_phones and valid_leads:
        print("Validated Scores:", validated_scores)
        print("\nFormatted Phones:", formatted_phones)
        print("\nValid Leads:", valid_leads)
    else:
        print("Please complete the TODOs first!")