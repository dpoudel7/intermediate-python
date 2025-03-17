# -----------------------------------------------------------------------------
# ITERATOR BEST PRACTICES
# -----------------------------------------------------------------------------

# 1. Separate Iterator from Iterable
class NumberSequence:
    """Iterable that produces numbers."""
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return NumberIterator(self.start, self.end)

class NumberIterator:
    """Iterator for NumberSequence."""
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# 2. Use iter() with Sentinel Value
with open('example.txt', 'w') as f:
    f.write('line 1\nline 2\nEND\nline 4')

print("Reading until sentinel:")
with open('example.txt') as f:
    for line in iter(lambda: f.readline().strip(), 'END'):
        print(line)

# 3. Don't store iterators in lists unless necessary
numbers = range(1000000)  # Iterator
# BAD: list(numbers)  # Don't convert to list unnecessarily
# GOOD: Use iterator directly
print("\nFirst 5 numbers:", [next(iter(numbers)) for _ in range(5)])

# 4. Use itertools when possible
from itertools import islice
print("\nUsing islice instead of converting to list:")
result = islice(numbers, 0, 5)  # More efficient than list slicing
print(list(result)) 