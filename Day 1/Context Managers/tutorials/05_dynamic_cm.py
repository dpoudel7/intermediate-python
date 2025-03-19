# -----------------------------------------------------------------------------
# DYNAMIC CONTEXT MANAGERS
# -----------------------------------------------------------------------------

"""
This tutorial demonstrates how to create a dynamic context manager.
"""

from contextlib import contextmanager, suppress, ExitStack
import os


# Using ExitStack to manage multiple resources dynamically
def process_multiple_files(file_paths):
    """Process multiple files using ExitStack.
    
    ExitStack lets us dynamically create and manage multiple context managers.
    This is useful when we don't know the number of resources at compile time.
    """
    with ExitStack() as stack:
        # Open all files and add them to the stack
        files = [
            stack.enter_context(open(path, 'r'))
            for path in file_paths
        ]
        
        # Process all files
        for file in files:
            print(f"Reading from {file.name}:")
            print(file.read())
            print()

def demonstrate_exitstack():
    """Show different ways to use ExitStack."""
    
    # Example 1: Basic multiple file handling
    print("Example 1: Processing multiple files")
    # process_multiple_files(['source.txt', 'example.txt'])
    
    # Example 2: Conditional resource management
    print("\nExample 2: Conditional resource management")
    with ExitStack() as stack:
        # Only open files that exist
        files = []
        for filename in ['exists.txt', 'doesnt_exist.txt']:
            try:
                file = stack.enter_context(open(filename, 'r'))
                files.append(file)
                print(f"Opened {filename}")
            except FileNotFoundError:
                print(f"Skipped {filename} - not found")
    
    # Example 3: Dynamic callback registration
    print("\nExample 3: Cleanup callbacks")
    with ExitStack() as stack:
        # Register cleanup callbacks
        stack.callback(lambda: print("Cleanup 1 done"))
        stack.callback(lambda: print("Cleanup 2 done"))
        print("Registered cleanup callbacks")
    print("Callbacks executed in reverse order")


    
demonstrate_exitstack()







