numbers = [1, 2, 3, 4, 5]

def is_even(x):
    return x % 2 == 0

res = [number for number in numbers if number % 2 == 0]

lambda_fn = lambda x: x % 2 == 0
lambda_res = [number for number in numbers if lambda_fn(number)]

print("Squared numbers:", lambda_res)

# -----------------------------------------------------------------------------


leads = [
    {'name': 'John Doe', 'company': 'Acme Corp', 'score': 85},
    {'name': 'Jane Smith', 'company': 'TechCo', 'score': 92},
    {'name': 'Bob Wilson', 'company': 'StartUp Inc', 'score': 78}
]

# Using lambda functions for simple operations

score_fn = lambda lead: lead['score'] >= 80
company_fn = lambda lead: lead['company']

qualified_companies = list(map(
    company_fn,
    filter(score_fn, leads)
))


highest_scorer = max(leads, key=lambda lead: lead['score'])['name'] # ->

max_company = 0
max_score = 0
for lead in leads:
    if lead['score'] > max_score:
        max_score = lead['score']
        max_company = lead['name']

print("Qualified companies:", qualified_companies)
print("Highest score:", highest_scorer)
print("Max score:", max_company)

print(sorted(leads, key=lambda lead: lead['score'], reverse=False))

list_of_tuples = [("John", 25), ("Anne", 22), ("Bob", 30)]

print(sorted(list_of_tuples, key=lambda x:x[1], reverse=False))