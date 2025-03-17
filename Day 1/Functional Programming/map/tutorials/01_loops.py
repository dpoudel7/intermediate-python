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

# Using a for loop
formatted_contacts = []
for contact in contacts:
    formatted_contact = {
        'name': f"{contact['FirstName']} {contact['LastName']}",
        'email': contact['Email'].lower(),
        'title': contact['Title'].upper()
    }
    formatted_contacts.append(formatted_contact)

# Using list comprehension
formatted_contacts_lc = [
    {
        'name': f"{c['FirstName']} {c['LastName']}",
        'email': c['Email'].lower(),
        'title': c['Title'].upper()
    }
    for c in contacts
]

print("Using for loop:", formatted_contacts)
print("Using list comprehension:", formatted_contacts_lc)
