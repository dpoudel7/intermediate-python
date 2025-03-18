#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCISE 2: IMPLEMENTING STRUCTURED AND CONTEXTUAL LOGGING

In this exercise, you'll improve a Salesforce batch processing system
by implementing structured and contextual logging. The system processes
different types of Salesforce objects (Accounts, Contacts, Opportunities)
in batches.

Tasks:
1. Implement structured logging for batch operations
2. Add contextual logging for tracking batch processing
3. Create custom log formatters for different outputs (console, file, JSON)
4. Implement performance logging
5. Add proper error context in logs

The code below processes Salesforce objects in batches. Your task is to
improve it by implementing structured and contextual logging.
"""

import time
import random
import json
from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

class ObjectType(Enum):
    ACCOUNT = "Account"
    CONTACT = "Contact"
    OPPORTUNITY = "Opportunity"

@dataclass
class BatchConfig:
    """Configuration for a batch process."""
    object_type: ObjectType
    batch_size: int
    timeout_seconds: int
    max_retries: int

class BatchProcessor:
    """Processes Salesforce objects in batches."""
    
    def __init__(self, config: BatchConfig):
        self.config = config
        # TODO: Setup structured logging here
    
    def process_batch(self, records: List[Dict]) -> Dict[str, Any]:
        """Process a batch of records."""
        print(f"Processing batch of {len(records)} {self.config.object_type.value}s")
        
        successful = []
        failed = []
        start_time = time.time()
        
        for record in records:
            try:
                if self._process_record(record):
                    successful.append(record['id'])
                else:
                    failed.append(record['id'])
            except Exception as e:
                print(f"Error processing record {record['id']}: {str(e)}")
                failed.append(record['id'])
        
        duration = time.time() - start_time
        
        result = {
            'object_type': self.config.object_type.value,
            'total_records': len(records),
            'successful': len(successful),
            'failed': len(failed),
            'duration_seconds': duration
        }
        
        print(f"Batch processing completed: {json.dumps(result)}")
        return result
    
    def _process_record(self, record: Dict) -> bool:
        """Process a single record."""
        # Simulate processing
        time.sleep(0.1)
        
        # Simulate random failures
        if random.random() < 0.1:  # 10% chance of failure
            print(f"Failed to process record: {record['id']}")
            return False
        
        return True

def get_sample_records(object_type: ObjectType, count: int) -> List[Dict]:
    """Generate sample records for testing."""
    records = []
    
    for i in range(count):
        record_id = f"{object_type.value[:3].upper()}_{i:03d}"
        
        if object_type == ObjectType.ACCOUNT:
            record = {
                'id': record_id,
                'name': f"Account {i}",
                'industry': random.choice(['Tech', 'Manufacturing', 'Healthcare']),
                'employees': random.randint(10, 1000)
            }
        elif object_type == ObjectType.CONTACT:
            record = {
                'id': record_id,
                'first_name': f"First{i}",
                'last_name': f"Last{i}",
                'email': f"contact{i}@example.com",
                'phone': f"555-{i:03d}-{i:04d}"
            }
        else:  # OPPORTUNITY
            record = {
                'id': record_id,
                'name': f"Opportunity {i}",
                'amount': random.randint(10000, 100000),
                'stage': random.choice(['Prospecting', 'Negotiation', 'Closed Won'])
            }
        
        records.append(record)
    
    return records

def main():
    """Main function demonstrating batch processing."""
    # Process different types of objects
    for object_type in ObjectType:
        print(f"\nProcessing {object_type.value} records...")
        
        # Configure batch processing
        config = BatchConfig(
            object_type=object_type,
            batch_size=10,
            timeout_seconds=30,
            max_retries=3
        )
        
        # Create processor
        processor = BatchProcessor(config)
        
        # Get sample records
        records = get_sample_records(object_type, 25)
        
        # Process in batches
        for i in range(0, len(records), config.batch_size):
            batch = records[i:i + config.batch_size]
            try:
                processor.process_batch(batch)
            except Exception as e:
                print(f"Error processing batch: {str(e)}")

if __name__ == "__main__":
    main() 