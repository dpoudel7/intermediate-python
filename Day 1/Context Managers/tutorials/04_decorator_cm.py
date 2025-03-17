# -----------------------------------------------------------------------------
# DECORATOR-BASED CONTEXT MANAGERS
# -----------------------------------------------------------------------------

"""
This tutorial demonstrates how to create a decorator-based context manager.
"""

from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# Example usage
with file_manager('example.txt', 'w') as file:
    file.write('Hello, World!')

print("File automatically closed")


