from operator import (
    add, sub, mul, truediv, floordiv,
    itemgetter, attrgetter, methodcaller,
    lt, le, eq, ne, ge, gt
)
import re
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
        'Phone': '555.123.456744',
        'LeadScore': '75',
        'LastActivityDate': 'Yesterday'
    }
]

def is_score_valid(score: str) -> bool:
    try:
        score = int(score)
        return ge(score, 0) and le(score, 100)
    except (ValueError, TypeError):
        return False
    
def format_phone(phone: str) -> str:
    # step 1: remove non-digits from the phone
    phone = "".join(filter(str.isdigit, phone))
    # step 2: format the phone as (XXX) XXX-XXXX
    return f"({phone[:3]}) {phone[3:6]}-{phone[6:10]}" 

def is_email_valid(email: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def exercise():
    """Data validation with operator functions."""
    print("\nExercise: Data Validation")
    
    get_name = itemgetter('Name')
    get_score = itemgetter('LeadScore')
    get_email = itemgetter('Email')
    get_phone = itemgetter('Phone')

    # TODO 1: Validate lead scores
    # Check if score is numeric and between 0-100
    # Return: {"name": "John Doe", "score": 95, "is_valid": True}
    validated_scores = list(map(
        lambda lead: {
            "name": get_name(lead),
            "score": int(get_score(lead)) if is_score_valid(get_score(lead)) else "ErrorGettingScore",
            "is_valid": is_score_valid(get_score(lead))
        },
        problematic_leads
    ))
    
    # TODO 2: Extract and standardize phone numbers
    # Remove non-digits and format as (XXX) XXX-XXXX
    # Use operator functions where possible
    formatted_phones = list(map(
        lambda lead:{
            "name": get_name(lead),
            "old_phone": get_phone(lead),
            "phone": format_phone(get_phone(lead))
        },
        problematic_leads
    ))
    
    # TODO 3: Filter valid leads and sort by score
    # Valid leads have valid score and properly formatted email
    # Sort by score in descending order
    valid_leads = sorted(
        filter(
            lambda lead: is_score_valid(get_score(lead)) and is_email_valid(get_email(lead)),
            problematic_leads
        ),
        key=lambda lead: float(get_score(lead)),
        reverse=False
    )
    
    # Test your solutions
    if validated_scores and formatted_phones and valid_leads:
        print("Validated Scores:", validated_scores)
        print("\nFormatted Phones:", formatted_phones)
        print("\nValid Leads:", valid_leads)
    else:
        print("Please complete the TODOs first!")


exercise()