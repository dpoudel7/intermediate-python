import logging
import logging.config
import json
import time
import threading
import queue
from datetime import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
from contextlib import contextmanager


@dataclass
class SalesforceEvent:
    """Structured data for Salesforce events."""
    event_type: str
    org_id: str
    user_id: str
    operation: str
    status: str
    duration_ms: Optional[float] = None
    error_message: Optional[str] = None
    record_count: Optional[int] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values."""
        return {k: v for k, v in asdict(self).items() if v is not None}

class StructuredLogger:
    """Logger that handles structured data."""
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Setup JSON handler
        handler = logging.FileHandler('structured.log')
        handler.setFormatter(JsonFormatter())
        self.logger.addHandler(handler)
    
    def log_event(self, event: SalesforceEvent, level: int = logging.INFO):
        """Log a structured event."""
        self.logger.log(level, '', extra={'event': event.to_dict()})

class JsonFormatter(logging.Formatter):
    """Format log records as JSON."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format the log record as JSON."""
        data = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'logger': record.name
        }
        
        # Add event data if present
        if hasattr(record, 'event'):
            data['event'] = record.event
        else:
            data['message'] = record.getMessage()
        
        # Add exception info if present
        if record.exc_info:
            data['exception'] = self.formatException(record.exc_info)
        
        return json.dumps(data)

def demonstrate_structured_logging():
    """Demonstrate structured logging."""
    logger = StructuredLogger('salesforce.structured')
    
    # Log a successful sync event
    event = SalesforceEvent(
        event_type='sync',
        org_id='ORG123',
        user_id='USER456',
        operation='account_update',
        status='success',
        duration_ms=1234.56,
        record_count=100
    )
    logger.log_event(event)
    
    # Log a failed sync event
    error_event = SalesforceEvent(
        event_type='sync',
        org_id='ORG123',
        user_id='USER456',
        operation='contact_update',
        status='error',
        duration_ms=567.89,
        error_message='API timeout'
    )
    logger.log_event(error_event, level=logging.ERROR)

demonstrate_structured_logging()