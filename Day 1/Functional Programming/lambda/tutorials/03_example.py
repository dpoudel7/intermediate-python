opportunities = [
    {
        'name': 'Big Deal',
        'amount': 50000,
        'stage': 'Negotiation',
        'probability': 80,
        'close_date': '2023-12-31'
    },
    {
        'name': 'Small Deal',
        'amount': 10000,
        'stage': 'Prospecting',
        'probability': 20,
        'close_date': '2023-11-30'
    },
    {
        'name': 'Medium Deal',
        'amount': 25000,
        'stage': 'Closed Won',
        'probability': 100,
        'close_date': '2023-10-15'
    }
]

# Example 1: Filtering high-value opportunities
high_value = list(filter(lambda opp: opp['amount'] > 20000, opportunities))

# Example 2: Calculating weighted amounts
weighted_amounts = list(map(
    lambda opp: opp['amount'] * opp['probability'] / 100,
    opportunities
))

# Example 3: Sorting by amount
sorted_opps = sorted(opportunities, key=lambda opp: opp['amount'], reverse=True)

# Example 4: Finding total potential revenue
total_potential = sum(map(lambda opp: opp['amount'], opportunities))

# Example 5: Complex filtering with multiple conditions
promising_deals = list(filter(
    lambda opp: opp['probability'] > 50 and opp['stage'] != 'Closed Won',
    opportunities
))