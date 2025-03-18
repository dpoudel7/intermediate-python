# -----------------------------------------------------------------------------
# INTRODUCTION TO ITERTOOLS
# -----------------------------------------------------------------------------


from itertools import count, cycle, repeat, islice

# Infinite counting
counter = count(1)  # Counts from 1 indefinitely
print("count():", list(islice(counter, 50)))  # Take first 5 numbers

# Cycling through elements
colors = cycle(['red', 'green', 'blue'])
print("\ncycle():", [next(colors) for _ in range(5)])  # Show 5 cycles

# Repeating elements
repeater = repeat('spam', 3)  # Repeat 'spam' 3 times
print("\nrepeat():", list(repeater))

# Combining iterables
from itertools import chain, zip_longest

# Chain multiple iterables
numbers = chain([1, 2], "Hello")
print("\nchain():", list(numbers))

# Zip with different lengths
list1 = [1, 2]
list2 = ['a', 'b', 'c']
print("\nzip_longest():", list(zip_longest(list1, list2, fillvalue='*'))) 