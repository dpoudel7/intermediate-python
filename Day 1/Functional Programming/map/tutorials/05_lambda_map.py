contacts = [
    {
        'Id': 'C001',
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': 'john.doe@email.com',
        'Title': 'CEO',
        'Department': 'Executive',
        'Phone': '(555) 123-4567',
        'MailingCity': 'San Francisco',
        'MailingState': 'CA'
    },
    {
        'Id': 'C002',
        'FirstName': 'Jane',
        'LastName': 'Smith',
        'Email': 'jane.smith@email.com',
        'Title': 'VP Sales',
        'Department': 'Sales',
        'Phone': '(555) 234-5678',
        'MailingCity': 'New York',
        'MailingState': 'NY'
    },
    {
        'Id': 'C003',
        'FirstName': 'Bob',
        'LastName': 'Johnson',
        'Email': 'bob.j@email.com',
        'Title': 'Developer',
        'Department': 'IT',
        'Phone': '(555) 345-6789',
        'MailingCity': 'Chicago',
        'MailingState': 'IL'
    }
]

# Example 1: Simple field extraction
print("\nExample 1: Extracting full names")
get_full_name = lambda c: f"{c['FirstName']} {c['LastName']}"
full_names = list(map(get_full_name, contacts))
print("Full names:", full_names)

# Example 2: Creating email display format
print("\nExample 2: Email display format")
format_email = lambda c: f"{get_full_name(c)} <{c['Email']}>"
email_displays = list(map(format_email, contacts))
print("Email displays:", email_displays)

# Example 3: Formatting locations
print("\nExample 3: Location formatting")
format_location = lambda c: f"{c['MailingCity']}, {c['MailingState']}"
locations = list(map(format_location, contacts))
print("Locations:", locations)