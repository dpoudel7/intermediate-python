
# Create an iterator from a list
numbers = [1, 2, 3]
iterator = iter(numbers)

# Using next() to get values one by one
print("Getting values with next():")
print("First value:", next(iterator))
print("Second value:", next(iterator))
print("Third value:", next(iterator))

# Once we've reached the end, next() will raise StopIteration
print("\nTrying to get more values:")
try:
    print("Fourth value:", next(iterator))
except StopIteration:
    print("No more values!")

# We can provide a default value to next()
print("\nUsing default values:")
iterator = iter(numbers)  # Reset iterator
print(next(iterator, "default"))  # 1
print(next(iterator, "default"))  # 2
print(next(iterator, "default"))  # 3
print(next(iterator, "default"))  # "default" 