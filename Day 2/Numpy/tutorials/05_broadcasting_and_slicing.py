# -----------------------------------------------------------------------------
# NUMPY BROADCASTING AND SLICING
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~30 minutes

This tutorial covers:
1. Basic array indexing and slicing
2. Advanced indexing techniques
3. Broadcasting rules and examples
4. Common broadcasting pitfalls
"""

import numpy as np

# 1. Basic Array Indexing and Slicing
print("1. BASIC INDEXING AND SLICING")
print("-" * 50)

# Create a sample array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original array:", arr)

# Basic indexing
print("\nBasic indexing:")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Third element:", arr[2])

# Basic slicing [start:stop:step]
print("\nBasic slicing:")
print("First three elements:", arr[:3])
print("Last three elements:", arr[-3:])
print("Every second element:", arr[::2])
print("Reverse array:", arr[::-1])

# 2. Multi-dimensional Slicing
print("\n2. MULTI-DIMENSIONAL SLICING")
print("-" * 50)

# Create a 2D array
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("2D array:\n", arr_2d)

print("\nSlicing 2D arrays:")
print("First row:", arr_2d[0])
print("First column:\n", arr_2d[:, 0])
print("2x2 subarray:\n", arr_2d[:2, :2])
print("Every second element of every row:\n", arr_2d[:, ::2])

# 3. Advanced Indexing
print("\n3. ADVANCED INDEXING")
print("-" * 50)

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5])
bool_idx = arr > 3
print("Array:", arr)
print("Boolean mask:", bool_idx)
print("Elements > 3:", arr[bool_idx])

# Integer indexing
indices = [0, 2, 4]
print("\nInteger indexing:", arr[indices])

# Combining boolean and integer indexing
print("Even numbers:", arr[arr % 2 == 0])

# 4. Broadcasting Rules
print("\n4. BROADCASTING RULES")
print("-" * 50)

"""
Broadcasting Rules:
1. Arrays must have same number of dimensions, or
2. One array can be 1-dimensional
3. Size of each dimension must be equal, or
4. One of the dimensions must be 1
"""

# Example 1: Scalar broadcasting
arr = np.array([1, 2, 3])
print("Array:", arr)
print("Add scalar:", arr + 5)  # 5 is broadcast to [5, 5, 5]

# Example 2: Array broadcasting
a = np.array([[1, 2, 3],
              [4, 5, 6]])  # Shape: (2, 3)
b = np.array([10, 20, 30])  # Shape: (3,)
print("\nArray a:\n", a)
print("Array b:", b)
print("a + b:\n", a + b)  # b is broadcast to shape (2, 3)

# Example 3: Broadcasting with different dimensions
x = np.array([[1], [2], [3]])  # Shape: (3, 1)
y = np.array([4, 5, 6])        # Shape: (3,)
print("\nArray x:\n", x)
print("Array y:", y)
print("x + y:\n", x + y)  # Both arrays are broadcast

# 5. Common Broadcasting Pitfalls
print("\n5. BROADCASTING PITFALLS")
print("-" * 50)

try:
    # Incompatible shapes
    a = np.array([[1, 2], [3, 4]])  # Shape: (2, 2)
    b = np.array([1, 2, 3])         # Shape: (3,)
    result = a + b
except ValueError as e:
    print("Error:", e)

# Correct way
b_correct = np.array([1, 2])  # Shape: (2,)
print("\nCorrect broadcasting:")
print("a + b_correct:\n", a + b_correct)

"""
Key Takeaways:
1. Slicing follows [start:stop:step] pattern
2. Multi-dimensional slicing uses comma-separated indices
3. Broadcasting makes array operations more convenient
4. Always check array shapes before broadcasting
5. Use boolean indexing for filtering data
""" 