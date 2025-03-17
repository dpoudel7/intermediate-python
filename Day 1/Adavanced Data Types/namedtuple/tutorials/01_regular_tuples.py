# A customer record as a regular tuple
customer = (
    'John Doe',
    'john.doe@example.com',
    '123-456-7890',
    'Gold',
    50000
    )

# Accessing data requires remembering indices
print(f"Customer name: {customer[0]}")
print(f"Customer email: {customer[1]}")

# What was at index 3 again? Status or spending?
print(f"Customer status: {customer[3]}")

# If we change the structure, all code breaks
# New structure with address added at position 1
customer_v2 = (
    'Jane Smith',
    '123 Main St',
    'jane.smith@example.com',
    '987-654-3210',
    'Silver',
    25000)

# This now prints the address instead of the email!
print(f"Customer email: {customer_v2[1]}")

