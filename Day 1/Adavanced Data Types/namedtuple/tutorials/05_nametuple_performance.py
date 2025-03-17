import sys
import time
import timeit

from collections import namedtuple

# Define data structures for comparison
Customer = namedtuple('Customer', ['name', 'email', 'phone', 'status', 'spend'])

# Create equivalent representations
data = ('John Doe', 'john@example.com', '555-1234', 'Gold', 50000)

tuple_customer = data
list_customer = list(data)
dict_customer = {'name': 'John Doe', 'email': 'john@example.com', 
                'phone': '555-1234', 'status': 'Gold', 'spend': 50000}
namedtuple_customer = Customer(*data)

class ClassCustomer:
    def __init__(self, name, email, phone, status, spend):
        self.name = name
        self.email = email
        self.phone = phone
        self.status = status
        self.spend = spend

class_customer = ClassCustomer(*data)

# Memory usage
print("Memory usage (bytes):")
print(f"Tuple: {sys.getsizeof(tuple_customer)}")
print(f"List: {sys.getsizeof(list_customer)}")
print(f"Dict: {sys.getsizeof(dict_customer)}")
print(f"NamedTuple: {sys.getsizeof(namedtuple_customer)}")
print(f"Class: {sys.getsizeof(class_customer)}")

# Access speed (simplified benchmark)
print("\nAccess speed (lower is better):")

# Tuple access by index
tuple_time = timeit.timeit(lambda: tuple_customer[1], number=1000000)
print(f"Tuple (by index): {tuple_time:.6f} seconds")

# List access by index
list_time = timeit.timeit(lambda: list_customer[1], number=1000000)
print(f"List (by index): {list_time:.6f} seconds")

# Dict access by key
dict_time = timeit.timeit(lambda: dict_customer['email'], number=1000000)
print(f"Dict (by key): {dict_time:.6f} seconds")

# NamedTuple access by attribute
namedtuple_attr_time = timeit.timeit(lambda: namedtuple_customer.email, number=1000000)
print(f"NamedTuple (by attribute): {namedtuple_attr_time:.6f} seconds")

# NamedTuple access by index
namedtuple_idx_time = timeit.timeit(lambda: namedtuple_customer[1], number=1000000)
print(f"NamedTuple (by index): {namedtuple_idx_time:.6f} seconds")

# Class access by attribute
class_time = timeit.timeit(lambda: class_customer.email, number=1000000)
print(f"Class (by attribute): {class_time:.6f} seconds")

# Creation speed
print("\nCreation speed (lower is better):")

# Tuple creation
tuple_create_time = timeit.timeit(lambda: (data[0], data[1], data[2], data[3], data[4]), number=100000)
print(f"Tuple creation: {tuple_create_time:.6f} seconds")

# List creation
list_create_time = timeit.timeit(lambda: [data[0], data[1], data[2], data[3], data[4]], number=100000)
print(f"List creation: {list_create_time:.6f} seconds")

# Dict creation
dict_create_time = timeit.timeit(
    lambda: {'name': data[0], 'email': data[1], 'phone': data[2], 'status': data[3], 'spend': data[4]}, 
    number=100000
)
print(f"Dict creation: {dict_create_time:.6f} seconds")

# NamedTuple creation
namedtuple_create_time = timeit.timeit(lambda: Customer(*data), number=100000)
print(f"NamedTuple creation: {namedtuple_create_time:.6f} seconds")

# Class creation
class_create_time = timeit.timeit(lambda: ClassCustomer(*data), number=100000)
print(f"Class creation: {class_create_time:.6f} seconds")