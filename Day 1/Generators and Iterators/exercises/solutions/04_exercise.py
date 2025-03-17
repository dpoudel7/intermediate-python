# -----------------------------------------------------------------------------
# ADVANCED GENERATOR EXERCISE - SOLUTION
# -----------------------------------------------------------------------------

"""
Exercise: Log Parser Pipeline

Create a pipeline of generators to process log entries. Each generator in the
pipeline will handle a specific task:

1. read_logs: Read log lines from a file
2. parse_logs: Parse each line into a dictionary
3. filter_errors: Filter only error messages
4. format_output: Format the errors for display

Solution explanation:
1. Each function is a generator that processes and yields items
2. Functions are connected in a pipeline
3. Each step handles a specific task
4. Error handling is implemented where needed
"""

def read_logs(filename):
    """Read log lines from file."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except Exception as e:
        print(f"Error reading file: {e}")

def parse_logs(lines):
    """Parse log lines into dictionaries."""
    for line in lines:
        try:
            # Split line into parts
            parts = line.split(' ', 3)
            if len(parts) == 4:
                date, time, level, message = parts
                yield {
                    'timestamp': f"{date} {time}",
                    'level': level,
                    'message': message
                }
        except Exception as e:
            print(f"Error parsing line: {line}, Error: {e}")
            continue

def filter_errors(log_dicts):
    """Filter only error messages."""
    for log in log_dicts:
        if log['level'] == 'ERROR':
            yield log

def format_output(error_dicts):
    """Format error dictionaries for display."""
    for error in error_dicts:
        yield f"{error['timestamp']} - {error['message']}"

# Create sample log file
with open('sample.log', 'w') as f:
    f.write("2024-01-15 10:30:15 ERROR Database connection failed\n")
    f.write("2024-01-15 10:30:16 INFO Server started\n")
    f.write("2024-01-15 10:30:17 ERROR Failed to load configuration\n")
    f.write("2024-01-15 10:30:18 DEBUG Checking cache\n")
    f.write("2024-01-15 10:30:19 ERROR Network timeout\n")
    # Add some malformed lines to test error handling
    f.write("Malformed line\n")
    f.write("2024-01-15 10:30:20 WARNING\n")

# Process logs through the pipeline
pipeline = format_output(
    filter_errors(
        parse_logs(
            read_logs('sample.log')
        )
    )
)

print("Processed error messages:")
for error in pipeline:
    print(error)

# Test with non-existent file
print("\nTesting with non-existent file:")
bad_pipeline = format_output(
    filter_errors(
        parse_logs(
            read_logs('nonexistent.log')
        )
    )
)
for error in bad_pipeline:
    print(error) 