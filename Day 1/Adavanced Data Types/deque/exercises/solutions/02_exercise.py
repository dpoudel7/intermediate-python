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
    """Analyze transactions using a sliding window."""
    # Create sliding windows for different metrics
    amounts = deque(maxlen=window_size)
    types = deque(maxlen=window_size)
    
    # Track moving statistics
    moving_stats = []
    anomalies = []
    
    for transaction in transactions:
        # Add to windows
        amounts.append(transaction['amount'])
        types.append(transaction['type'])
        
        # Calculate statistics when window is full
        if len(amounts) == window_size:
            window_stats = {
                'timestamp': transaction['timestamp'],
                'average': statistics.mean(amounts),
                'median': statistics.median(amounts),
                'type_counts': {
                    'purchase': types.count('purchase'),
                    'refund': types.count('refund')
                }
            }
            
            # Detect anomalies
            if window_stats['average'] > 200:
                anomalies.append({
                    'timestamp': transaction['timestamp'],
                    'type': 'high_average',
                    'value': window_stats['average']
                })
            
            if types.count('refund') > types.count('purchase'):
                anomalies.append({
                    'timestamp': transaction['timestamp'],
                    'type': 'high_refunds',
                    'refund_count': types.count('refund')
                })
            
            moving_stats.append(window_stats)
    
    return {
        'moving_statistics': moving_stats,
        'anomalies': anomalies,
        'final_window': {
            'amounts': list(amounts),
            'types': list(types)
        }
    }