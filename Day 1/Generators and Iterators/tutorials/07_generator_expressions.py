# -----------------------------------------------------------------------------
# GENERATOR EXPRESSIONS
# -----------------------------------------------------------------------------


# List comprehension vs Generator expression
import sys

# List comprehension (creates all values immediately)
squares_list = [x**2 for x in range(10)]
print("List comprehension:")
print(f"Result: {squares_list}")
print(f"Size in memory: {sys.getsizeof(squares_list)} bytes")

# Generator expression (creates values on demand)
squares_gen = (x**2 for x in range(10))
print("\nGenerator expression:")
print(f"Object: {squares_gen}")
print(f"Size in memory: {sys.getsizeof(squares_gen)} bytes")

# Using generator expressions in functions
print("\nSum of squares using generator expression:")
total = sum(x**2 for x in range(10))  # No need for extra parentheses
print(total)

# Chaining generator expressions
numbers = (x for x in range(10))
squares = (x**2 for x in numbers)
even_squares = (x for x in squares if x % 2 == 0)

print("\nChained generator expressions:")
for num in even_squares:
    print(num)

# Memory efficiency with large sequences
def compare_memory_usage(n):
    list_comp = [i**2 for i in range(n)]
    gen_exp = (i**2 for i in range(n))
    
    print(f"\nMemory comparison for {n} numbers:")
    print(f"List comprehension: {sys.getsizeof(list_comp)} bytes")
    print(f"Generator expression: {sys.getsizeof(gen_exp)} bytes")

compare_memory_usage(1000000) 