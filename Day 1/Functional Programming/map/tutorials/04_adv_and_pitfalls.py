data = [1, 2, 3, 4, 5]

# Iterator consumption
squared = map(lambda x: x**2, data)
print("First pass:", list(squared))
print("Second pass (empty):", list(squared))  # Iterator is exhausted

# Memory efficiency with large datasets
def process_large_dataset():
    # map() is memory efficient for large datasets
    numbers = range(1000000)
    squares = map(lambda x: x**2, numbers)
    # Only one number is processed at a time
    for square in squares:
        if square > 100:
            break

# Error handling patterns
def safe_transform(func):
    def wrapper(item):
        try:
            return func(item)
        except Exception as e:
            return None
    return wrapper

# Using safe transform
data_with_errors = ['1', '2', 'not_a_number', '4']
safe_int = safe_transform(int)

results = list(map(safe_int, data_with_errors))

print("Results:", results)
