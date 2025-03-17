# -----------------------------------------------------------------------------
# ADVANCED GENERATOR FEATURES
# -----------------------------------------------------------------------------

# Generator with send() - Two-way communication
def counter(start=0):
    """Generator that can receive values while generating."""
    current = start
    while True:
        # yield returns a value AND receives next value to adjust
        adjustment = yield current
        if adjustment is not None:
            current += adjustment
        else:
            current += 1

# Using send()
print("Two-way communication with send():")
c = counter(10)
print(next(c))      # Prime the generator
print(c.send(2))    # Add 2
print(c.send(-3))   # Subtract 3
print(next(c))      # Default increment

# Generator with throw() and cleanup
def sensor_reader():
    """Simulates reading from a sensor with error handling."""
    try:
        while True:
            try:
                yield "Reading sensor..."
            except ValueError as e:
                print(f"Handled error: {e}")
    finally:
        print("Cleaning up sensor resources!")

# Using throw()
print("\nError handling with throw():")
sensor = sensor_reader()
print(next(sensor))
print(next(sensor))
sensor.throw(ValueError("Sensor malfunction"))
sensor.close()

# yield from example
def sub_generator():
    yield "Message 1 from sub"
    yield "Message 2 from sub"

def main_generator():
    yield "Message from main"
    yield from sub_generator()
    yield "Back to main"

print("\nUsing yield from:")
for msg in main_generator():
    print(msg)

# Pipeline example
def producer():
    """Produces data."""
    for i in range(3):
        yield f"Data {i}"

def filter_processor(data):
    """Processes data."""
    for item in data:
        yield f"Processed {item}"

def consumer(data):
    """Consumes data."""
    for item in data:
        yield f"Consumed {item}"

# Create pipeline
print("\nPipeline processing:")
pipeline = consumer(filter_processor(producer()))
for result in pipeline:
    print(result) 