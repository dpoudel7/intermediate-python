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
