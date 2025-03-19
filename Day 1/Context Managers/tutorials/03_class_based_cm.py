# -----------------------------------------------------------------------------
# CLASS-BASED CONTEXT MANAGERS
# -----------------------------------------------------------------------------

"""
This tutorial demonstrates how to create a class-based context manager.

The class-based context manager is a more explicit way to manage resources.
It uses the __enter__ and __exit__ methods to manage the resources.

"""

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        BIG_TEST_STRING = "HEY THERE! :))"
        return self.file, BIG_TEST_STRING

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Example usage
try:
    with FileManager('example.txt', 'w') as (file, ts):
        print(ts)
        file.write('Hello, World!')
except:
    print("An error occurred")

print("File automatically closed")


