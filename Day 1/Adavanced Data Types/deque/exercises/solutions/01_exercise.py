from collections import deque
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
import json
import statistics

# Sample message data
message_data = [
    {
        'id': 'MSG001',
        'type': 'email',
        'priority': 'high',
        'recipient': 'user@example.com',
        'subject': 'Account Update',
        'timestamp': '2024-03-01 10:00:00'
    },
    {
        'id': 'MSG002',
        'type': 'sms',
        'priority': 'medium',
        'recipient': '+1234567890',
        'subject': 'Login Alert',
        'timestamp': '2024-03-01 10:01:00'
    },
    {
        'id': 'MSG003',
        'type': 'notification',
        'priority': 'low',
        'recipient': 'app_user_123',
        'subject': 'New Feature',
        'timestamp': '2024-03-01 10:02:00'
    },
    {
        'id': 'MSG004',
        'type': 'email',
        'priority': 'high',
        'recipient': 'admin@example.com',
        'subject': 'Security Alert',
        'timestamp': '2024-03-01 10:03:00'
    },
    {
        'id': 'MSG005',
        'type': 'sms',
        'priority': 'medium',
        'recipient': '+0987654321',
        'subject': 'Password Reset',
        'timestamp': '2024-03-01 10:04:00'
    }
]

def implement_message_queue(messages: List[Dict]) -> Dict:
    """Implement a message processing queue using deque."""
    # Create priority queues
    high_priority = deque()
    medium_priority = deque()
    low_priority = deque()
    
    # Statistics tracking
    stats = {
        'type_counts': {'email': 0, 'sms': 0, 'notification': 0},
        'priority_counts': {'high': 0, 'medium': 0, 'low': 0},
        'total_messages': 0
    }
    
    # Process timeout (5 minutes)
    timeout = timedelta(minutes=5)
    
    # Sort messages into priority queues
    for message in messages:
        # Update statistics
        stats['type_counts'][message['type']] += 1
        stats['priority_counts'][message['priority']] += 1
        stats['total_messages'] += 1
        
        # Add timestamp object for timeout checking
        message['timestamp_obj'] = datetime.strptime(
            message['timestamp'], 
            '%Y-%m-%d %H:%M:%S'
        )
        
        # Add to appropriate queue
        if message['priority'] == 'high':
            high_priority.append(message)
        elif message['priority'] == 'medium':
            medium_priority.append(message)
        else:
            low_priority.append(message)
    
    def process_queue(queue: deque) -> List[Dict]:
        """Process a queue and handle timeouts."""
        processed = []
        current_time = datetime.now()
        
        while queue:
            message = queue.popleft()
            if current_time - message['timestamp_obj'] <= timeout:
                processed.append(message)
        
        return processed
    
    # Process all queues in priority order
    processed_messages = {
        'high_priority': process_queue(high_priority),
        'medium_priority': process_queue(medium_priority),
        'low_priority': process_queue(low_priority)
    }
    
    return {
        'processed_messages': processed_messages,
        'statistics': stats
    }