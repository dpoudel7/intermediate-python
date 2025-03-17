# Memory and performance characteristics
import sys
from collections import OrderedDict

# Compare memory usage
regular_dict = dict.fromkeys('abcde')
ordered_dict = OrderedDict.fromkeys('abcde')

print("Memory Usage Comparison:")
print(f"Regular dict: {sys.getsizeof(regular_dict)} bytes")
print(f"OrderedDict: {sys.getsizeof(ordered_dict)} bytes")

# Demonstrate internal order tracking
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print("\nInternal Order Representation:")
print(f"Keys in order: {list(od.keys())}")
print(f"Items in order: {list(od.items())}")

# Show order preservation during operations
od.pop('b')
od['b'] = 2  # Re-insert 'b'
print("\nOrder after pop and re-insert:")
print(f"Keys: {list(od.keys())}")

# Demonstrate memory overhead with size
sizes = [10, 100, 1000]
for size in sizes:
    d = dict(zip(range(size), range(size)))
    od = OrderedDict(d)
    print(f"\nSize {size}:")
    print(f"Regular dict: {sys.getsizeof(d)} bytes")
    print(f"OrderedDict: {sys.getsizeof(od)} bytes")