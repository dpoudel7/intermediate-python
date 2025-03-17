# Example: Processing Salesforce leads
leads = [
    {'name': 'John Doe', 'company': 'Acme Corp', 'score': 85},
    {'name': 'Jane Smith', 'company': 'TechCo', 'score': 92},
    {'name': 'Bob Wilson', 'company': 'StartUp Inc', 'score': 78}
]

# Traditional function definition for a simple operation
def get_lead_score(lead):
    return lead['score']

# Another simple function that could be more concise
def is_qualified_lead(lead):
    return lead['score'] >= 80

# Function that just returns a field
def get_company_name(lead):
    return lead['company']

# Using these functions
qualified_leads = list(filter(is_qualified_lead, leads))
company_names = list(map(get_company_name, qualified_leads))

print("Qualified companies:", company_names)
print("Highest score:", max(leads, key=get_lead_score)['name'])