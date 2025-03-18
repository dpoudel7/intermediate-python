# -----------------------------------------------------------------------------
# NUMPY ARRAY CREATION METHODS
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~25 minutes

This tutorial covers different ways to create NumPy arrays:
1. From Python sequences
2. Using NumPy functions
3. Reading from files
4. Creating special arrays
5. Random number generation
"""

import numpy as np

# 1. Creating from Python Sequences
print("1. FROM PYTHON SEQUENCES")
print("-" * 50)

# From lists
list_1d = [1, 2, 3, 4]
list_2d = [[1, 2], [3, 4]]

arr_1d = np.array(list_1d)
arr_2d = np.array(list_2d)

print("1D array:", arr_1d)
print("2D array:\n", arr_2d)

# From tuples
tuple_1d = (1, 2, 3, 4)
arr_from_tuple = np.array(tuple_1d)
print("\nFrom tuple:", arr_from_tuple)

# 2. Using NumPy Functions
print("\n2. USING NUMPY FUNCTIONS")
print("-" * 50)

# arange: like Python's range
print("arange:")
print("0 to 9:", np.arange(10))
print("5 to 9:", np.arange(5, 10))
print("0 to 10 step 2:", np.arange(0, 11, 2))

# linspace: evenly spaced numbers over interval
print("\nlinspace:")
print("5 numbers between 0 and 1:", np.linspace(0, 1, 5))
print("4 numbers between -1 and 1:", np.linspace(-1, 1, 4))

# logspace: numbers spaced evenly on log scale
print("\nlogspace:")
print("Powers of 10:", np.logspace(0, 2, 3))  # 10^0 to 10^2

# 3. Special Arrays
print("\n3. SPECIAL ARRAYS")
print("-" * 50)

# Zeros and ones
print("Zeros (1D):", np.zeros(3))
print("Zeros (2D):\n", np.zeros((2, 3)))
print("\nOnes (1D):", np.ones(3))
print("Ones (2D):\n", np.ones((2, 2)))

# Identity and diagonal
print("\nIdentity matrix (3x3):\n", np.eye(3))
print("\nDiagonal array:", np.diag([1, 2, 3]))

# Empty and full
print("\nEmpty (uninitialized):\n", np.empty((2, 2)))
print("Full (filled with 7):\n", np.full((2, 2), 7))

# 4. Random Number Generation
print("\n4. RANDOM NUMBER GENERATION")
print("-" * 50)

# Set seed for reproducibility
np.random.seed(42)

print("Random floats (0 to 1):\n", np.random.rand(2, 3))
print("\nRandom integers (1 to 10):\n", np.random.randint(1, 11, (2, 3)))
print("\nNormal distribution:\n", np.random.normal(0, 1, (2, 3)))
print("\nUniform distribution:\n", np.random.uniform(-1, 1, (2, 3)))

# 5. Creating from Existing Arrays
print("\n5. FROM EXISTING ARRAYS")
print("-" * 50)

original = np.array([[1, 2], [3, 4]])
print("Original array:\n", original)

# Copying arrays
shallow_copy = original.view()  # View
deep_copy = original.copy()     # Copy

print("\nReshaping:")
print(original.reshape(1, 4))  # Reshape to 1x4
print(original.reshape(4, 1))  # Reshape to 4x1

print("\nRepeat elements:")
print("Repeat array:", np.repeat(original, 2))
print("Tile array:", np.tile(original, 2))

"""
Key Takeaways:
1. Multiple ways to create arrays for different needs
2. Some methods create new arrays, others create views
3. Random number generation is useful for simulations
4. Special arrays are helpful for linear algebra
5. Shape manipulation is important for data processing
"""