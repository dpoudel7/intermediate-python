# -----------------------------------------------------------------------------
# ASSERTING - assert
# -----------------------------------------------------------------------------


# Basic assertion
def divide(a, b):
    """Simple division with assertion."""
    # Assert that divisor is not zero
    assert b != 0, "Division by zero is not allowed"
    return a / b

# Demonstrate basic assertion
print("Basic assertions:")
try:
    print(divide(10, 2))  # Works fine
    print(divide(10, 0))  # Raises AssertionError
except AssertionError as e:
    print(f"Caught assertion error: {e}")

# Assertions with complex conditions
def process_age(age):
    """Process age with multiple assertions."""
    # Multiple conditions in one assertion
    assert isinstance(age, (int, float)) and 0 <= age <= 150, \
           f"Invalid age: {age}. Must be number between 0 and 150"
    return f"Processing age: {age}"

# Demonstrate complex assertions
print("\nComplex assertions:")
try:
    print(process_age(25))    # Valid
    print(process_age(-5))    # Invalid
except AssertionError as e:
    print(f"Caught assertion error: {e}")
