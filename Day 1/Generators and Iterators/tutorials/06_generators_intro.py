# -----------------------------------------------------------------------------
# INTRODUCTION TO GENERATORS
# -----------------------------------------------------------------------------


# Simple function that returns a list
def create_squares_list(n):
    """Regular function that returns all squares at once."""
    squares = []
    for i in range(n):
        squares.append(i ** 2)
    return squares

# Generator function that yields one square at a time
def create_squares_generator(n):
    """Generator that yields squares one at a time."""
    for i in range(n):
        yield i ** 2

# Compare the two approaches
print("Using function (creates all squares at once):")
squares_list = create_squares_list(5)
print(squares_list)

print("\nUsing generator (creates squares on demand):")
squares_gen = create_squares_generator(5)
print(squares_gen)  # Show generator object
for square in squares_gen:
    print(f"Generated: {square}")

# Show that generators are iterators
squares_gen = create_squares_generator(3)
print("\nManual iteration of generator:")
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4

# Show StopIteration
try:
    print(next(squares_gen))
except StopIteration:
    print("Generator exhausted!") 