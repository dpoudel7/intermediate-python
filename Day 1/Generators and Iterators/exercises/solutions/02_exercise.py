# -----------------------------------------------------------------------------
# ADVANCED ITERATOR EXERCISE - SOLUTION
# -----------------------------------------------------------------------------

"""
Exercise: Sliding Window Iterator

Create an iterator that implements a sliding window over a sequence.
For example, with a window size of 3:
sequence [1, 2, 3, 4, 5] would yield:
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]

Solution explanation:
1. Track current position with self.current
2. Check if enough elements remain for a full window
3. Create a new window list for each iteration
4. Handle edge cases properly
"""

class WindowedIterator:
    def __init__(self, sequence, window_size):
        if window_size <= 0:
            raise ValueError("Window size must be positive")
        
        self.sequence = sequence
        self.window_size = window_size
        self.current = 0  # Track current position
    
    def __iter__(self):
        self.current = 0  # Reset position
        return self
    
    def __next__(self):
        # Check if we can create another window
        if self.current + self.window_size > len(self.sequence):
            raise StopIteration
        
        # Create window from current position
        window = self.sequence[self.current:self.current + self.window_size]
        self.current += 1
        return window

# Test the iterator
sequence = [1, 2, 3, 4, 5]
windowed = WindowedIterator(sequence, 3)

print("First iteration:")
for window in windowed:
    print(window)

print("\nSecond iteration:")
for window in windowed:
    print(window)

# Test edge case
try:
    invalid = WindowedIterator([1, 2], 3)
    next(iter(invalid))
except StopIteration:
    print("\nProperly handled window size > sequence length")

# Additional test: window size 2
print("\nTesting with window size 2:")
windowed = WindowedIterator([1, 2, 3], 2)
for window in windowed:
    print(window) 