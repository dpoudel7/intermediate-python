from collections import defaultdict
from datetime import datetime
from typing import List, Dict, DefaultDict
import json

# Sample support ticket data
ticket_data = [
    {
        'id': 'T001',
        'customer': 'Acme Corp',
        'category': 'Technical',
        'subcategory': 'API',
        'priority': 'High',
        'status': 'Open',
        'assigned_to': 'Alice',
        'created_date': '2024-03-01'
    },
    {
        'id': 'T002',
        'customer': 'Globex',
        'category': 'Billing',
        'subcategory': 'Subscription',
        'priority': 'Medium',
        'status': 'Closed',
        'assigned_to': 'Bob',
        'created_date': '2024-03-02'
    },
    {
        'id': 'T003',
        'customer': 'Acme Corp',
        'category': 'Technical',
        'subcategory': 'Integration',
        'priority': 'Low',
        'status': 'In Progress',
        'assigned_to': 'Charlie',
        'created_date': '2024-03-02'
    },
    {
        'id': 'T004',
        'customer': 'Wayne Corp',
        'category': 'Technical',
        'subcategory': 'API',
        'priority': 'High',
        'status': 'Open',
        'assigned_to': 'Alice',
        'created_date': '2024-03-03'
    },
    {
        'id': 'T005',
        'customer': 'Globex',
        'category': 'Technical',
        'subcategory': 'Integration',
        'priority': 'Medium',
        'status': 'Closed',
        'assigned_to': 'Bob',
        'created_date': '2024-03-03'
    }
]

def analyze_support_tickets(tickets: List[Dict]) -> Dict:
    """
    Analyze support tickets using defaultdict to track various metrics.
    
    TODO:
    1. Track number of tickets by category and subcategory
    2. Track ticket status by priority
    3. Track agent workload (number of tickets assigned)
    4. Track customer ticket history
    
    Use defaultdict to simplify the data structure creation and updates.
    """
    # Your code here
    pass
