
from collections import namedtuple

# Define namedtuples for common Salesforce objects
Account = namedtuple('Account', ['id', 'name', 'industry', 'annual_revenue', 'created_date'])
Contact = namedtuple('Contact', ['id', 'first_name', 'last_name', 'email', 'account_id'])
Opportunity = namedtuple('Opportunity', ['id', 'name', 'stage', 'amount', 'close_date', 'account_id'])

accounts = [
    Account(id='001A',
            name='Acme Corporation',
            industry='Manufacturing',
            annual_revenue=1500000,
            created_date='2020-01-15'),
    Account('001B', 'Globex', 'Technology', 3000000, '2019-05-22'),
    Account('001C', 'Stark Industries', 'Defense', 5000000, '2018-11-30')
]

contacts = [
    Contact('003A', 'John', 'Smith', 'john@acme.com', '001A'),
    Contact('003B', 'Jane', 'Doe', 'jane@acme.com', '001A'),
    Contact('003C', 'Bob', 'Johnson', 'bob@globex.com', '001B')
]

opportunities = [
    Opportunity('006A', 'Acme Q1 Order', 'Closed Won', 250000, '2023-03-15', '001A'),
    Opportunity('006B', 'Globex Project', 'Negotiation', 500000, '2023-06-30', '001B'),
    Opportunity('006C', 'Stark Contract', 'Qualification', 1000000, '2023-09-01', '001C')
]

# -----------------------------------------------------------------------------
# EXAMPLE: Find all contacts for a specific account
# -----------------------------------------------------------------------------

acme_id = '001A'
acme_contacts = [contact for contact in contacts if contact.account_id == acme_id]
print(acme_contacts)
print(f"Contacts for Acme Corporation:")
for contact in acme_contacts:
    print(f"  - {contact.first_name} {contact.last_name} ({contact.email})")

# -----------------------------------------------------------------------------
# EXAMPLE: Calculate total opportunity value by account
# -----------------------------------------------------------------------------

account_opportunity_totals = {}
for opp in opportunities:
    if opp.account_id not in account_opportunity_totals:
        account_opportunity_totals[opp.account_id] = 0
    account_opportunity_totals[opp.account_id] += opp.amount

print("\nTotal opportunity value by account:")
for account in accounts:
    total = account_opportunity_totals.get(account.id, 0)
    print(f"  - {account.name}: ${total:,}")