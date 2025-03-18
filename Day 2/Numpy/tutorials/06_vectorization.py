# -----------------------------------------------------------------------------
# NUMPY VECTORIZATION
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~30 minutes

This tutorial demonstrates:
1. What is vectorization
2. Comparing loops vs vectorized operations
3. Real-world examples
4. Performance measurements
"""

import numpy as np
import time

# 1. Understanding Vectorization
print("1. UNDERSTANDING VECTORIZATION")
print("-" * 50)

# Example: Calculate square of numbers
numbers = np.array([1, 2, 3, 4, 5])

print("Original array:", numbers)
print("Using vectorization:", numbers ** 2)

# Compare with Python loop
print("\nPython loop vs Numpy vectorization:")
python_squares = []
for num in numbers:
    python_squares.append(num ** 2)
print("Using Python loop:", python_squares)

# 2. Performance Comparison
print("\n2. PERFORMANCE COMPARISON")
print("-" * 50)

# Create large arrays for testing
size = 1_000_000
data = np.random.random(size)

# Using Python loop
start_time = time.time()
python_result = []
for x in data:
    python_result.append(np.sin(x) * np.cos(x))
python_time = time.time() - start_time
print(f"Python loop time: {python_time:.4f} seconds")

# Using NumPy vectorization
start_time = time.time()
numpy_result = np.sin(data) * np.cos(data)
numpy_time = time.time() - start_time
print(f"NumPy vectorization time: {numpy_time:.4f} seconds")

print(f"Speedup factor: {python_time/numpy_time:.1f}x")

# 3. Real-world Examples
print("\n3. REAL-WORLD EXAMPLES")
print("-" * 50)

# Example 1: Data normalization
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original data:", data)

# Normalize to range [0, 1]
normalized = (data - data.min()) / (data.max() - data.min())
print("Normalized data:", normalized)

# Example 2: Distance calculation
points = np.random.rand(5, 2)  # 5 points in 2D
print("\n2D Points:\n", points)

# Calculate distances between all points
distances = np.sqrt(((points[:, np.newaxis] - points) ** 2).sum(axis=2))
print("\nDistance matrix:\n", distances)

# Example 3: Image processing
print("\nImage processing example:")
image = np.random.randint(0, 256, (4, 4))  # Small example image
print("Original image:\n", image)

# Apply threshold
threshold = 128
binary_image = image > threshold
print("\nBinary image (threshold=128):\n", binary_image)

# 4. Common Vectorization Patterns
print("\n4. COMMON VECTORIZATION PATTERNS")
print("-" * 50)

# Pattern 1: Element-wise operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Element-wise multiplication:", arr1 * arr2)

# Pattern 2: Broadcasting with scalars
temperatures = np.array([0, 15, 30, 45])
print("\nCelsius:", temperatures)
print("Fahrenheit:", temperatures * 9/5 + 32)

# Pattern 3: Boolean masking
data = np.array([1, -2, 3, -4, 5])
print("\nOriginal data:", data)
print("Positive values:", data[data > 0])
print("Replace negatives with zero:", np.where(data < 0, 0, data))

# Pattern 4: Reduction operations
print("\nReduction operations:")
print("Sum:", data.sum())
print("Product:", data.prod())
print("Mean:", data.mean())
print("Standard deviation:", data.std())

"""
Key Takeaways:
1. Vectorization eliminates explicit loops
2. Vectorized operations are much faster
3. Many real-world problems can be vectorized
4. NumPy provides many built-in vectorized operations
5. Vectorization makes code more readable and maintainable
""" 