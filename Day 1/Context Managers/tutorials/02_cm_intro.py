# -----------------------------------------------------------------------------
# SIMPLIFYING RESOURCE MANAGEMENT WITH CONTEXT MANAGERS
# -----------------------------------------------------------------------------

"""
This tutorial demonstrates how context managers simplify resource management.
Compare these examples with the previous tutorial to see the difference.
"""

# Example 1: File handling with context manager
print("Example 1: Writing to a file")
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
print("File automatically closed")

# Example 2: Multiple resources with context managers
print("\nExample 2: Copying file content")
with open('source.txt', 'r') as source, open('destination.txt', 'w') as dest:
    content = source.read()
    dest.write(content)
    print(f"Content copied: {content[:50]}...")  # Show first 50 chars
print("Both files automatically closed")

# Example 3: Nested resources (much cleaner!)
print("\nExample 3: Database operations (simulated)")

class FakeConnection:
    def __init__(self):
        print("Connection created")
    
    def cursor(self):
        return FakeCursor()
    
    def close(self):
        print("Connection closed")
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class FakeCursor:
    def execute(self, query):
        print(f"Executing: {query}")
    
    def close(self):
        print("Cursor closed")
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def get_database_connection():
    """Simulate getting a database connection."""
    return FakeConnection()

def process_results(cursor):
    """Simulate processing database results."""
    print("Processing results...")

# Using context managers for database operations
with get_database_connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM users')
        process_results(cursor)

print("All database resources automatically closed")