#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SECTION 1: THE PROBLEM - FILTERING DATA EFFICIENTLY
------------------------------------------------

In many applications, particularly in data processing and enterprise systems,
we often need to filter collections of data based on specific criteria. Traditional
approaches using loops and conditionals can be verbose and harder to maintain.

Consider this traditional approach:
"""

# Traditional imperative approach
def get_active_users(users):
    active_users = []
    for user in users:
        if user['status'] == 'active':
            active_users.append(user)
    return active_users

"""
INSTRUCTOR NOTES:

Key Teaching Points:
1. Traditional filtering approaches often mix iteration and condition logic
2. Imperative code can be harder to read and maintain as complexity grows
3. Error handling and edge cases can make the code even more complex

Discussion Questions:
Q: What are the drawbacks of using loops for filtering?
A: - More verbose and harder to read
   - Mixes concerns (iteration and filtering logic)
   - More prone to errors in complex scenarios
   - Less composable with other operations
   - Harder to parallelize or optimize

Q: How does this impact maintainability?
A: - More code means more places for bugs
   - Changes require careful consideration of the entire loop
   - Harder to modify or extend filtering criteria
   - Testing requires covering more code paths
"""

"""
SECTION 2: INTRODUCING FILTER
---------------------------

The filter() function is a built-in Python function that provides a more
functional approach to filtering sequences. It creates an iterator of elements
that satisfy a given predicate (a function that returns True/False).

Syntax: filter(function, iterable)
- function: predicate that returns True/False for each element
- iterable: sequence to filter
"""

# Simple filter example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Equivalent to the previous active users example
users = [
    {'id': 1, 'name': 'Alice', 'status': 'active'},
    {'id': 2, 'name': 'Bob', 'status': 'inactive'},
    {'id': 3, 'name': 'Charlie', 'status': 'active'}
]

active_users = list(filter(lambda user: user['status'] == 'active', users))

"""
INSTRUCTOR NOTES:

Key Teaching Points:
1. filter() is a higher-order function that takes a predicate
2. Returns an iterator (lazy evaluation)
3. More declarative and focused on "what" rather than "how"
4. Can be combined with other functional tools

Discussion Questions:
Q: Why use filter() instead of list comprehension?
A: - More explicit about intent (filtering vs. transformation)
   - Can be more readable for complex conditions
   - Follows functional programming principles
   - Can be more efficient for large datasets (lazy evaluation)
   - Better integration with other functional tools

Q: What are the trade-offs of using filter()?
A: - May require understanding of functional concepts
   - Lambda functions might be less readable for complex predicates
   - Need to be aware of lazy evaluation
   - May need to convert to list for immediate results
"""

"""
SECTION 3: ADVANCED FILTER PATTERNS
--------------------------------

Filter becomes particularly powerful when combined with other functional
programming concepts and when handling complex filtering scenarios.
"""

from typing import List, Dict, Callable
from functools import reduce
from operator import and_

def combine_filters(filters: List[Callable]) -> Callable:
    """Combine multiple filter predicates into one."""
    def combined_filter(item):
        return all(f(item) for f in filters)
    return combined_filter

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

high_budget_priority = list(filter(combine_filters(filters), data))

"""
INSTRUCTOR NOTES:

Key Teaching Points:
1. Filter predicates can be composed and combined
2. Complex filtering logic can be broken down into smaller, reusable parts
3. Filter works well with custom helper functions
4. Type hints help with maintainability

Discussion Questions:
Q: How do you design effective filter predicates?
A: - Keep predicates simple and focused
   - Use meaningful names for predicate functions
   - Consider reusability across different contexts
   - Use type hints for better maintainability
   - Document edge cases and assumptions

Q: What patterns emerge when using filter in large applications?
A: - Predicate factories for generating context-specific filters
   - Filter composition for complex rules
   - Caching filtered results for performance
   - Error handling for robust predicates
"""

"""
SECTION 4: PERFORMANCE AND OPTIMIZATION
-----------------------------------

Understanding filter's performance characteristics and optimization
techniques is crucial for effective usage in production systems.
"""

from itertools import filterfalse
import time

def benchmark_filter(data: List, predicate: Callable, iterations: int = 1000):
    """Benchmark filter performance."""
    start = time.time()
    for _ in range(iterations):
        list(filter(predicate, data))
    return time.time() - start

"""
INSTRUCTOR NOTES:

Key Teaching Points:
1. filter() is lazy - only evaluates when consumed
2. Memory efficiency through iterator protocol
3. Performance implications of predicate complexity
4. Trade-offs between filter and other approaches

Discussion Questions:
Q: When might filter's performance be a concern?
A: - Very large datasets
   - Complex predicates
   - Frequent filtering operations
   - Memory-constrained environments

Q: How can filter performance be optimized?
A: - Use simpler predicates when possible
   - Consider early termination for certain cases
   - Cache filtered results when appropriate
   - Use filterfalse for inverse operations
   - Consider parallel processing for large datasets
"""

"""
SECTION 5: BEST PRACTICES AND GUIDELINES
-------------------------------------

Following established best practices ensures effective and maintainable
use of filter in production code.
"""

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

"""
INSTRUCTOR NOTES:

Key Teaching Points:
1. Write clear, maintainable predicates
2. Handle errors gracefully
3. Consider reusability and composition
4. Document assumptions and requirements

Discussion Questions:
Q: What makes a good filter implementation?
A: - Clear predicate names and purposes
   - Proper error handling
   - Good documentation
   - Consideration of edge cases
   - Type hints for better maintainability
   - Tests for predicates and filtered results

Q: How do you ensure filter usage scales well?
A: - Break down complex filters into smaller parts
   - Use composition for flexibility
   - Consider performance implications
   - Plan for maintenance and updates
   - Document usage patterns and examples
"""

"""
SECTION 6: COMMON PITFALLS AND TROUBLESHOOTING
-------------------------------------------

Understanding common issues and how to address them is crucial for
effective use of filter.
"""

# Pitfall: Modifying data during filtering
def bad_practice_filter(items):
    return filter(
        lambda x: x.update({'processed': True}) or x['status'] == 'active',
        items
    )

# Better approach: Separate concerns
def mark_processed(items):
    return [dict(item, processed=True) for item in items]

def is_active(item):
    return item['status'] == 'active'

"""
INSTRUCTOR NOTES:

Key Teaching Points:
1. Common anti-patterns to avoid
2. Debugging filter operations
3. Testing strategies
4. Maintenance considerations

Discussion Questions:
Q: What are common filter-related bugs?
A: - Mutating data during filtering
   - Not handling edge cases
   - Complex, hard-to-maintain predicates
   - Incorrect assumption about data structure
   - Not considering performance implications

Q: How do you debug filter operations?
A: - Use logging in predicates
   - Write unit tests for predicates
   - Monitor performance metrics
   - Document edge cases and assumptions
   - Use type hints for better IDE support
"""