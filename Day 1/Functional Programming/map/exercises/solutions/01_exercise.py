opportunities = [
    {
        'Id': 'O001',
        'Name': 'New Software',
        'Account': {'Name': 'Acme Corp', 'Industry': 'Technology'},
        'Amount': '50000.00',
        'StageName': 'Negotiation',
        'Probability': '60',
        'CloseDate': '2024-03-31'
    },
    {
        'Id': 'O002',
        'Name': 'Consulting Project',
        'Account': {'Name': 'TechCo', 'Industry': 'Manufacturing'},
        'Amount': '75000.00',
        'StageName': 'Proposal',
        'Probability': '40',
        'CloseDate': '2024-06-30'
    },
    {
        'Id': 'O003',
        'Name': 'Support Contract',
        'Account': {'Name': 'StartUp Inc', 'Industry': 'Technology'},
        'Amount': '25000.00',
        'StageName': 'Closed Won',
        'Probability': '100',
        'CloseDate': '2024-01-31'
    }
]

def exercise():
    """Data transformation for report generation."""
    print("\nExercise: Report Generation")
    
    # Solution 1: Create opportunity summaries
    # We extract and format the required fields into a new dictionary
    opportunity_summaries = list(map(
        lambda opp: {
            "opportunity": opp['Name'],
            "account": opp['Account']['Name'],
            "value": opp['Amount']
        },
        opportunities
    ))
    
    # Solution 2: Calculate weighted amounts
    # We convert string values to float and calculate weighted amount
    weighted_amounts = list(map(
        lambda opp: {
            "name": opp['Name'],
            "weighted_amount": float(opp['Amount']) * float(opp['Probability']) / 100
        },
        opportunities
    ))
    
    # Solution 3: Format opportunities by industry
    # We combine industry and opportunity details into a formatted string
    opportunities_by_industry = list(map(
        lambda opp: f"{opp['Account']['Industry']}: {opp['Name']} (${opp['Amount']})",
        opportunities
    ))
    
    # Test the solutions
    print("Opportunity Summaries:", opportunity_summaries)
    print("\nWeighted Amounts:", weighted_amounts)
    print("\nOpportunities by Industry:", opportunities_by_industry)

    
exercise()