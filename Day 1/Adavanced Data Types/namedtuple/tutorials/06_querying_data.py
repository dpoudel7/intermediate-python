from collections import namedtuple
import json
import csv
from datetime import datetime
from typing import List, Dict, Any, NamedTuple


# Define namedtuples for common Salesforce objects
Account = namedtuple('Account', [
    'id', 'name', 'industry', 'type', 'annual_revenue', 
    'billing_city', 'billing_country', 'created_date'
])

Contact = namedtuple('Contact', [
    'id', 'first_name', 'last_name', 'email', 'phone',
    'title', 'account_id', 'created_date'
])

Opportunity = namedtuple('Opportunity', [
    'id', 'name', 'stage', 'amount', 'close_date', 
    'probability', 'account_id', 'created_date'
])

# Sample data (as if from Salesforce API)
accounts = [
    Account('001A', 'Acme Corporation', 'Manufacturing', 'Customer', 1500000, 
            'San Francisco', 'USA', '2020-01-15'),
    Account('001B', 'Globex', 'Technology', 'Customer', 3000000, 
            'New York', 'USA', '2019-05-22'),
    Account('001C', 'Stark Industries', 'Defense', 'Prospect', 5000000, 
            'Los Angeles', 'USA', '2018-11-30'),
    Account('001D', 'Wayne Enterprises', 'Technology', 'Customer', 4200000, 
            'Gotham', 'USA', '2019-03-17'),
    Account('001E', 'Umbrella Corp', 'Pharmaceutical', 'Customer', 2800000, 
            'Raccoon City', 'USA', '2020-02-08')
]

contacts = [
    Contact('003A', 'John', 'Smith', 'john@acme.com', '555-123-4567', 
            'CEO', '001A', '2020-01-20'),
    Contact('003B', 'Jane', 'Doe', 'jane@acme.com', '555-234-5678', 
            'CTO', '001A', '2020-01-25'),
    Contact('003C', 'Bob', 'Johnson', 'bob@globex.com', '555-345-6789', 
            'VP Sales', '001B', '2019-06-15'),
    Contact('003D', 'Tony', 'Stark', 'tony@stark.com', '555-456-7890', 
            'CEO', '001C', '2018-12-10'),
    Contact('003E', 'Bruce', 'Wayne', 'bruce@wayne.com', '555-567-8901', 
            'CEO', '001D', '2019-04-01'),
    Contact('003F', 'Albert', 'Wesker', 'wesker@umbrella.com', '555-678-9012', 
            'Research Director', '001E', '2020-02-15')
]

opportunities = [
    Opportunity('006A', 'Acme Q1 Order', 'Closed Won', 250000, '2023-03-15', 
                90, '001A', '2023-01-10'),
    Opportunity('006B', 'Acme Q2 Order', 'Negotiation', 300000, '2023-06-30', 
                60, '001A', '2023-04-05'),
    Opportunity('006C', 'Globex Project', 'Proposal', 500000, '2023-07-15', 
                40, '001B', '2023-02-20'),
    Opportunity('006D', 'Stark Contract', 'Qualification', 1000000, '2023-09-01', 
                20, '001C', '2023-03-15'),
    Opportunity('006E', 'Wayne Tech Deal', 'Closed Won', 750000, '2023-02-28', 
                100, '001D', '2022-11-10'),
    Opportunity('006F', 'Umbrella Research', 'Negotiation', 450000, '2023-08-15', 
                70, '001E', '2023-05-01')
]

# -----------------------------------------------------------------------------
# QUERYING DATA
# -----------------------------------------------------------------------------


def find_contacts_by_account(contacts: List[Contact], account_id: str) -> List[Contact]:
    return [contact for contact in contacts if contact.account_id == account_id]

def find_opportunities_by_stage(opportunities: List[Opportunity], stage: str) -> List[Opportunity]:
    return [opportunity for opportunity in opportunities if opportunity.stage == stage]

def calculate_total_opportunity_value(opportunities: List[Opportunity]) -> float:
    return sum(float(opp.amount) for opp in opportunities)


acme_id = '001A'
acme_contacts = find_contacts_by_account(contacts, acme_id)

print(f"Contacts for Acme Corporation (ID: {acme_id}):")
for contact in acme_contacts:
    print(f"  - {contact.first_name} {contact.last_name} ({contact.title})")

# Find all opportunities in Negotiation stage
negotiation_opps = find_opportunities_by_stage(opportunities, 'Negotiation')

print("\nOpportunities in Negotiation stage:")
for opp in negotiation_opps:
    print(f"  - {opp.name}: ${float(opp.amount):,.2f} (Probability: {opp.probability}%)")

# Calculate total and weighted opportunity values
total_value = calculate_total_opportunity_value(opportunities)

print(f"\nTotal opportunity pipeline: ${total_value:,.2f}")






