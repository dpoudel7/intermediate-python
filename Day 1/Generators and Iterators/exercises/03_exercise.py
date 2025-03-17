# -----------------------------------------------------------------------------
# BASIC GENERATOR EXERCISE
# -----------------------------------------------------------------------------

"""
Exercise: Fibonacci Generator

Create a generator function that yields Fibonacci numbers up to a maximum value.
The Fibonacci sequence starts with 0, 1 and each subsequent number is the sum
of the previous two.

Example:
fib(10) should yield: 0, 1, 1, 2, 3, 5, 8
(stops at 8 because next number would be 13 > 10)

Tasks:
1. Complete the fibonacci_up_to generator function
2. Use yield to generate numbers one at a time
3. Stop when the next number would exceed max_value
"""

def fibonacci_up_to(max_value):
    """Generate Fibonacci numbers up to max_value."""
    # TODO: Initialize first two Fibonacci numbers
    
    # TODO: Yield initial values
    
    # TODO: Generate subsequent Fibonacci numbers
    # Hint: Keep track of the last two numbers
    # Hint: Use yield to return numbers one at a time
    pass

# Test the generator
print("Fibonacci numbers up to 10:")
for num in fibonacci_up_to(10):
    print(num)

print("\nFibonacci numbers up to 100:")
for num in fibonacci_up_to(100):
    print(num)

# Should print:
# Fibonacci numbers up to 10:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 
# Fibonacci numbers up to 100:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89 