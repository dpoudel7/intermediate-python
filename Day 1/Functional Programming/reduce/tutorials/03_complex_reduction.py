from operator import add
from functools import reduce

accounts = [
    {
        'Name': 'Acme Corp',
        'Opportunities': [
            {
                'Name': 'Big Deal',
                'Products': [
                    {'Name': 'Product A', 'Revenue': '10000.00', 'Costs': '5000.00'},
                    {'Name': 'Product B', 'Revenue': '5000.00', 'Costs': '2500.00'}
                ]
            }
        ],
        'Metrics': {'Satisfaction': 4.5, 'Loyalty': 3}
    },
    {
        'Name': 'TechCo',
        'Opportunities': [
            {
                'Name': 'Medium Deal',
                'Products': [
                    {'Name': 'Product C', 'Revenue': '7500.00', 'Costs': '3000.00'}
                ]
            }
        ],
        'Metrics': {'Satisfaction': 4.8, 'Loyalty': 4}
    }
]
