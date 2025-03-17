# -----------------------------------------------------------------------------
# UNDER THE HOOD - HOW NAMEDTUPLES WORK
# -----------------------------------------------------------------------------

"""
Namedtuples are a type of class that are used to create immutable objects.
When created, they inherit from the 'tuple' class. And adds properties like:

- _fields
- _field_defaults
- _replace
- _asdict
- _make
- _asdict
"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

point = Point(1, 2)

print(point)

print(point._fields)

# -----------------------------------------------------------------------------
# IMPLEMENTATION OF NAMEDTUPLE UNDER THE HOOD
# -----------------------------------------------------------------------------

def create_namedtuple(typename, fields):
    """Simple implementation of namedtuple under the hood."""
    
    # Convert string fields to list if needed
    if isinstance(fields, str):
        fields = fields.replace(',', ' ').split()
    
    # Create class dictionary with properties
    class_dict = {
        '_fields': tuple(fields),
        '__slots__': ()  # Prevent instance dictionary creation
    }
    
    # Add property access for each field
    for idx, name in enumerate(fields):
        class_dict[name] = property(lambda self, i=idx: self[i])
    
    # Create new class inheriting from tuple
    return type(typename, (tuple,), class_dict)

# Let's create our own Point type
MyPoint = create_namedtuple('MyPoint', ['x', 'y'])

# Create an instance
p = MyPoint(3, 4)

print("\nDemonstrating our custom implementation:")
print(f"Point: {p}")
print(f"Access by index: p[0]={p[0]}, p[1]={p[1]}")
print(f"Access by name: p.x={p.x}, p.y={p.y}")
print(f"Fields: {p._fields}")
print(f"Is instance of tuple? {isinstance(p, tuple)}")





