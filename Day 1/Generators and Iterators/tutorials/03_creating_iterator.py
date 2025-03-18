# -----------------------------------------------------------------------------
# CREATING A CUSTOM ITERATOR
# -----------------------------------------------------------------------------


class Countdown:
    """Iterator that counts down from a starting number."""
    
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        # Reset the counter and return self as iterator
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        self.current -= 1
        return self.current + 1

# Create and use the iterator
countdown = Countdown(3)

print("First iteration:")
for num in countdown: # -> __iter__ is called
    print(num) # __next__ is called

print("\nSecond iteration (starts over):")
for num in countdown:  # -> __iter__ is called
    print(num) # __next__ is called

# Manual iteration
print("\nManual iteration:")
manual_countdown = Countdown(3)
iterator = iter(manual_countdown)

print(next(iterator))  # 3
print(next(iterator))  # 2
print(next(iterator))  # 1 