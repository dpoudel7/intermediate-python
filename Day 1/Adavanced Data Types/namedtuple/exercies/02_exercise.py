from collections import namedtuple
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import csv
import json

# Sample lead data (as if from Salesforce)
lead_data = [
    {
        "id": "00QL000000A1B2C",
        "first_name": "John",
        "last_name": "Smith",
        "email": "john.smith@example.com",
        "company": "Acme Inc",
        "industry": "Manufacturing",
        "status": "Qualified",
        "created_date": "2023-01-15",
        "lead_source": "Website",
        "rating": "Hot"
    },
    {
        "id": "00QL000000D3E4F",
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com",
        "company": "Globex Corp",
        "industry": "Technology",
        "status": "Working",
        "created_date": "2023-02-10",
        "lead_source": "Trade Show",
        "rating": "Warm"
    },
    {
        "id": "00QL000000G5H6I",
        "first_name": "Bob",
        "last_name": "Johnson",
        "email": "bob.johnson@example.com",
        "company": "Stark Industries",
        "industry": "Defense",
        "status": "Qualified",
        "created_date": "2023-01-20",
        "lead_source": "Partner Referral",
        "rating": "Hot"
    },
    {
        "id": "00QL000000J7K8L",
        "first_name": "Alice",
        "last_name": "Williams",
        "email": "alice.williams@example.com",
        "company": "Wayne Enterprises",
        "industry": "Technology",
        "status": "Unqualified",
        "created_date": "2023-03-05",
        "lead_source": "Website",
        "rating": "Cold"
    },
    {
        "id": "00QL000000M9N0P",
        "first_name": "Charlie",
        "last_name": "Brown",
        "email": "charlie.brown@example.com",
        "company": "Umbrella Corp",
        "industry": "Pharmaceutical",
        "status": "Qualified",
        "created_date": "2023-02-25",
        "lead_source": "Email Campaign",
        "rating": "Warm"
    }
]

# Sample conversion data (as if from Salesforce)
conversion_data = [
    {
        "lead_id": "00QL000000A1B2C",
        "opportunity_id": "006R000000ABCDE",
        "opportunity_name": "Acme Inc - New Equipment",
        "amount": 75000,
        "stage": "Closed Won",
        "close_date": "2023-03-20",
        "converted_date": "2023-01-25",
        "days_to_convert": 10,
        "converted_by": "Sarah Johnson"
    },
    {
        "lead_id": "00QL000000G5H6I",
        "opportunity_id": "006R000000FGHIJ",
        "opportunity_name": "Stark Industries - Defense Contract",
        "amount": 250000,
        "stage": "Negotiation",
        "close_date": "2023-04-15",
        "converted_date": "2023-02-05",
        "days_to_convert": 16,
        "converted_by": "Michael Chen"
    },
    {
        "lead_id": "00QL000000M9N0P",
        "opportunity_id": "006R000000KLMNO",
        "opportunity_name": "Umbrella Corp - Research Partnership",
        "amount": 120000,
        "stage": "Proposal",
        "close_date": "2023-05-10",
        "converted_date": "2023-03-10",
        "days_to_convert": 13,
        "converted_by": "Sarah Johnson"
    }
]


# TODO: Create a Lead namedtuple with fields matching the lead_data dictionary keys
# Hint: Use the keys from the first lead_data entry as field names


# TODO: Create a Conversion namedtuple with fields matching the conversion_data dictionary keys
# Hint: Use the keys from the first conversion_data entry as field names


def convert_dict_to_leads(lead_dicts: List[Dict]) -> List:
    """Convert a list of lead dictionaries to a list of Lead namedtuples."""
    leads = []
    
    # TODO: Iterate through lead_dicts and create a Lead namedtuple for each dictionary
    # Hint: Use the ** operator to unpack the dictionary into keyword arguments
    
    return leads

def convert_dict_to_conversions(conversion_dicts: List[Dict]) -> List:
    """Convert a list of conversion dictionaries to a list of Conversion namedtuples."""
    conversions = []
    
    # TODO: Iterate through conversion_dicts and create a Conversion namedtuple for each dictionary
    # Hint: Use the ** operator to unpack the dictionary into keyword arguments
    
    return conversions

def find_leads_by_status(leads: List, status: str) -> List:
    """Find all leads with a specific status."""
    # TODO: Use a list comprehension to filter leads by status
    
    return []


def find_hot_leads(leads: List) -> List:
    """Find all leads with a 'Hot' rating."""
    # TODO: Use a list comprehension to filter leads by rating
    
    return []

def find_conversion_by_lead_id(conversions: List, lead_id: str) -> Optional:
    """Find the conversion for a specific lead ID, if it exists."""
    # TODO: Use a for loop or list comprehension to find the conversion with the given lead_id
    # Return None if no conversion is found
    
    return None


