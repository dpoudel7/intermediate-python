# Same contact data
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

# Define transformation functions
def format_name(contact):
    return f"{contact['FirstName']} {contact['LastName']}"

def format_contact(contact):
    return {
        'name': format_name(contact),
        'email': contact['Email'].lower(),
        'title': contact['Title'].upper()
    }

# Using map
formatted_contacts = list(map(format_contact, contacts))
print(formatted_contacts)

# Composing multiple transformations
names = list(map(format_name, contacts))
emails = list(map(lambda c: c['Email'].lower(), contacts))
titles = list(map(lambda c: c['Title'].upper(), contacts))

print("Using map:", formatted_contacts)
print("Names:", names)
print("Emails:", emails)
print("Titles:", titles)


print("### Using filter ###")
numbers = [1, 2, 3, 4, 5]
print(list(filter(lambda n: n > 3, numbers)))

filtering_fn = lambda n: n > 3
mid_step = list(map(filtering_fn, numbers))
print([n for i, n in enumerate(numbers) if mid_step[i]])
