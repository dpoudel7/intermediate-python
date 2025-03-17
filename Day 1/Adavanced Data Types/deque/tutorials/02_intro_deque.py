from collections import deque

# Basic deque operations
queue = deque(['First', 'Second', 'Third'])

# Adding and removing from both ends (all O(1))
queue.append('Last')  # Add to right
queue.appendleft('Start')  # Add to left
print("Queue after appends:", queue)

last = queue.pop()  # Remove from right
first = queue.popleft()  # Remove from left
print(f"Removed items - First: {first}, Last: {last}")
print("Queue after pops:", queue)

# Efficient rotation
queue.rotate(1)  # Rotate right by 1
print("Queue after rotating right:", queue)
queue.rotate(-1)  # Rotate left by 1
print("Queue after rotating left:", queue)

# Efficient sliding window
data = range(100)
window = deque(maxlen=3)  # Fixed-size window

# Adding items automatically maintains window size
for item in data:
    window.append(item)
    if len(window) == window.maxlen:
        print(f"Current window: {list(window)}")