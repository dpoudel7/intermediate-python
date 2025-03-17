from operator import add, mul
from functools import reduce

opportunities = [
    {'Amount': '1000.00', 'Probability': '90'},
    {'Amount': '5000.00', 'Probability': '60'},
    {'Amount': '2000.00', 'Probability': '75'}
]

print("\nReduce Function Examples:")

# Calculate total pipeline with reduce
total = reduce(
    add,
    map(lambda x: float(x['Amount']), opportunities)
)
print("Total Pipeline (Reduce):", total)

# Calculate weighted pipeline with reduce
weighted_total = reduce(
    add,
    map(
        lambda x: mul(
            float(x['Amount']),
            float(x['Probability']) / 100
        ),
        opportunities
    )
)
print("Weighted Pipeline (Reduce):", weighted_total)