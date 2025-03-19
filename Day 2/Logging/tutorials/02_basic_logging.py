import logging
import time
import random

records = [
    {"id": 1, "value": "foo"},
    {"id": 2, "value": "bar"},
]

"""Process records using basic logging setup."""
# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Starting record processing...")
logging.info(f"Found {len(records)} records to process")

successful = 0
failed = 0

for i, record in enumerate(records, 1):
    try:
        # Simulate processing
        time.sleep(0.1)
        if random.random() < 0.1:  # 10% chance of failure
            logging.error(f"Failed to process record {record['id']}")
            raise Exception(f"Failed to process record {record['id']}")
            
        successful += 1
        logging.info(f"Successfully processed record {record['id']}")
        
    except Exception as e:
        failed += 1
        logging.error(f"Error processing record: {str(e)}")
        logging.exception("ERROR!")
    
    if i % 10 == 0:
        logging.info(f"Progress: {i}/{len(records)} records processed")

logging.info("Processing completed!")
logging.info(f"Results: {successful} successful, {failed} failed")