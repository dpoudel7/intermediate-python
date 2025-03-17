
from collections import defaultdict

# Create a simple defaultdict
d = defaultdict(list)

# Show what the class looks like
print(f"defaultdict is a {type(defaultdict)}")
print(f"defaultdict base classes: {defaultdict.__bases__}")

# Demonstrate the __missing__ method behavior
print("\nAccessing a missing key:")
print(f"Before access: {dict(d)}")
d['new_key'].append(1)  # This triggers __missing__
print(f"After access: {dict(d)}")

# Show how the factory function is used
print("\nFactory function behavior:")
numbers = defaultdict(int)
print(f"Default value for missing key: {numbers['not_there']}")

# Custom factory function
def custom_factory():
    return "Custom default"

custom_dict = defaultdict(custom_factory)
print(f"Custom default value: {custom_dict['missing']}")
print(dict(custom_dict))

# Show memory usage comparison
import sys
regular_dict = {}
default_dict = defaultdict(list)

print("\nMemory comparison:")
print(f"Regular dict size: {sys.getsizeof(regular_dict)} bytes")
print(f"defaultdict size: {sys.getsizeof(default_dict)} bytes")