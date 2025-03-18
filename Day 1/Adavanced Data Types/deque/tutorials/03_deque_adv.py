from collections import deque

# Circular buffer with maxlen
history = deque(maxlen=3)
for i in range(5):
    history.append(i)
    print(f"History after adding {i}: {list(history)}")

print(history) # -> [2, 3, 4]

# LRU Cache implementation
class LRUCache:
    def __init__(self, maxsize):
        self.cache = {}
        self.history = deque(maxlen=maxsize)
    
    def get(self, key):
        if key in self.cache:
            # Move to most recently used
            self.history.remove(key)
            self.history.append(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            self.history.remove(key)
            
        elif len(self.history) == self.history.maxlen:
            # Remove least recently used
            lru_key = self.history.popleft()
            del self.cache[lru_key]
        
        self.cache[key] = value
        self.history.append(key)

# Demonstrate LRU Cache
lru = LRUCache(3)
lru.put('A', 1)
lru.put('B', 2)
lru.put('C', 3)
print("\nLRU Cache after initial puts:", list(lru.history))

lru.get('A')  # Moves 'A' to most recent
print("LRU Cache after accessing 'A':", list(lru.history))

lru.put('D', 4)  # Should evict 'B'
print("LRU Cache after adding 'D':", list(lru.history))
