# Traditional approach using regular dictionaries
# Example: Counting word frequencies in text
text = "the quick brown fox jumps over the lazy dog"
word_counts = {}

# Without defaultdict - need explicit key checking
for word in text.split():
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

print("Word counts (traditional):", word_counts)

# Example: Grouping items by category
sales = [
    ('Electronics', 'Laptop'),
    ('Clothing', 'T-shirt'),
    ('Electronics', 'Phone'),
    ('Books', 'Python Guide'),
    ('Electronics', 'Tablet')
]

# Without defaultdict - need to initialize lists
categories = {}
for category, item in sales:
    if category not in categories:
        categories[category] = []
    categories[category].append(item)

print("\nCategories (traditional):", categories)

# Example: Nested dictionaries
# Without defaultdict - complex initialization
nested_data = {}
region = "West"
city = "San Francisco"
product = "Laptop"

# Verbose nested checks
if region not in nested_data:
    nested_data[region] = {}
if city not in nested_data[region]:
    nested_data[region][city] = {}
if product not in nested_data[region][city]:
    nested_data[region][city][product] = 0
nested_data[region][city][product] += 1

print("\nNested data (traditional):", nested_data)