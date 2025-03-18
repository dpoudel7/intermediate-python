import logging
import time
import random
from datetime import datetime

"""Process records using appropriate log levels."""
# Configure logging with a more detailed format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s',
    handlers=[
        logging.FileHandler('processing_detailed.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("Starting record processing...")
logger.debug(f"Processing started at: {datetime.now()}")
logger.info(f"Found {len(records)} records to process")

successful = 0
failed = 0
start_time = time.time()

for i, record in enumerate(records, 1):
    try:
        # Log detailed record information at DEBUG level
        logger.debug(f"Processing record: {record}")
        
        # Simulate processing
        time.sleep(0.1)
        if random.random() < 0.1:  # 10% chance of failure
            raise Exception(f"Failed to process record {record['id']}")
            
        successful += 1
        logger.debug(f"Successfully processed record {record['id']}")
        
    except Exception as e:
        failed += 1
        logger.error(
            f"Error processing record {record['id']}", 
            exc_info=True,
            extra={'record_id': record['id']}
        )
        
        # If multiple failures, escalate to warning
        if failed > len(records) * 0.2:  # More than 20% failure rate
            logger.warning(
                f"High failure rate detected: {failed}/{i} records failed"
            )
    
    if i % 10 == 0:
        progress = (i / len(records)) * 100
        logger.info(f"Progress: {progress:.1f}% ({i}/{len(records)} records)")

processing_time = time.time() - start_time
logger.info("Processing completed!")
logger.info(
    f"Results: {successful} successful, {failed} failed "
    f"(took {processing_time:.2f} seconds)"
)

# Log summary statistics
if failed > 0:
    logger.warning(f"Failed to process {failed} records")
if successful == len(records):
    logger.info("All records processed successfully!")