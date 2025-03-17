from operator import add, mul, itemgetter, attrgetter
from functools import reduce
from typing import List, Dict, Any


opportunities = [
    {
        'Name': 'Big Deal',
        'Products': [
            {'Name': 'Product A', 'Quantity': 2, 'Price': 1000.00},
            {'Name': 'Product B', 'Quantity': 1, 'Price': 500.00}
        ]
    },
    {
        'Name': 'Small Deal',
        'Products': [
            {'Name': 'Product C', 'Quantity': 3, 'Price': 200.00}
        ]
    }
]

# Function composition with operator functions
get_products = itemgetter('Products')
get_price = itemgetter('Price')
get_quantity = itemgetter('Quantity')

def calculate_product_total(product):
    return mul(float(get_quantity(product)), float(get_price(product)))

# Calculate total value for each opportunity
opportunity_values = list(map(
    lambda opp: reduce(
        add,
        map(calculate_product_total, get_products(opp))
    ),
    opportunities
))
print("\nOpportunity Values:", opportunity_values)

# Error handling with operator functions
def safe_multiply(x, y):
    try:
        return mul(float(x), float(y))
    except (ValueError, TypeError):
        return 0.0

# Safe calculations with error handling
safe_values = list(map(
    lambda opp: reduce(
        add,
        map(
            lambda p: safe_multiply(get_quantity(p), get_price(p)),
            get_products(opp)
        )
    ),
    opportunities
))
print("Safe Values:", safe_values)