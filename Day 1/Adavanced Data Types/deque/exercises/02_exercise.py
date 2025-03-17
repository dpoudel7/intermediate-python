from collections import deque
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
import json

# Sample transaction data
transaction_data = [
    {'amount': 100, 'type': 'purchase', 'timestamp': '2024-03-01 10:00:00'},
    {'amount': 200, 'type': 'refund', 'timestamp': '2024-03-01 10:01:00'},
    {'amount': 150, 'type': 'purchase', 'timestamp': '2024-03-01 10:02:00'},
    {'amount': 300, 'type': 'purchase', 'timestamp': '2024-03-01 10:03:00'},
    {'amount': 50, 'type': 'refund', 'timestamp': '2024-03-01 10:04:00'},
    {'amount': 250, 'type': 'purchase', 'timestamp': '2024-03-01 10:05:00'},
    {'amount': 175, 'type': 'purchase', 'timestamp': '2024-03-01 10:06:00'},
    {'amount': 225, 'type': 'refund', 'timestamp': '2024-03-01 10:07:00'}
]

def analyze_transactions(transactions: List[Dict], window_size: int = 3) -> Dict:
    """
    Analyze transactions using a sliding window.
    
    TODO:
    1. Calculate moving averages for transaction amounts
    2. Track transaction types in the current window
    3. Detect anomalies (unusual patterns)
    4. Generate window-based statistics
    
    Use deque with maxlen for efficient window operations.
    """
    # Your code here
    pass