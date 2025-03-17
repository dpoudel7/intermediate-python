opportunities = [
    {
        'id': 'O001',
        'name': 'Enterprise Deal',
        'account': 'Acme Corp',
        'stage': 'Negotiation',
        'amount': 100000,
        'probability': 75,
        'close_date': '2024-03-31',
        'type': 'New Business'
    },
    {
        'id': 'O002',
        'name': 'Expansion Project',
        'account': 'TechCo',
        'stage': 'Proposal',
        'amount': 50000,
        'probability': 50,
        'close_date': '2024-02-28',
        'type': 'Expansion'
    },
    {
        'id': 'O003',
        'name': 'Renewal Deal',
        'account': 'StartUp Inc',
        'stage': 'Closed Won',
        'amount': 25000,
        'probability': 100,
        'close_date': '2024-01-31',
        'type': 'Renewal'
    }
]

# Example 1: Calculate weighted amounts
weighted_amounts = list(map(
    lambda opp: {
        'name': opp['name'],
        'weighted_amount': opp['amount'] * opp['probability'] / 100
    },
    opportunities
))
print("\nWeighted opportunity amounts:")
for wa in weighted_amounts:
    print(f"{wa['name']}: ${wa['weighted_amount']:,.2f}")

# Example 2: Filter and transform in one chain
high_probability_names = list(map(
    lambda opp: opp['name'],
    filter(lambda opp: opp['probability'] >= 75, opportunities)
))
print("\nHigh probability opportunities:", high_probability_names)

# Example 3: Complex sorting with multiple criteria
multi_sorted_opps = sorted(
    opportunities,
    key=lambda opp: (opp['stage'] != 'Closed Won', -opp['probability'], -opp['amount'])
)
print("\nOpportunities by stage, probability, and amount:")
for opp in multi_sorted_opps:
    print(f"{opp['name']}: {opp['stage']}, {opp['probability']}%, ${opp['amount']:,}")