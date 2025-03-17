# -----------------------------------------------------------------------------
# BASIC ITERATOR EXERCISE
# -----------------------------------------------------------------------------

"""
Exercise: Temperature Converter Iterator

In this exercise, you'll create a simple iterator that converts a list of
Celsius temperatures to Fahrenheit.

The formula is: F = C * 9/5 + 32

Tasks:
1. Implement the __iter__ method
2. Implement the __next__ method to convert temperatures
3. Raise StopIteration when all temperatures are processed
"""

class CelsiusToFahrenheit:
    def __init__(self, celsius_temps):
        self.celsius_temps = celsius_temps
        # TODO: Add any necessary instance variables
        # Hint: You'll need to keep track of position
    
    def __iter__(self):
        # TODO: Implement __iter__
        # Hint: Reset position and return self
        pass
    
    def __next__(self):
        # TODO: Implement __next__
        # 1. Check if there are more temperatures to process
        # 2. Get the next Celsius temperature
        # 3. Convert it to Fahrenheit
        # 4. Return the result
        pass

# Test the iterator
temps = [0, 10, 20, 30, 40]
temp_converter = CelsiusToFahrenheit(temps)

print("Converting Celsius to Fahrenheit:")
for fahrenheit in temp_converter:
    print(f"{fahrenheit}°F")

# Should print:
# 32.0°F
# 50.0°F
# 68.0°F
# 86.0°F
# 104.0°F 