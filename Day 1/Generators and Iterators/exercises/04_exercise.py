# -----------------------------------------------------------------------------
# ADVANCED GENERATOR EXERCISE
# -----------------------------------------------------------------------------

"""
Exercise: Log Parser Pipeline

Create a pipeline of generators to process log entries. Each generator in the
pipeline will handle a specific task:

1. read_logs: Read log lines from a file
2. parse_logs: Parse each line into a dictionary
3. filter_errors: Filter only error messages
4. format_output: Format the errors for display

Example log line:
2024-01-15 10:30:15 ERROR Database connection failed
2024-01-15 10:30:16 INFO Server started
2024-01-15 10:30:17 ERROR Failed to load configuration

Tasks:
1. Complete each generator function
2. Connect them in a pipeline
3. Handle errors gracefully
"""

def read_logs(filename):
    """Read log lines from file."""
    # TODO: Open file and yield lines
    # Hint: Use with statement for file handling
    pass

def parse_logs(lines):
    """Parse log lines into dictionaries."""
    # TODO: Parse each line into parts
    # Expected format: date time level message
    # Return dict with keys: timestamp (date + time), level, message
    pass

def filter_errors(log_dicts):
    """Filter only error messages."""
    # TODO: Yield only dictionaries where level is ERROR
    pass

def format_output(error_dicts):
    """Format error dictionaries for display."""
    # TODO: Format each error dictionary into a string
    # Format: timestamp - message
    pass

# Create sample log file
with open('sample.log', 'w') as f:
    f.write("2024-01-15 10:30:15 ERROR Database connection failed\n")
    f.write("2024-01-15 10:30:16 INFO Server started\n")
    f.write("2024-01-15 10:30:17 ERROR Failed to load configuration\n")
    f.write("2024-01-15 10:30:18 DEBUG Checking cache\n")
    f.write("2024-01-15 10:30:19 ERROR Network timeout\n")

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

# Should print:
# 2024-01-15 10:30:15 - Database connection failed
# 2024-01-15 10:30:17 - Failed to load configuration
# 2024-01-15 10:30:19 - Network timeout 