queue = []

# Adding items to the end (O(1) amortized)
queue.append('First')
queue.append('Second')
queue.append('Third')
print("Queue after appending:", queue)

# Removing from the beginning (O(n) - has to shift all elements)
first_item = queue.pop(0)  # Inefficient!
print(f"Removed item: {first_item}")
print("Queue after pop(0):", queue)

# Example: Maintaining a sliding window
data = list(range(1000))
window_size = 3
windows = []

# Inefficient sliding window with lists
for i in range(len(data) - window_size + 1):
    window = data[i:i + window_size]  # Creates a new list each time
    windows.append(window)

print("\nFirst few sliding windows:", windows[:3])

# Example: Rotating a list
items = ['A', 'B', 'C', 'D']
# Rotate right by 1 (inefficient with lists)
items = [items[-1]] + items[:-1]
print("\nRotated list:", items)