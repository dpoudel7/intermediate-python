from collections import defaultdict

# Basic defaultdict with int factory
word_counts = defaultdict(int) # -> int() -> 0
text = "the quick brown fox jumps over the lazy dog"

# No need for key checking!
for word in text.split():
    word_counts[word] += 1

print("Word counts (defaultdict):", dict(word_counts))

# defaultdict with list factory
categories = defaultdict(list)
sales = [
    ('Electronics', 'Laptop'),
    ('Clothing', 'T-shirt'),
    ('Electronics', 'Phone'),
    ('Books', 'Python Guide'),
    ('Electronics', 'Tablet')
]

# Simple, clean grouping
for category, item in sales:
    categories[category].append(item)

print("\nCategories (defaultdict):", dict(categories))

# Nested defaultdict
# Lambda creates a new defaultdict(int) for each missing key
nested_data = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

# No initialization needed!
region = "West"
city = "San Francisco"
product = "Laptop"
nested_data[region][city][product] += 1

print("\nNested data (defaultdict):", dict(nested_data))