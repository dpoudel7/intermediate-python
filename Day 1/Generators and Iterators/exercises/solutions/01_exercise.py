# -----------------------------------------------------------------------------
# BASIC ITERATOR EXERCISE - SOLUTION
# -----------------------------------------------------------------------------

"""
Exercise: Temperature Converter Iterator

In this exercise, you'll create a simple iterator that converts a list of
Celsius temperatures to Fahrenheit.

The formula is: F = C * 9/5 + 32

Solution explanation:
1. We track position using self.index
2. __iter__ resets the index and returns self
3. __next__ checks if we've processed all temperatures
4. Convert and return the next temperature
"""

class CelsiusToFahrenheit:
    def __init__(self, celsius_temps):
        self.celsius_temps = celsius_temps
        self.index = 0  # Keep track of current position
    
    def __iter__(self):
        self.index = 0  # Reset position
        return self
    
    def __next__(self):
        if self.index >= len(self.celsius_temps):
            raise StopIteration
        
        celsius = self.celsius_temps[self.index]
        self.index += 1
        return celsius * 9/5 + 32

# Test the iterator
temps = [0, 10, 20, 30, 40]
temp_converter = CelsiusToFahrenheit(temps)

print("Converting Celsius to Fahrenheit:")
for fahrenheit in temp_converter:
    print(f"{fahrenheit}°F")

# Verify it can be used multiple times
print("\nConverting again:")
for fahrenheit in temp_converter:
    print(f"{fahrenheit}°F") 