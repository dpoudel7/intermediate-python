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

def is_valid_score(score):
    """Helper function to validate lead scores."""
    try:
        score_value = float(score)
        return ge(score_value, 0) and le(score_value, 100)
    except (ValueError, TypeError):
        return False

def format_phone(phone):
    """Helper function to format phone numbers."""
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return None

def is_valid_email(email):
    """Helper function to validate email addresses."""
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def exercise():
    """Data validation with operator functions."""
    print("\nExercise: Data Validation")
    
    # Solution 1: Validate lead scores
    get_name = itemgetter('Name')
    get_score = itemgetter('LeadScore')
    
    validated_scores = list(map(
        lambda lead: {
            'name': get_name(lead),
            'score': float(get_score(lead)) if is_valid_score(get_score(lead)) else None,
            'is_valid': is_valid_score(get_score(lead))
        },
        problematic_leads
    ))
    
    # Solution 2: Format phone numbers
    get_phone = itemgetter('Phone')
    
    formatted_phones = list(map(
        lambda lead: {
            'name': get_name(lead),
            'phone': format_phone(get_phone(lead))
        },
        problematic_leads
    ))
    
    # Solution 3: Filter and sort valid leads
    get_email = itemgetter('Email')
    
    valid_leads = sorted(
        filter(
            lambda lead: is_valid_score(get_score(lead)) and is_valid_email(get_email(lead)),
            problematic_leads
        ),
        key=lambda lead: float(get_score(lead)),
        reverse=True
    )
    
    # Test the solutions
    print("Validated Scores:", validated_scores)
    print("\nFormatted Phones:", formatted_phones)
    print("\nValid Leads:")
    for lead in valid_leads:
        print(f"{get_name(lead)} (Score: {get_score(lead)})")
    
    return validated_scores, formatted_phones, valid_leads

exercise()