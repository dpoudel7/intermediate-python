# -----------------------------------------------------------------------------
# PROBLEMS WITH TRADITIONAL RESOURCE MANAGEMENT
# -----------------------------------------------------------------------------

"""
This tutorial demonstrates common problems when managing resources without
context managers. These examples show why context managers are needed.
"""

# Example 1: Basic file handling without context manager
print("Example 1: Writing to a file")
file = None
try:
    file = open('example.txt', 'w')
    file.write('Hello, World!')
finally:
    if file:
        file.close()
    print("File closed")

# Example 2: Multiple resources without context managers
print("\nExample 2: Copying file content")
file1 = None
file2 = None
try:
    file1 = open('source.txt', 'r')
    file2 = open('destination.txt', 'w')
    content = file1.read()
    file2.write(content)
    print(f"Content copied: {content[:50]}...")  # Show first 50 chars
finally:
    if file1:
        file1.close()
        print("Source file closed")
    if file2:
        file2.close()
        print("Destination file closed")

# Example 3: Nested resource management (gets messy quickly)
print("\nExample 3: Database operations (simulated)")

def get_database_connection():
    """Simulate getting a database connection."""
    class FakeConnection:
        def cursor(self):
            return FakeCursor()
        def close(self):
            print("Connection closed")
    return FakeConnection()

def process_results(cursor):
    """Simulate processing database results."""
    print("Processing results...")

class FakeCursor:
    def execute(self, query):
        print(f"Executing: {query}")
    def close(self):
        print("Cursor closed")

connection = None
cursor = None
try:
    connection = get_database_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute('SELECT * FROM users')
            process_results(cursor)
        finally:
            if cursor:
                cursor.close()
    finally:
        if connection:
            connection.close()
except Exception as e:
    print(f"Error: {e}")

print("\nNotice how the code gets increasingly complex with nested try-finally blocks.")
print("In the next tutorial, we'll see how context managers simplify this.")