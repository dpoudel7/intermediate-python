contacts = [
    {
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': 'john.doe@email.com',
        'Title': 'CEO'
    },
    {
        'FirstName': 'Jane',
        'LastName': 'Smith',
        'Email': 'jane.smith@email.com',
        'Title': 'CTO'
    }
]

def format_name(contact):
    return f"{contact['FirstName']} {contact['LastName']}"

# Using a for loop
for contact in contacts:
    contact['name'] = format_name(contact)

# Using list comprehension
# formatted_contacts_lc = [
#     {
#         'name': f"{c['FirstName']} {c['LastName']}",
#         'email': c['Email'].lower(),
#         'title': c['Title'].upper()
#     }
#     for c in contacts
# ]

# print("Using for loop:", formatted_contacts)
# print("Using list comprehension:", formatted_contacts_lc)
