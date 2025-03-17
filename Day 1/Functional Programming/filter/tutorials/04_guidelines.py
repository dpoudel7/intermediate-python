# Good Practice: Named predicates for clarity
def is_high_priority(item: Dict) -> bool:
    return item['priority'] == 'high'

def meets_budget_threshold(threshold: float) -> Callable:
    return lambda item: item['budget'] >= threshold

# Good Practice: Error handling in predicates
def safe_predicate(predicate: Callable) -> Callable:
    def wrapped(item):
        try:
            return predicate(item)
        except (KeyError, TypeError, ValueError):
            return False
    return wrapped

# Good Practice: Use list comprehensions for simple filters
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]

# Good Practice: Use filter with named predicates
filtered_users = list(filter(is_active, users))

# Good Practice: Use filter with named predicates
filtered_projects = list(filter(meets_budget_threshold(1000), projects))

# Good Practice: Use filter with named predicates
filtered_data = list(filter(is_high_priority, data))

# Good Practice: Use filter with named predicates
filtered_data = list(filter(safe_predicate(is_high_priority), data))


