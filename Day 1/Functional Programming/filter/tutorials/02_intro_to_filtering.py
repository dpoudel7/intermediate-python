# Simple filter example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Equivalent to the previous active users example
users = [
    {'id': 1, 'name': 'Alice', 'status': 'active'},
    {'id': 2, 'name': 'Bob', 'status': 'inactive'},
    {'id': 3, 'name': 'Charlie', 'status': 'active'}
]

active_users = list(filter(lambda user: user['status'] == 'active', users))

print(even_numbers)
print(active_users)
