# -----------------------------------------------------------------------------
# CONVERTING PYTHON FUNCTIONS TO NUMPY
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~25 minutes

This tutorial demonstrates:
1. Converting regular Python functions to NumPy
2. Creating custom universal functions (ufuncs)
3. Vectorizing functions
4. Performance comparisons
"""

import numpy as np
from numpy import frompyfunc
import time

# 1. Basic Function Conversion
print("1. BASIC FUNCTION CONVERSION")
print("-" * 50)

# Regular Python function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Test with single value
print("Single value conversion:")
print(f"0°C = {celsius_to_fahrenheit(0)}°F")

# Try with array (won't work efficiently)
temperatures = np.array([-40, 0, 37, 100])
print("\nTemperatures in Celsius:", temperatures)

# Method 1: Using numpy.vectorize
vectorized_convert = np.vectorize(celsius_to_fahrenheit)
print("Using vectorize:", vectorized_convert(temperatures))

# Method 2: Using frompyfunc
ufunc_convert = frompyfunc(celsius_to_fahrenheit, 1, 1)
print("Using frompyfunc:", ufunc_convert(temperatures))

# Method 3: Rewriting for NumPy (most efficient)
def celsius_to_fahrenheit_numpy(celsius_array):
    return (celsius_array * 9/5) + 32

print("Using NumPy operations:", celsius_to_fahrenheit_numpy(temperatures))

# 2. More Complex Examples
print("\n2. MORE COMPLEX EXAMPLES")
print("-" * 50)

# Example 1: Calculate circle areas
def circle_area_python(radius):
    return 3.14159 * radius * radius

# Convert to NumPy function
def circle_area_numpy(radius_array):
    return np.pi * np.square(radius_array)

radii = np.array([1, 2, 3, 4, 5])
print("Circle areas:")
print("Using vectorize:", np.vectorize(circle_area_python)(radii))
print("Using NumPy:", circle_area_numpy(radii))

# Example 2: Custom grading function
def assign_grade_python(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

# NumPy version using where
def assign_grade_numpy(scores):
    grades = np.full_like(scores, 'F', dtype=str)
    grades = np.where(scores >= 70, 'C', grades)
    grades = np.where(scores >= 80, 'B', grades)
    grades = np.where(scores >= 90, 'A', grades)
    return grades

scores = np.array([85, 95, 65, 75, 90])
print("\nGrades:")
vectorized_grade = np.vectorize(assign_grade_python)
print("Using vectorize:", vectorized_grade(scores))
print("Using NumPy:", assign_grade_numpy(scores))

# 3. Creating Custom Universal Functions
print("\n3. CREATING CUSTOM UNIVERSAL FUNCTIONS")
print("-" * 50)

# Example: Custom sigmoid function
def sigmoid_python(x):
    return 1 / (1 + np.exp(-x))

# Convert to ufunc
sigmoid_ufunc = frompyfunc(sigmoid_python, 1, 1)

# NumPy optimized version
def sigmoid_numpy(x):
    return 1 / (1 + np.exp(-x))

# Test data
x = np.array([-2, -1, 0, 1, 2])
print("Sigmoid function results:")
print("Using ufunc:", sigmoid_ufunc(x))
print("Using NumPy:", sigmoid_numpy(x))

# 4. Performance Comparison
print("\n4. PERFORMANCE COMPARISON")
print("-" * 50)

# Create large dataset
size = 1_000_000
data = np.random.random(size) * 10 - 5  # Values between -5 and 5

# Test different implementations
def measure_time(func, data):
    start = time.time()
    result = func(data)
    return time.time() - start

# Regular Python (using list comprehension)
start = time.time()
python_result = [sigmoid_python(x) for x in data]
python_time = time.time() - start

# Vectorized function
vectorized_time = measure_time(np.vectorize(sigmoid_python), data)

# Universal function
ufunc_time = measure_time(sigmoid_ufunc, data)

# NumPy optimized
numpy_time = measure_time(sigmoid_numpy, data)

print("Time comparison for sigmoid calculation:")
print(f"Python list comprehension: {python_time:.6f} seconds")
print(f"Vectorized function: {vectorized_time:.6f} seconds")
print(f"Universal function: {ufunc_time:.6f} seconds")
print(f"NumPy optimized: {numpy_time:.6f} seconds")

# 5. Best Practices
print("\n5. BEST PRACTICES")
print("-" * 50)

print("""
When converting Python functions to NumPy:
1. Use built-in NumPy functions when available
2. Avoid explicit loops
3. Use broadcasting instead of iteration
4. Prefer array operations over element-wise operations
5. Use np.where for conditional operations
6. Profile different approaches for your specific case
""")

"""
Key Takeaways:
1. Multiple ways to convert Python functions to work with NumPy arrays
2. np.vectorize is convenient but not always efficient
3. Custom ufuncs are good for simple mathematical operations
4. Rewriting functions to use NumPy operations is most efficient
5. Always profile performance for your specific use case
""" 