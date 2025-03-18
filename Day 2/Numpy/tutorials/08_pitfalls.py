# -----------------------------------------------------------------------------
# NUMPY COMMON PITFALLS AND GOTCHAS
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~25 minutes

This tutorial covers common mistakes and pitfalls when using NumPy:
1. Copy vs View confusion
2. Broadcasting mistakes
3. Memory issues
4. Type conversion problems
5. Shape mismatch errors
"""

import numpy as np

# 1. Copy vs View Confusion
print("1. COPY VS VIEW CONFUSION")
print("-" * 50)

# Pitfall 1: Modifying views affects original array
original = np.array([1, 2, 3, 4, 5])
view = original[1:4]  # Creates a view
print("Original array:", original)
print("View:", view)

view[0] = 10  # Modifies original array too!
print("\nAfter modifying view:")
print("Original array:", original)
print("View:", view)

# Solution: Use copy when independent array is needed
copy = original[1:4].copy()
copy[0] = 20  # Doesn't affect original
print("\nAfter modifying copy:")
print("Original array:", original)
print("Copy:", copy)

# 2. Broadcasting Mistakes
print("\n2. BROADCASTING MISTAKES")
print("-" * 50)

# Pitfall 2: Unexpected broadcasting
a = np.array([[1, 2, 3],
              [4, 5, 6]])  # Shape: (2, 3)

try:
    # This will fail
    b = np.array([1, 2])  # Shape: (2,)
    result = a + b
except ValueError as e:
    print("Error:", e)

# Solution: Reshape array for intended broadcasting
b_correct = b.reshape(-1, 1)  # Shape: (2, 1)
result = a + b_correct
print("\nCorrect broadcasting result:\n", result)

# 3. Memory Issues
print("\n3. MEMORY ISSUES")
print("-" * 50)

# Pitfall 3: Creating large temporary arrays
size = 1000
data = np.random.random((size, size))

# Bad practice: Creates temporary large arrays
def inefficient_calculation(arr):
    temp1 = arr * arr  # Creates temporary
    temp2 = temp1 * arr  # Creates another temporary
    return temp2.sum()

# Better practice: Avoid temporary arrays
def efficient_calculation(arr):
    return (arr ** 3).sum()

# 4. Type Conversion Problems
print("\n4. TYPE CONVERSION PROBLEMS")
print("-" * 50)

# Pitfall 4: Unexpected type conversion
integers = np.array([1, 2, 3, 4])
floats = np.array([1.5, 2.5, 3.5, 4.5])

# Integer division
print("Integer division:", integers / 2)  # Converts to float
print("Floor division:", integers // 2)   # Stays integer

# Mixed type operations
mixed = integers + floats
print("\nMixed type result:", mixed)
print("Result dtype:", mixed.dtype)

# 5. Shape Mismatch Errors
print("\n5. SHAPE MISMATCH ERRORS")
print("-" * 50)

# Pitfall 5: Reshape confusion
arr = np.array([1, 2, 3, 4, 5, 6])

try:
    # This will fail
    reshaped = arr.reshape(4, 2)
except ValueError as e:
    print("Reshape error:", e)

# Solution: Check dimensions first
total_elements = arr.size
print("\nTotal elements:", total_elements)
print("Possible reshape dimensions:")
for i in range(1, total_elements + 1):
    if total_elements % i == 0:
        print(f"({i}, {total_elements//i})")

# Correct reshape
correct_reshape = arr.reshape(2, 3)
print("\nCorrect reshape:\n", correct_reshape)

# 6. Boolean Indexing Gotchas
print("\n6. BOOLEAN INDEXING GOTCHAS")
print("-" * 50)

# Pitfall 6: Chaining comparisons
data = np.array([1, 2, 3, 4, 5])

# Wrong way (Python chaining)
print("Wrong way:", 1 <= data <= 3)  # This doesn't work as expected

# Correct way (NumPy logical operators)
print("Correct way:", (data >= 1) & (data <= 3))

# 7. NaN Handling
print("\n7. NaN HANDLING")
print("-" * 50)

# Pitfall 7: NaN propagation
data = np.array([1, 2, np.nan, 4, 5])
print("Array with NaN:", data)
print("Mean (with NaN):", data.mean())
print("Mean (ignoring NaN):", np.nanmean(data))

"""
Key Takeaways:
1. Always be clear about copy vs view
2. Check array shapes before broadcasting
3. Avoid creating unnecessary temporary arrays
4. Be aware of type conversion rules
5. Verify dimensions before reshaping
6. Use NumPy logical operators for boolean indexing
7. Handle NaN values appropriately
""" 