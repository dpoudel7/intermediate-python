# -----------------------------------------------------------------------------
# ADVANCED ITERATOR EXERCISE
# -----------------------------------------------------------------------------

"""
Exercise: Sliding Window Iterator

Create an iterator that implements a sliding window over a sequence.
For example, with a window size of 3:
sequence [1, 2, 3, 4, 5] would yield:
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]

Tasks:
1. Complete the WindowedIterator class
2. Implement proper iteration protocol
3. Handle edge cases (window_size > sequence length)
4. Make it reusable (multiple iterations)
"""

class WindowedIterator:
    def __init__(self, sequence, window_size):
        if window_size <= 0:
            raise ValueError("Window size must be positive")
        
        self.sequence = sequence
        self.window_size = window_size
        # TODO: Add any necessary instance variables
    
    def __iter__(self):
        # TODO: Implement __iter__
        # Hint: Reset position and return iterator
        pass
    
    def __next__(self):
        # TODO: Implement __next__
        # 1. Check if there are enough elements left
        # 2. Get the next window of elements
        # 3. Return the window
        # 4. Raise StopIteration when done
        pass

# Test the iterator
sequence = [1, 2, 3, 4, 5]
windowed = WindowedIterator(sequence, 3)

print("First iteration:")
for window in windowed:
    print(window)

print("\nSecond iteration:")
for window in windowed:
    print(window)

# Should print:
# First iteration:
# [1, 2, 3]
# [2, 3, 4]
# [3, 4, 5]
# 
# Second iteration:
# [1, 2, 3]
# [2, 3, 4]
# [3, 4, 5]

# Test edge case
try:
    invalid = WindowedIterator([1, 2], 3)
    next(iter(invalid))
except StopIteration:
    print("\nProperly handled window size > sequence length") 