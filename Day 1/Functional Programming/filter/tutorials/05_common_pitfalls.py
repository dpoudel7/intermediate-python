# -----------------------------------------------------------------------------
# COMMON PITFALLS WHEN USING FILTER
# -----------------------------------------------------------------------------

"""
This tutorial demonstrates common mistakes when using filter and how to avoid them.
"""

def demonstrate_side_effects():
    """Pitfall 1: Modifying data during filtering."""
    print("Pitfall 1: Side Effects in Filter")
    
    # Bad practice: Modifying items during filtering
    items = [
        {'id': 1, 'status': 'active', 'processed': False},
        {'id': 2, 'status': 'inactive', 'processed': False},
        {'id': 3, 'status': 'active', 'processed': False}
    ]
    
    print("Original items:", items)
    
    # BAD: Modifying while filtering
    active_items = list(filter(
        lambda x: x.update({'processed': True}) or x['status'] == 'active',
        items
    ))
    
    print("After bad filter (all items modified!):", items)
    print("Filtered items:", active_items)
    
    # GOOD: Separate the operations
    items = [
        {'id': 1, 'status': 'active', 'processed': False},
        {'id': 2, 'status': 'inactive', 'processed': False},
        {'id': 3, 'status': 'active', 'processed': False}
    ]
    
    def is_active(item):
        return item['status'] == 'active'
    
    active_items = list(filter(is_active, items))
    processed_items = [dict(item, processed=True) for item in active_items]
    
    print("\nBetter approach results:")
    print("Original items unchanged:", items)
    print("Processed active items:", processed_items)

def demonstrate_mutable_defaults():
    """Pitfall 2: Using mutable default arguments."""
    print("\nPitfall 2: Mutable Default Arguments")
    
    # BAD: Using mutable default argument
    def bad_filter(items, processed=[]):
        processed.append('call')  # This modifies the default list!
        return list(filter(lambda x: x > 0, items))
    
    print("First call:", bad_filter([1, 2, 3]))
    print("Second call processed list:", bad_filter([4, 5, 6]))  # Oops!
    
    # GOOD: Use None as default
    def good_filter(items, processed=None):
        processed = [] if processed is None else processed
        processed.append('call')
        return list(filter(lambda x: x > 0, items))
    
    print("\nBetter approach:")
    print("First call:", good_filter([1, 2, 3]))
    print("Second call:", good_filter([4, 5, 6]))  # Clean!

def demonstrate_none_return():
    """Pitfall 3: Functions that return None in filter."""
    print("\nPitfall 3: None-returning Functions in Filter")
    
    items = [{'name': 'a'}, {'name': 'b'}, {'name': 'c'}]
    
    # BAD: Method returns None but used in filter
    def bad_process(item):
        item['processed'] = True  # Returns None!
    
    filtered = list(filter(bad_process, items))
    print("Bad filter (empty because function returns None):", filtered)
    
    # GOOD: Return a boolean
    def good_process(item):
        item['processed'] = True
        return True
    
    filtered = list(filter(good_process, items))
    print("Good filter (maintains items):", filtered)

def main():
    """Run all pitfall demonstrations."""
    demonstrate_side_effects()
    demonstrate_mutable_defaults()
    demonstrate_none_return()

if __name__ == "__main__":
    main()
