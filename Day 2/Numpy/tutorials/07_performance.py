# -----------------------------------------------------------------------------
# NUMPY PERFORMANCE OPTIMIZATION
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~35 minutes

This tutorial covers:
1. Memory layout and access patterns
2. Choosing the right data type
3. Avoiding copies
4. Profiling NumPy operations
5. Best practices for performance
"""

import numpy as np
import time
import sys

# 1. Memory Layout and Access Patterns
print("1. MEMORY LAYOUT AND ACCESS PATTERNS")
print("-" * 50)

# Create sample arrays
size = 1000
arr_c = np.zeros((size, size), order='C')  # Row-major (C-style)
arr_f = np.zeros((size, size), order='F')  # Column-major (Fortran-style)

# Compare row vs column access
def access_by_rows(arr):
    start = time.time()
    for i in range(arr.shape[0]):
        row_sum = arr[i, :].sum()
    return time.time() - start

def access_by_cols(arr):
    start = time.time()
    for j in range(arr.shape[1]):
        col_sum = arr[:, j].sum()
    return time.time() - start

print("Row access time (C-order):", access_by_rows(arr_c))
print("Row access time (F-order):", access_by_rows(arr_f))
print("Column access time (C-order):", access_by_cols(arr_c))
print("Column access time (F-order):", access_by_cols(arr_f))

# 2. Data Type Impact
print("\n2. DATA TYPE IMPACT")
print("-" * 50)

# Create arrays with different dtypes
size = 1_000_000
data_float64 = np.random.random(size)  # Default float64
data_float32 = data_float64.astype(np.float32)
data_int64 = np.random.randint(0, 100, size)
data_int32 = data_int64.astype(np.int32)

# Compare memory usage
print("Memory usage per array:")
print(f"float64: {data_float64.nbytes / 1024:.2f} KB")
print(f"float32: {data_float32.nbytes / 1024:.2f} KB")
print(f"int64: {data_int64.nbytes / 1024:.2f} KB")
print(f"int32: {data_int32.nbytes / 1024:.2f} KB")

# Compare computation speed
def measure_computation(arr):
    start = time.time()
    for _ in range(100):
        result = np.sin(arr) * np.cos(arr)
    return time.time() - start

print("\nComputation time:")
print(f"float64: {measure_computation(data_float64):.4f} seconds")
print(f"float32: {measure_computation(data_float32):.4f} seconds")

# 3. Avoiding Copies
print("\n3. AVOIDING COPIES")
print("-" * 50)

# Example of view vs copy
arr = np.arange(1_000_000)

# Using view
start = time.time()
view = arr[::2]  # Creates a view
view_time = time.time() - start
print(f"View creation time: {view_time:.6f} seconds")

# Using copy
start = time.time()
copy = arr[::2].copy()  # Creates a copy
copy_time = time.time() - start
print(f"Copy creation time: {copy_time:.6f} seconds")

# Check if array owns its data
print("\nMemory ownership:")
print("View owns data:", view.flags.owndata)
print("Copy owns data:", copy.flags.owndata)

# 4. Efficient Operations
print("\n4. EFFICIENT OPERATIONS")
print("-" * 50)

# Compare different ways to calculate mean
data = np.random.random(1_000_000)

# Method 1: Python loop
start = time.time()
mean1 = sum(data) / len(data)
time1 = time.time() - start

# Method 2: NumPy mean
start = time.time()
mean2 = data.mean()
time2 = time.time() - start

print(f"Python loop time: {time1:.6f} seconds")
print(f"NumPy mean time: {time2:.6f} seconds")

# 5. Best Practices
print("\n5. BEST PRACTICES")
print("-" * 50)

# Example 1: Pre-allocation vs append
size = 1000
times = []

# Bad practice: Growing array
start = time.time()
arr = np.array([])
for i in range(size):
    arr = np.append(arr, i)
times.append(time.time() - start)
print(f"Growing array time: {times[0]:.6f} seconds")

# Good practice: Pre-allocation
start = time.time()
arr = np.zeros(size)
for i in range(size):
    arr[i] = i
times.append(time.time() - start)
print(f"Pre-allocated time: {times[1]:.6f} seconds")

# Example 2: Vectorized operations
numbers = np.arange(1_000_000)

# Bad practice: Python loop
start = time.time()
result1 = []
for num in numbers:
    if num % 2 == 0:
        result1.append(num ** 2)
time1 = time.time() - start

# Good practice: Vectorized operation
start = time.time()
result2 = numbers[numbers % 2 == 0] ** 2
time2 = time.time() - start

print(f"\nLoop time: {time1:.6f} seconds")
print(f"Vectorized time: {time2:.6f} seconds")

"""
Key Takeaways:
1. Memory layout affects performance
2. Choose appropriate data types
3. Avoid unnecessary copies
4. Use vectorized operations
5. Pre-allocate arrays when possible
6. Profile code to identify bottlenecks
""" 