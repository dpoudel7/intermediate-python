opportunities = [
    {
        'Id': '006A000001',
        'Name': 'Big Deal',
        'Amount': '50000.00',
        'StageName': 'Negotiation',
        'Probability': '80.0',
        'CloseDate': '2024-03-31',
        'Account': {'Name': 'Acme Corp', 'Industry': 'Technology'}
    },
    {
        'Id': '006A000002',
        'Name': 'Small Deal',
        'Amount': '10000.00',
        'StageName': 'Prospecting',
        'Probability': '20.0',
        'CloseDate': '2024-06-30',
        'Account': {'Name': 'TechCo', 'Industry': 'Manufacturing'}
    }
]

# Clean and standardize data
def clean_opportunity(opp):
    return {
        'id': opp['Id'],
        'name': opp['Name'],
        'amount': float(opp['Amount']),
        'stage': opp['StageName'],
        'probability': float(opp['Probability']),
        'close_date': opp['CloseDate'],
        'account_name': opp['Account']['Name'],
        'industry': opp['Account']['Industry']
    }

# Transform for analytics
def calculate_weighted_amount(opp):
    return {
        'name': opp['name'],
        'weighted_amount': opp['amount'] * opp['probability'] / 100
    }

# Chain transformations
clean_opps = map(clean_opportunity, opportunities)
weighted_opps = map(calculate_weighted_amount, clean_opps)

print(list(weighted_opps))
