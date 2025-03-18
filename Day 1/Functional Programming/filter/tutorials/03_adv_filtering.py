from typing import List, Dict, Callable
from functools import reduce

# Example usage
data = [
    {'name': 'Project A', 'budget': 10000, 'priority': 'high'},
    {'name': 'Project B', 'budget': 5000, 'priority': 'medium'},
    {'name': 'Project C', 'budget': 15000, 'priority': 'high'}
]


filters = [
    lambda x: x['budget'] > 7000,
    lambda x: x['priority'] == 'high'
]

def combine_filters(filters: List[Callable]) -> Callable:
    """Combine multiple filter predicates into one."""
    def combined_filter(item):
        return all(f(item) for f in filters)
    return combined_filter

high_budget_priority = list(filter(combine_filters(filters), data))

print(high_budget_priority)
