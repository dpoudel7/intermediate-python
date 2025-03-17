from operator import add, mul, itemgetter, attrgetter
from functools import reduce
from typing import List, Dict, Any

# Using add() for addition
total = reduce(add, [1, 2, 3, 4, 5])
print("Sum with operator.add:", total)

# Using mul() for multiplication
product = reduce(mul, [1, 2, 3, 4, 5])
print("Product with operator.mul:", product)

# Sample Salesforce data
opportunities = [
    {'Amount': '1000.00', 'Probability': '90'},
    {'Amount': '5000.00', 'Probability': '60'},
    {'Amount': '2000.00', 'Probability': '75'}
]

# Using itemgetter for dictionary access
get_amount = itemgetter('Amount')
amounts = list(map(
    lambda x: float(get_amount(x)),
    opportunities
))
print("Amounts with itemgetter:", amounts)