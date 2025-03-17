from collections import defaultdict
from datetime import datetime
from typing import List, Dict, DefaultDict, Any, Optional
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
    """
    # Track tickets by category and subcategory
    category_counts = defaultdict(lambda: defaultdict(int))
    
    # Track ticket status by priority
    priority_status = defaultdict(lambda: defaultdict(int))
    
    # Track agent workload
    agent_tickets = defaultdict(list)
    
    # Track customer history
    customer_history = defaultdict(lambda: {
        'tickets': [],
        'categories': defaultdict(int),
        'priorities': defaultdict(int)
    })
    
    for ticket in tickets:
        # Update category counts
        category_counts[ticket['category']][ticket['subcategory']] += 1
        
        # Update priority status
        priority_status[ticket['priority']][ticket['status']] += 1
        
        # Update agent workload
        agent_tickets[ticket['assigned_to']].append(ticket['id'])
        
        # Update customer history
        customer = ticket['customer']
        customer_history[customer]['tickets'].append(ticket['id'])
        customer_history[customer]['categories'][ticket['category']] += 1
        customer_history[customer]['priorities'][ticket['priority']] += 1
    
    return {
        'category_analysis': dict(category_counts),
        'priority_status': dict(priority_status),
        'agent_workload': {
            agent: {
                'ticket_count': len(tickets),
                'tickets': tickets
            }
            for agent, tickets in agent_tickets.items()
        },
        'customer_history': dict(customer_history)
    }