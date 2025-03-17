# -----------------------------------------------------------------------------
# GENERATOR BEST PRACTICES
# -----------------------------------------------------------------------------

# 1. Proper Resource Management
def read_large_file(file_path, chunk_size=8192):
    """Properly managed file reading generator."""
    try:
        with open(file_path, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    except Exception as e:
        print(f"Error reading file: {e}")

# Create a sample file
with open('large_file.txt', 'w') as f:
    f.write('A' * 1000 + '\n')
    f.write('B' * 1000 + '\n')

# Use the generator
print("Reading file in chunks:")
for chunk in read_large_file('large_file.txt', chunk_size=500):
    print(f"Got chunk of size: {len(chunk)}")

# 2. Proper Error Handling
def number_generator(n):
    """Generator with proper error handling."""
    try:
        for i in range(n):
            if i == 5:
                raise ValueError("Example error")
            yield i
    except ValueError as e:
        print(f"Handled error: {e}")
    finally:
        print("Generator cleanup")

print("\nError handling example:")
for num in number_generator(10):
    print(num)

# 3. Memory-Efficient Data Processing
def process_data(data_generator):
    """Shows how to chain generators efficiently."""
    # Filter
    def filter_even(numbers):
        for num in numbers:
            if num % 2 == 0:
                yield num
    
    # Transform
    def double_numbers(numbers):
        for num in numbers:
            yield num * 2
    
    # Chain operations
    filtered = filter_even(data_generator)
    doubled = double_numbers(filtered)
    return doubled

print("\nEfficient data processing:")
data = range(10)
processed = process_data(data)
for item in processed:
    print(item)

# 4. Reusable Generator Pattern
class DataProcessor:
    """Class demonstrating reusable generator pattern."""
    def __init__(self, data):
        self.data = data
    
    def process(self):
        """Generator method that can be called multiple times."""
        for item in self.data:
            yield item * 2

print("\nReusable generator pattern:")
processor = DataProcessor([1, 2, 3])
print("First run:", list(processor.process()))
print("Second run:", list(processor.process())) 