
cases = [
    {
        'id': 'CS001',
        'subject': 'Technical Issue',
        'status': 'New',
        'priority': 'High',
        'created_date': '2023-12-01',
        'last_modified': '2023-12-01',
        'is_escalated': False
    },
    {
        'id': 'CS002',
        'subject': 'Feature Request',
        'status': 'In Progress',
        'priority': 'Medium',
        'created_date': '2023-11-15',
        'last_modified': '2023-12-05',
        'is_escalated': True
    },
    {
        'id': 'CS003',
        'subject': 'Bug Report',
        'status': 'New',
        'priority': 'Critical',
        'created_date': '2023-12-05',
        'last_modified': '2023-12-05',
        'is_escalated': True
    }
]

def exercise3():
    """Complex lambda operations with case data."""
    print("\nExercise 3: Complex Lambda Operations")
    
    # TODO 1: Create a lambda to check if case needs immediate attention
    # (is_escalated True OR priority Critical)
    
    # TODO 2: Create a lambda to transform case into status update string
    # Format: "Case {id}: {subject} - {status} ({priority})"
    
    # TODO 3: Create a lambda for sorting cases by priority
    # Order: Critical -> High -> Medium -> Low

    # Test your lambdas
    if needs_attention and format_status and sort_by_priority:
        print("Needs attention:", list(filter(needs_attention, cases)))
        print("Status updates:", list(map(format_status, cases)))
        sorted_cases = sorted(cases, key=sort_by_priority)
        print("Sorted by priority:", [f"{c['subject']} ({c['priority']})" for c in sorted_cases])
    else:
        print("Please complete the TODOs first!")