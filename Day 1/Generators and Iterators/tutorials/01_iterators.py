# A simple list to demonstrate iteration
numbers = [1, 2, 3]

# Get an iterator from the list using iter()
numbers_iterator = iter(numbers)

print("Iterator object:", numbers_iterator)
print("Type of iterator:", type(numbers_iterator))

# We can also get an iterator using __iter__()
another_iterator = numbers.__iter__()

print("\nBoth ways create the same type of iterator:")
print("Using iter():", type(numbers_iterator))
print("Using __iter__():", type(another_iterator))

# Many Python objects are iterable
print("\nOther iterable objects:")
print("String iterator:", type(iter("hello")))
print("Tuple iterator:", type(iter((1, 2, 3))))
