# -----------------------------------------------------------------------------
# BASIC GENERATOR EXERCISE - SOLUTION
# -----------------------------------------------------------------------------

"""
Exercise: Fibonacci Generator

Create a generator function that yields Fibonacci numbers up to a maximum value.
The Fibonacci sequence starts with 0, 1 and each subsequent number is the sum
of the previous two.

Solution explanation:
1. Initialize first two numbers (0, 1)
2. Yield them first
3. Calculate next number and check against max_value
4. Keep track of last two numbers for next calculation
"""

def fibonacci_up_to(max_value):
    """Generate Fibonacci numbers up to max_value."""
    # Initialize first two numbers
    a, b = 0, 1
    
    # Yield initial values
    yield a
    if max_value >= b:
        yield b
    
    # Generate subsequent numbers
    while True:
        # Calculate next number
        next_num = a + b
        if next_num > max_value:
            break
            
        yield next_num
        # Update last two numbers
        a, b = b, next_num

# Test the generator
print("Fibonacci numbers up to 10:")
for num in fibonacci_up_to(10):
    print(num)

print("\nFibonacci numbers up to 100:")
for num in fibonacci_up_to(100):
    print(num)

# Additional test: small numbers
print("\nFibonacci numbers up to 3:")
for num in fibonacci_up_to(3):
    print(num)

# Additional test: zero or negative
print("\nFibonacci numbers up to 0:")
for num in fibonacci_up_to(0):
    print(num) 