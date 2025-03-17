config = {}
config['database'] = 'mysql'
config['host'] = 'localhost'
config['port'] = 3306
config['username'] = 'admin'

print("Regular dict (modern Python preserves order):", config)

# But OrderedDict provides explicit ordering guarantees and features
from collections import OrderedDict
ordered_config = OrderedDict()
ordered_config['database'] = 'mysql'
ordered_config['host'] = 'localhost'
ordered_config['port'] = 3306
ordered_config['username'] = 'admin'

print("\nOrderedDict with explicit ordering:", ordered_config)

# Example: Dictionary equality comparison differences
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print("\nRegular dict comparison (order doesn't matter):")
print(f"dict1 == dict2: {dict1 == dict2}")

odict1 = OrderedDict([('a', 1), ('b', 2)])
odict2 = OrderedDict([('b', 2), ('a', 1)])
print("\nOrderedDict comparison (order matters):")
print(f"odict1 == odict2: {odict1 == odict2}")