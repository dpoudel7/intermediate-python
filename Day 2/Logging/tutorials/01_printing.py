import time
import random
from datetime import datetime

def process_records_with_print(records):
    """Process records using print statements for output."""
    print("Starting record processing...")
    print(f"Time: {datetime.now()}")
    print(f"Found {len(records)} records to process")

successful = 0
failed = 0

for i, record in enumerate(records, 1):
    try:
        # Simulate processing
        time.sleep(0.1)
        if random.random() < 0.1:  # 10% chance of failure
            raise Exception(f"Failed to process record {record['id']}")
            
        successful += 1
        print(f"Successfully processed record {record['id']}")
        
    except Exception as e:
        failed += 1
        print(f"Error: {str(e)}")
    
    if i % 10 == 0:
        print(f"Progress: {i}/{len(records)} records processed")

print("\nProcessing completed!")
print(f"Time: {datetime.now()}")
print(f"Results: {successful} successful, {failed} failed")