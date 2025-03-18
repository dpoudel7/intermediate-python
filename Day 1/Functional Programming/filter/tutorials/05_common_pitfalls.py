# -----------------------------------------------------------------------------
# COMMON PITFALLS WHEN USING FILTER
# -----------------------------------------------------------------------------

items = [
    {'id': 1, 'status': 'active', 'processed': False},
    {'id': 2, 'status': 'inactive', 'processed': False},
    {'id': 3, 'status': 'active', 'processed': False}
]

print("Original items:", items)

# BAD: Modifying while filtering
active_items = list(filter(
    lambda x: x.update({'processed': True}) or x['status'] == 'active',
    items
))

print("After bad filter (all items modified!):", items)
print("Filtered items:", active_items)

# GOOD: Separate the operations
items = [
    {'id': 1, 'status': 'active', 'processed': False},
    {'id': 2, 'status': 'inactive', 'processed': False},
    {'id': 3, 'status': 'active', 'processed': False}
]

def is_active(item):
    return item['status'] == 'active'

active_items = list(filter(is_active, items))
processed_items = [dict(item, processed=True) for item in active_items]

print("\nBetter approach results:")
print("Original items unchanged:", items)
print("Processed active items:", processed_items)


