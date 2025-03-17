# -----------------------------------------------------------------------------
# INTRODUCING NAMEDTUPLE
# -----------------------------------------------------------------------------

from collections import namedtuple


first_name_tuple = namedtuple("First_Name", ["first_name", "last_name"])

first_name_tuple = first_name_tuple("John", "Doe")

print(first_name_tuple)

# -----------------------------------------------------------------------------
# ACCESSING NAMEDTUPLE
# -----------------------------------------------------------------------------

print(first_name_tuple.first_name)
print(first_name_tuple.last_name)


# -----------------------------------------------------------------------------
# CUSOMTER FOR NAMEDTUPLE
# -----------------------------------------------------------------------------

customer = namedtuple("Customer", ["name", "email", "phone", "status", "spend"])

customer = customer("John Doe", "john.doe@example.com", "123-456-7890", "Gold", 50000)

print(customer)

print(f"Customer name: {customer.name}")
print(f"Customer email: {customer.email}")
print(f"Customer phone: {customer.phone}")
print(f"Customer status: {customer.status}")
print(f"Customer spend: {customer.spend}")


# -----------------------------------------------------------------------------
# NAMEDTUPLE INTERNALS
# -----------------------------------------------------------------------------

print(customer._fields)

print(customer._field_defaults)


# -----------------------------------------------------------------------------
# ADVANCED NAMEDTUPLE FEATURES
# -----------------------------------------------------------------------------

customer = customer._replace(status="Silver")

print(customer)

# -----------------------------------------------------------------------------
# NAMEDTUPLE AS A DICTIONARY
# -----------------------------------------------------------------------------

customer_dict = customer._asdict()

print(customer_dict)


# -----------------------------------------------------------------------------
# NAMEDTUPLE FROM A DICTIONARY
# -----------------------------------------------------------------------------

Customer = namedtuple('Customer', ['name', 'email', 'phone', 'status', 'annual_spend'])

# Creating from a dictionary
customer_data = {
    'name': 'Alice Johnson',
    'email': 'alice@example.com',
    'phone': '555-123-4567',
    'status': 'Silver',
    'annual_spend': 30000
}

# The ** unpacks the dictionary into keyword arguments
customer = Customer(**customer_data)
print(f"Customer from dict: {customer}")










