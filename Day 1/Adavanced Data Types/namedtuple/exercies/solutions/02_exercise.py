
from collections import namedtuple
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import csv
import json

# -----------------------------------------------------------------------------
# PART 1: CREATE NAMEDTUPLES FOR LEAD AND CONVERSION DATA
# -----------------------------------------------------------------------------

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

# Create a Lead namedtuple with fields matching the lead_data dictionary keys
Lead = namedtuple('Lead', [
    'id', 'first_name', 'last_name', 'email', 'company', 
    'industry', 'status', 'created_date', 'lead_source', 'rating'
])

# Create a Conversion namedtuple with fields matching the conversion_data dictionary keys
Conversion = namedtuple('Conversion', [
    'lead_id', 'opportunity_id', 'opportunity_name', 'amount', 'stage',
    'close_date', 'converted_date', 'days_to_convert', 'converted_by'
])


def convert_dict_to_leads(lead_dicts: List[Dict]) -> List[Lead]:
    """Convert a list of lead dictionaries to a list of Lead namedtuples."""
    leads = []
    
    for lead_dict in lead_dicts:
        # Create a Lead namedtuple from the dictionary
        lead = Lead(**lead_dict)
        leads.append(lead)
    
    return leads

def convert_dict_to_conversions(conversion_dicts: List[Dict]) -> List[Conversion]:
    """Convert a list of conversion dictionaries to a list of Conversion namedtuples."""
    conversions = []
    
    for conversion_dict in conversion_dicts:
        # Create a Conversion namedtuple from the dictionary
        conversion = Conversion(**conversion_dict)
        conversions.append(conversion)
    
    return conversions

def find_leads_by_status(leads: List[Lead], status: str) -> List[Lead]:
    """Find all leads with a specific status."""
    return [lead for lead in leads if lead.status == status]


def find_hot_leads(leads: List[Lead]) -> List[Lead]:
    """Find all leads with a 'Hot' rating."""
    return [lead for lead in leads if lead.rating == 'Hot']


def find_conversion_by_lead_id(conversions: List[Conversion], lead_id: str) -> Optional[Conversion]:
    """Find the conversion for a specific lead ID, if it exists."""
    for conversion in conversions:
        if conversion.lead_id == lead_id:
            return conversion
    return None