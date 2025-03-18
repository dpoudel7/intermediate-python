from collections import OrderedDict

# Custom sorting
data = {'banana': 3, 'apple': 1, 'cherry': 2}

# Sort by keys
sorted_by_key = OrderedDict(sorted(data.items()))
print("Sorted by key:", sorted_by_key)

# Sort by values
sorted_by_value = OrderedDict(
    sorted(data.items(), key=lambda x: x[1])
)
print("\nSorted by value:", sorted_by_value)

# Implementing an ordered set
class OrderedSet(OrderedDict):
    def add(self, item):
        self[item] = None
    
    def remove(self, item):
        del self[item]
    
    def __iter__(self):
        return iter(self.keys())
    
    def __str__(self):
        return f"OrderedSet({list(self.keys())})"

# Demonstrate OrderedSet
oset = OrderedSet()
oset.add('red')
oset.add('green')
oset.add('blue')
oset.add('red')
print("\nOrdered Set:", oset)
