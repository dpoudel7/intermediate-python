numbers = [1, 2, 3, 4, 5]

# Using lambda functions for simple operations
squared_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Squared numbers:", squared_numbers)



# -----------------------------------------------------------------------------


leads = [
    {'name': 'John Doe', 'company': 'Acme Corp', 'score': 85},
    {'name': 'Jane Smith', 'company': 'TechCo', 'score': 92},
    {'name': 'Bob Wilson', 'company': 'StartUp Inc', 'score': 78}
]

# Using lambda functions for simple operations
qualified_companies = list(map(
    lambda lead: lead['company'],
    filter(lambda lead: lead['score'] >= 80, leads)
))

highest_scorer = max(leads, key=lambda lead: lead['score'])['name']

print("Qualified companies:", qualified_companies)
print("Highest score:", highest_scorer)