# -----------------------------------------------------------------------------
# NUMPY ARRAY OPERATIONS
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~30 minutes

This tutorial focuses on operations we can perform with NumPy arrays:
1. Basic arithmetic operations
2. Mathematical functions
3. Comparison operations
4. Logical operations
5. Matrix operations
"""

import numpy as np

# 1. Basic Arithmetic Operations
print("1. BASIC ARITHMETIC")
print("-" * 50)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)
print("\nElement-wise operations:")
print("Addition:", a + b)        # [5, 7, 9]
print("Subtraction:", a - b)     # [-3, -3, -3]
print("Multiplication:", a * b)  # [4, 10, 18]
print("Division:", b / a)        # [4.0, 2.5, 2.0]
print("Power:", a ** 2)          # [1, 4, 9]
print("Modulus:", b % a)         # [0, 1, 0]

# 2. Mathematical Functions
print("\n2. MATHEMATICAL FUNCTIONS")
print("-" * 50)

x = np.array([0, 30, 45, 60, 90])
angles = x * np.pi / 180  # Convert to radians

print("Original angles (degrees):", x)
print("\nTrigonometric functions:")
print("Sin:", np.sin(angles))
print("Cos:", np.cos(angles))
print("Tan:", np.tan(angles))

numbers = np.array([1, 4, 9, 16, 25])
print("\nOther math functions:")
print("Square root:", np.sqrt(numbers))
print("Exponential (e^x):", np.exp(a))
print("Natural log:", np.log(numbers))
print("Log base 10:", np.log10(numbers))

# 3. Comparison Operations
print("\n3. COMPARISON OPERATIONS")
print("-" * 50)

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 3, 3, 2, 5])

print("Array a:", a)
print("Array b:", b)
print("\nComparisons (return boolean arrays):")
print("Equal:", a == b)
print("Not equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater or equal:", a >= b)
print("Less or equal:", a <= b)

# 4. Logical Operations
print("\n4. LOGICAL OPERATIONS")
print("-" * 50)

condition1 = a > 2
condition2 = b > 2

print("Condition1 (a > 2):", condition1)
print("Condition2 (b > 2):", condition2)
print("\nLogical operations:")
print("AND:", np.logical_and(condition1, condition2))
print("OR:", np.logical_or(condition1, condition2))
print("NOT:", np.logical_not(condition1))
print("XOR:", np.logical_xor(condition1, condition2))

# 5. Matrix Operations
print("\n5. MATRIX OPERATIONS")
print("-" * 50)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\nMatrix operations:")
print("Matrix multiplication (dot):\n", np.dot(A, B))
print("Matrix multiplication (@):\n", A @ B)  # Python 3.5+
print("Element-wise multiplication:\n", A * B)
print("Matrix transpose:\n", A.T)
print("Matrix inverse:\n", np.linalg.inv(A))
print("Matrix determinant:", np.linalg.det(A))

# 6. Aggregate Operations
print("\n6. AGGREGATE OPERATIONS")
print("-" * 50)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Array:\n", arr)
print("\nAggregate operations:")
print("Sum of all elements:", arr.sum())
print("Product of all elements:", arr.prod())
print("Mean of all elements:", arr.mean())
print("Standard deviation:", arr.std())
print("Minimum element:", arr.min())
print("Maximum element:", arr.max())

print("\nAxis operations:")
print("Row sums:", arr.sum(axis=1))
print("Column sums:", arr.sum(axis=0))

"""
Key Takeaways:
1. NumPy operations are element-wise by default
2. Operations are much faster than Python loops
3. Broadcasting rules apply to operations
4. Matrix operations are available for 2D arrays
5. Most operations can work along specified axes
"""
