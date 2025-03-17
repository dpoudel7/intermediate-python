from collections import OrderedDict

# Creating OrderedDict instances
# Method 1: From a sequence of pairs
pairs = [('a', 1), ('b', 2), ('c', 3)]
ordered_dict1 = OrderedDict(pairs)
print("From pairs:", ordered_dict1)

# Method 2: From keyword arguments
ordered_dict2 = OrderedDict(x=1, y=2, z=3)
print("\nFrom kwargs:", ordered_dict2)

# Method 3: Updating incrementally
ordered_dict3 = OrderedDict()
ordered_dict3['first'] = 1
ordered_dict3['second'] = 2
ordered_dict3['third'] = 3
print("\nBuilt incrementally:", ordered_dict3)

# Demonstrating order sensitivity
ordered_dict3.move_to_end('first')  # Move to end
print("\nAfter moving 'first' to end:", ordered_dict3)

ordered_dict3.move_to_end('second', last=False)  # Move to beginning
print("After moving 'second' to start:", ordered_dict3)

# Demonstrate order preservation during updates
ordered_dict3.update({'fourth': 4, 'fifth': 5})
print("\nAfter update:", ordered_dict3)