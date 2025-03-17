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

print("\nSalesforce Applications:")

# Calculate total revenue across all accounts
total_revenue = reduce(
    add,
    [
        reduce(
            add,
            [
                reduce(
                    add,
                    map(
                        lambda p: float(p['Revenue']),
                        opp['Products']
                    ),
                    0.0
                )
                for opp in acc['Opportunities']
            ],
            0.0
        )
        for acc in accounts
    ],
    0.0
)
print("Total Revenue:", total_revenue)

# Calculate average satisfaction score
avg_satisfaction = reduce(
    lambda acc, x: {
        'total': acc['total'] + x['Metrics']['Satisfaction'],
        'count': acc['count'] + 1
    },
    accounts,
    {'total': 0, 'count': 0}
)
print("Average Satisfaction:", avg_satisfaction['total'] / avg_satisfaction['count'])