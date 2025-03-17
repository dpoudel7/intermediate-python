
from collections import defaultdict

# Custom factory functions
def zero_to_hundred():
    return list(range(100))

number_lists = defaultdict(zero_to_hundred)
print("Custom factory - number list:", number_lists['first'][:5], "...")
print("Custom factory - number list:", number_lists['second'][:5], "...")

# Factory function that counts from a starting point
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

sequential_ids = defaultdict(Counter())
print("\nAutomatic sequential IDs:")
print(f"First ID: {sequential_ids['a']}")
print(f"Second ID: {sequential_ids['b']}")
print(f"Third ID: {sequential_ids['c']}")

# Using lambda for complex defaults
nested_default = defaultdict(lambda: defaultdict(set))
nested_default['users']['permissions'].add('read')
nested_default['users']['permissions'].add('write')
print("\nNested defaultdict with sets:", dict(nested_default))

# Type hints with defaultdict
from typing import DefaultDict, List, Set

# Explicitly typed defaultdict
user_roles: DefaultDict[str, Set[str]] = defaultdict(set)
user_roles['alice'].add('admin')
user_roles['bob'].add('user')
print("\nTyped defaultdict:", dict(user_roles))

# Performance pattern: precomputing defaults
from functools import partial

# Instead of lambda: {'count': 0, 'sum': 0}
def make_stats():
    return {'count': 0, 'sum': 0}

stats = defaultdict(make_stats)

# Using partial for parameterized defaults
def make_threshold(threshold=100):
    return {'value': 0, 'threshold': threshold}

# Create defaultdict with threshold=100
thresholds = defaultdict(partial(make_threshold, 50))
print("\nParameterized default:", thresholds['new_item'])
thresholds['new_item']['threshold'] = 200
print(dict(thresholds))

# Example:

import requests
from collections import defaultdict

# Factory function that fetches user info from an API
def fetch_user_data():
    
    def whatever_you_want(username):
        response = requests.get(f"https://api.example.com/users/{username}")
        if response.status_code == 200:
            return response.json()  # Return user data
        return {"error": "User not found"}
    
    return whatever_you_want

# Create defaultdict with the API-fetching factory
user_profiles = defaultdict(fetch_user_data())

# Access user data dynamically
print(user_profiles["john_doe"])  # Fetches data from API for "john_doe"

