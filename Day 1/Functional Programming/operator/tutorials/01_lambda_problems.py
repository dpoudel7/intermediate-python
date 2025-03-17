from operator import add, mul, itemgetter, attrgetter
from functools import reduce
from typing import List, Dict, Any


# Sample Salesforce opportunity data
opportunities = [
    {'Amount': '1000.00', 'Probability': '90'},
    {'Amount': '5000.00', 'Probability': '60'},
    {'Amount': '2000.00', 'Probability': '75'}
]

# Using lambda for simple addition
print("\nVerbose Lambda Examples:")

# Lambda for addition
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print("Sum with lambda:", total)

# Lambda for multiplication
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print("Product with lambda:", product)

# Lambda for dictionary key access
amounts = list(map(
    lambda opp: float(opp['Amount']),
    opportunities
))
print("Amounts with lambda:", amounts)