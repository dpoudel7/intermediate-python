import time
import random
import logging
from contextlib import contextmanager
from typing import List, Dict, Any, Optional, Generator

# -----------------------------------------------------------------------------
# Mock Cloud Storage Service
# -----------------------------------------------------------------------------

class CloudStorageError(Exception):
    """Base exception for cloud storage operations."""
    pass

class ConnectionError(CloudStorageError):
    """Raised when connection fails."""
    pass

class TransactionError(CloudStorageError):
    """Raised when transaction fails."""
    pass

class CloudStorage:
    """Mock cloud storage service."""
    
    def __init__(self):
        self.connected = False
        self.files: Dict[str, bytes] = {}
        self.transaction_active = False
        self.transaction_changes: Dict[str, bytes] = {}
    
    def connect(self) -> None:
        """Simulate connecting to the service."""
        if random.random() < 0.1:  # 10% chance of connection failure
            raise ConnectionError("Failed to connect to cloud storage")
        self.connected = True
    
    def disconnect(self) -> None:
        """Simulate disconnecting from the service."""
        self.connected = False
    
    def begin_transaction(self) -> None:
        """Start a new transaction."""
        if not self.connected:
            raise CloudStorageError("Not connected")
        if self.transaction_active:
            raise TransactionError("Transaction already in progress")
        self.transaction_active = True
        self.transaction_changes.clear()
    
    def commit_transaction(self) -> None:
        """Commit the current transaction."""
        if not self.transaction_active:
            raise TransactionError("No transaction in progress")
        if random.random() < 0.1:  # 10% chance of commit failure
            raise TransactionError("Failed to commit transaction")
        self.files.update(self.transaction_changes)
        self.transaction_active = False
        self.transaction_changes.clear()
    
    def rollback_transaction(self) -> None:
        """Rollback the current transaction."""
        if not self.transaction_active:
            raise TransactionError("No transaction in progress")
        self.transaction_active = False
        self.transaction_changes.clear()
    
    def upload_file(self, name: str, content: bytes) -> None:
        """Upload a file to the storage."""
        if not self.connected:
            raise CloudStorageError("Not connected")
        if random.random() < 0.1:  # 10% chance of upload failure
            raise CloudStorageError(f"Failed to upload {name}")
        if self.transaction_active:
            self.transaction_changes[name] = content
        else:
            self.files[name] = content
    
    def download_file(self, name: str) -> bytes:
        """Download a file from the storage."""
        if not self.connected:
            raise CloudStorageError("Not connected")
        if random.random() < 0.1:  # 10% chance of download failure
            raise CloudStorageError(f"Failed to download {name}")
        if name not in self.files:
            raise CloudStorageError(f"File not found: {name}")
        return self.files[name]


# -----------------------------------------------------------------------------
# EXERCISE 1: Implement Connection Manager
# -----------------------------------------------------------------------------

# TODO: Implement a context manager for cloud storage connections
# The manager should:
# 1. Connect to the service on enter
# 2. Disconnect on exit
# 3. Handle connection errors appropriately
# 4. Ensure disconnection happens even if errors occur

class CloudStorageConnection:
    """Context manager for cloud storage connections."""
    
    def __init__(self, storage: CloudStorage):
        self.storage = storage
    
    def __enter__(self):
        # TODO: Implement connection logic
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Implement disconnection logic
        pass