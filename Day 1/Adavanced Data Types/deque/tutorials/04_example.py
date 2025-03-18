from collections import deque
from datetime import datetime
import time

# Example 2: Rate Limiting
class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.requests = deque(maxlen=max_requests)
        self.max_requests = max_requests
        self.time_window = time_window
    
    def allow_request(self):
        now = datetime.now()
        # Remove old requests
        while self.requests and (now - self.requests[0]).seconds > self.time_window:
            self.requests.popleft()
        
        time.sleep(2)

        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False

# Demonstrate rate limiting
limiter = RateLimiter(max_requests=3, time_window=5)
print("\nRate limiting:")
for i in range(4):
    allowed = limiter.allow_request()
    print(f"Request {i+1} allowed: {allowed}")