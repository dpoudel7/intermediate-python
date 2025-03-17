
contacts = [
    {
        'id': 'C001',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@email.com',
        'title': 'CEO',
        'department': 'Executive',
        'created_date': '2023-01-15',
        'last_modified': '2023-12-01'
    },
    {
        'id': 'C002',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane.smith@email.com',
        'title': 'VP Sales',
        'department': 'Sales',
        'created_date': '2023-02-20',
        'last_modified': '2023-11-15'
    },
    {
        'id': 'C003',
        'first_name': 'Bob',
        'last_name': 'Johnson',
        'email': 'bob.johnson@email.com',
        'title': 'Developer',
        'department': 'IT',
        'created_date': '2023-03-10',
        'last_modified': '2023-12-05'
    }
]

def exercise1():
    """Basic lambda operations with contact data."""
    print("\nExercise 1: Basic Lambda Operations")
    
    # TODO 1: Create a lambda function to get full name (first_name + ' ' + last_name)
    get_full_name = lambda contact: f"{contact['first_name']} {contact['last_name']}"
    
    # TODO 2: Create a lambda function to get email domain (part after @ in email)
    get_email_domain = lambda email: email.split('@')[-1]
    
    # TODO 3: Create a lambda function to check if contact is from Sales department
    is_sales = lambda contact: contact['department'] == 'Sales'
    
    # Test your lambdas
    if get_full_name and get_email_domain and is_sales:
        print("Full names:", list(map(get_full_name, contacts)))
        print("Email domains:", list(map(get_email_domain, contacts)))
        print("Sales contacts:", list(filter(is_sales, contacts)))
    else:
        print("Please complete the TODOs first!")

exercise1()