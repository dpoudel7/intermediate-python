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
    
    # TODO 1: Create a list of opportunity summaries for a report
    # Format: {"opportunity": "New Software", "account": "Acme Corp", "value": "50000.00"}
    opportunity_summaries = None  # Replace None with your map operation
    
    # TODO 2: Calculate weighted amounts for pipeline report
    # Format: {"name": "New Software", "weighted_amount": 30000.00} (amount * probability / 100)
    weighted_amounts = None  # Replace None with your map operation
    
    # TODO 3: Create a list of opportunities by industry
    # Format: "Technology: New Software ($50000.00)"
    opportunities_by_industry = None  # Replace None with your map operation
    
    # Test your solutions
    if opportunity_summaries and weighted_amounts and opportunities_by_industry:
        print("Opportunity Summaries:", opportunity_summaries)
        print("\nWeighted Amounts:", weighted_amounts)
        print("\nOpportunities by Industry:", opportunities_by_industry)
    else:
        print("Please complete the TODOs first!")

    
exercise()