#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCISE 2: IMPLEMENTING STRUCTURED AND CONTEXTUAL LOGGING - SOLUTION

This solution demonstrates:
1. Structured logging for batch operations
2. Contextual logging for tracking batch processing
3. Custom log formatters for different outputs
4. Performance logging
5. Proper error context in logs
"""

import logging
import time
import random
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum
from contextlib import contextmanager
import threading

# -----------------------------------------------------------------------------
# Logging Setup
# -----------------------------------------------------------------------------

class JsonFormatter(logging.Formatter):
    """Format log records as JSON."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format the log record as JSON."""
        # Get the regular formatted message
        message = super().format(record)
        
        # Create the base log record
        log_data = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'logger': record.name,
            'message': message
        }
        
        # Add extra fields from the record
        if hasattr(record, 'batch_id'):
            log_data['batch_id'] = record.batch_id
        if hasattr(record, 'object_type'):
            log_data['object_type'] = record.object_type
        if hasattr(record, 'duration_ms'):
            log_data['duration_ms'] = record.duration_ms
        
        # Add any extra contextual information
        context = getattr(record, 'context', {})
        if context:
            log_data['context'] = context
        
        # Add exception info if present
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
        
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

# -----------------------------------------------------------------------------
# Business Logic
# -----------------------------------------------------------------------------

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
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for logging."""
        return {
            'object_type': self.object_type.value,
            'batch_size': self.batch_size,
            'timeout_seconds': self.timeout_seconds,
            'max_retries': self.max_retries
        }

@dataclass
class BatchMetrics:
    """Metrics for batch processing."""
    total_records: int
    successful: List[str]
    failed: List[str]
    start_time: datetime
    end_time: Optional[datetime] = None
    duration_seconds: Optional[float] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for logging."""
        return {
            'total_records': self.total_records,
            'successful_count': len(self.successful),
            'failed_count': len(self.failed),
            'duration_seconds': self.duration_seconds,
            'failed_records': self.failed
        }

class BatchProcessor:
    """Processes Salesforce objects in batches."""
    
    def __init__(self, config: BatchConfig):
        self.config = config
        self.logger = self._setup_logger()
        self.batch_id = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    def _setup_logger(self) -> logging.Logger:
        """Setup logging for the batch processor."""
        logger = logging.getLogger(f'salesforce.batch.{self.config.object_type.value.lower()}')
        logger.setLevel(logging.DEBUG)
        
        # Console handler with simple format
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - [%(object_type)s] %(message)s'
        )
        console_handler.setFormatter(console_format)
        
        # File handler with JSON format
        file_handler = logging.FileHandler(
            f'batch_{self.config.object_type.value.lower()}.json.log'
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(JsonFormatter())
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
        return logger
    
    def process_batch(self, records: List[Dict]) -> Dict[str, Any]:
        """Process a batch of records."""
        with log_context(batch_id=self.batch_id, object_type=self.config.object_type.value):
            self.logger.info(
                f"Starting batch processing",
                extra={'record_count': len(records)}
            )
            
            metrics = BatchMetrics(
                total_records=len(records),
                successful=[],
                failed=[],
                start_time=datetime.now()
            )
            
            with log_performance(self.logger, "batch_processing"):
                for record in records:
                    try:
                        if self._process_record(record):
                            metrics.successful.append(record['id'])
                        else:
                            metrics.failed.append(record['id'])
                    except Exception as e:
                        self.logger.error(
                            f"Error processing record",
                            exc_info=True,
                            extra={
                                'record_id': record['id'],
                                'error': str(e)
                            }
                        )
                        metrics.failed.append(record['id'])
            
            # Update metrics
            metrics.end_time = datetime.now()
            metrics.duration_seconds = (metrics.end_time - metrics.start_time).total_seconds()
            
            # Log completion
            self.logger.info(
                f"Batch processing completed",
                extra={
                    'metrics': metrics.to_dict(),
                    'config': self.config.to_dict()
                }
            )
            
            # Log warning if there were failures
            if metrics.failed:
                self.logger.warning(
                    f"Some records failed processing",
                    extra={'failed_records': metrics.failed}
                )
            
            return metrics.to_dict()
    
    def _process_record(self, record: Dict) -> bool:
        """Process a single record."""
        with log_context(record_id=record['id']):
            self.logger.debug(
                f"Processing record",
                extra={'record_data': record}
            )
            
            try:
                with log_performance(self.logger, "record_processing"):
                    # Simulate processing
                    time.sleep(0.1)
                    
                    # Simulate random failures
                    if random.random() < 0.1:  # 10% chance of failure
                        raise Exception(f"Random processing failure")
                    
                    self.logger.debug(
                        f"Record processed successfully",
                        extra={'record_id': record['id']}
                    )
                    return True
                    
            except Exception as e:
                self.logger.error(
                    f"Failed to process record",
                    exc_info=True,
                    extra={
                        'record_id': record['id'],
                        'error': str(e)
                    }
                )
                return False

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
    # Setup root logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('salesforce.batch')
    
    logger.info("Starting batch processing demonstration")
    
    # Process different types of objects
    for object_type in ObjectType:
        with log_context(object_type=object_type.value):
            logger.info(f"Processing {object_type.value} records")
            
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
                    with log_context(batch_number=i//config.batch_size + 1):
                        processor.process_batch(batch)
                except Exception as e:
                    logger.error(
                        "Error processing batch",
                        exc_info=True,
                        extra={'batch_number': i//config.batch_size + 1}
                    )
    
    logger.info("Batch processing demonstration completed")

if __name__ == "__main__":
    main() 