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
import logging
from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

from contextlib import contextmanager
import threading

# Logging configuration

class JsonFormatter(logging.Formatter):


    def format(self, record:logging.LogRecord) -> str:
        message = super().format(record)

        log_data = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "message": message,
            "logger": record.name
        }

        if hasattr(record, "batch_id"):
            log_data["batch_id"] = record.batch_id
        if hasattr(record, "object_type"):
            log_data["object_type"] = record.object_type
        if hasattr(record, "duration_seconds"):
            log_data["duration_seconds"] = record.duration_seconds

        context = getattr(record, "context", {})
        log_data.update(context)

        if record.exc_info:
            log_data["error"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1])
            }
        return json.dumps(log_data)

class LogContext:
    """Thread-local storage for log context."""
    _context = threading.local()
    
    @classmethod
    def get_context(cls) -> Dict[str, Any]:
        """Get the current context dictionary."""
        if not hasattr(cls._context, 'data'):
            cls._context.data = {}
        return cls._context.data
    
    @classmethod
    def set_context(cls, **kwargs):
        """Update the current context."""
        cls.get_context().update(kwargs)
    
    @classmethod
    def clear_context(cls):
        """Clear the current context."""
        if hasattr(cls._context, 'data'):
            cls._context.data.clear()

@contextmanager
def log_context(**kwargs):
    """Context manager for temporary logging context."""
    try:
        LogContext.set_context(**kwargs)
        yield
    finally:
        LogContext.clear_context()

@contextmanager
def log_performance(logger: logging.Logger, operation: str):
    """Context manager for performance logging."""
    start_time = time.time()
    try:
        yield
    finally:
        duration_ms = (time.time() - start_time) * 1000
        logger.info(
            f"{operation} completed",
            extra={
                'operation': operation,
                'duration_ms': duration_ms
            }
        )
# ------


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