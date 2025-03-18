#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCISE 3: LOGGING CONFIGURATION AND HANDLERS - SOLUTION

This solution demonstrates:
1. Advanced logging configuration with multiple handlers
2. Log rotation setup
3. Email notifications for critical errors
4. Custom formatters for different outputs
5. Configuration file management
"""

import logging
import logging.config
import logging.handlers
import time
import random
import json
import yaml
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

# -----------------------------------------------------------------------------
# Logging Configuration
# -----------------------------------------------------------------------------

def create_logging_config(email_settings: Dict[str, str]) -> Dict:
    """Create logging configuration dictionary."""
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s - %(levelname)s - %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - '
                         '%(pathname)s:%(lineno)d - %(message)s'
            },
            'json': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            },
            'file_debug': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'DEBUG',
                'formatter': 'detailed',
                'filename': 'debug.log',
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5
            },
            'file_error': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'ERROR',
                'formatter': 'detailed',
                'filename': 'error.log',
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5
            },
            'file_json': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'level': 'INFO',
                'formatter': 'json',
                'filename': 'metrics.json.log',
                'when': 'midnight',
                'interval': 1,
                'backupCount': 7
            },
            'email': {
                'class': 'logging.handlers.SMTPHandler',
                'level': 'CRITICAL',
                'formatter': 'detailed',
                'mailhost': email_settings['host'],
                'fromaddr': email_settings['from'],
                'toaddrs': email_settings['to'].split(','),
                'subject': 'Salesforce Monitoring Alert'
            }
        },
        'loggers': {
            'salesforce': {
                'level': 'DEBUG',
                'handlers': ['console', 'file_debug', 'file_error', 'file_json', 'email'],
                'propagate': False
            },
            'salesforce.service': {
                'level': 'DEBUG',
                'handlers': ['console', 'file_debug', 'file_error', 'file_json', 'email'],
                'propagate': False
            },
            'salesforce.sync': {
                'level': 'DEBUG',
                'handlers': ['console', 'file_debug', 'file_error', 'file_json', 'email'],
                'propagate': False
            }
        }
    }

def setup_logging():
    """Setup logging configuration."""
    # Email settings (in production, these would come from environment variables)
    email_settings = {
        'host': ('smtp.gmail.com', 587),
        'from': 'monitoring@example.com',
        'to': 'admin@example.com'
    }
    
    # Create configuration
    config = create_logging_config(email_settings)
    
    # Apply configuration
    logging.config.dictConfig(config)

# -----------------------------------------------------------------------------
# Business Logic
# -----------------------------------------------------------------------------

class ServiceStatus(Enum):
    """Possible statuses for Salesforce services."""
    HEALTHY = "Healthy"
    DEGRADED = "Degraded"
    DOWN = "Down"

@dataclass
class ServiceMetrics:
    """Metrics for a Salesforce service."""
    name: str
    status: ServiceStatus
    response_time_ms: float
    error_count: int
    success_rate: float
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for logging."""
        return {
            'name': self.name,
            'status': self.status.value,
            'response_time_ms': self.response_time_ms,
            'error_count': self.error_count,
            'success_rate': self.success_rate
        }

class SalesforceMonitor:
    """Monitors Salesforce services and API health."""
    
    def __init__(self):
        self.services = [
            "REST API",
            "Bulk API",
            "Streaming API",
            "Metadata API"
        ]
        self.logger = logging.getLogger('salesforce.service')
    
    def check_service_health(self, service: str) -> ServiceMetrics:
        """Check health of a specific service."""
        self.logger.info(f"Checking health of {service}")
        self.logger.debug(f"Starting health check for {service}")
        
        # Simulate service check
        time.sleep(0.5)
        
        # Simulate metrics
        response_time = random.uniform(100, 2000)  # ms
        error_count = random.randint(0, 10)
        success_rate = random.uniform(0.8, 1.0)
        
        # Determine status based on metrics
        if response_time > 1500 or success_rate < 0.9:
            status = ServiceStatus.DEGRADED
        elif response_time > 1800 or success_rate < 0.85:
            status = ServiceStatus.DOWN
        else:
            status = ServiceStatus.HEALTHY
        
        metrics = ServiceMetrics(
            name=service,
            status=status,
            response_time_ms=response_time,
            error_count=error_count,
            success_rate=success_rate
        )
        
        # Log results with appropriate levels
        self.logger.info(
            f"Service check completed for {service}",
            extra={'metrics': metrics.to_dict()}
        )
        
        self.logger.debug(
            f"Service metrics",
            extra={
                'service': service,
                'response_time': response_time,
                'success_rate': success_rate
            }
        )
        
        if status != ServiceStatus.HEALTHY:
            level = logging.CRITICAL if status == ServiceStatus.DOWN else logging.WARNING
            self.logger.log(
                level,
                f"Service {service} is {status.value}",
                extra={'metrics': metrics.to_dict()}
            )
        
        return metrics

class DataSyncMonitor:
    """Monitors data synchronization processes."""
    
    def __init__(self):
        self.sync_processes = {
            "accounts": {"interval_minutes": 60, "last_sync": None},
            "contacts": {"interval_minutes": 30, "last_sync": None},
            "opportunities": {"interval_minutes": 15, "last_sync": None}
        }
        self.logger = logging.getLogger('salesforce.sync')
    
    def check_sync_status(self) -> Dict[str, Dict]:
        """Check status of all sync processes."""
        self.logger.info("Starting sync status check")
        results = {}
        
        for process, config in self.sync_processes.items():
            self.logger.debug(f"Checking sync status for {process}")
            
            # Simulate check
            time.sleep(0.3)
            
            # Simulate sync status
            last_sync = config["last_sync"] or datetime.now()
            sync_age_minutes = (datetime.now() - last_sync).total_seconds() / 60
            is_overdue = sync_age_minutes > config["interval_minutes"]
            
            # Simulate sync health
            success_rate = random.uniform(0.7, 1.0)
            error_count = random.randint(0, 5)
            
            results[process] = {
                "last_sync": last_sync,
                "is_overdue": is_overdue,
                "success_rate": success_rate,
                "error_count": error_count
            }
            
            # Log status with appropriate levels
            self.logger.info(
                f"Sync status for {process}",
                extra={
                    'process': process,
                    'metrics': results[process]
                }
            )
            
            if is_overdue:
                self.logger.warning(
                    f"{process} sync is overdue",
                    extra={
                        'process': process,
                        'age_minutes': sync_age_minutes,
                        'interval': config["interval_minutes"]
                    }
                )
            
            if success_rate < 0.9:
                self.logger.warning(
                    f"{process} sync success rate is low",
                    extra={
                        'process': process,
                        'success_rate': success_rate
                    }
                )
            
            if error_count > 3:
                self.logger.error(
                    f"High error count in {process} sync",
                    extra={
                        'process': process,
                        'error_count': error_count
                    }
                )
        
        return results

def monitor_salesforce_health():
    """Main monitoring function."""
    logger = logging.getLogger('salesforce')
    
    try:
        logger.info("Starting Salesforce health monitoring")
        
        # Create monitors
        sf_monitor = SalesforceMonitor()
        sync_monitor = DataSyncMonitor()
        
        # Check service health
        logger.info("Checking Salesforce Service Health")
        critical_services = []
        
        for service in sf_monitor.services:
            metrics = sf_monitor.check_service_health(service)
            if metrics.status == ServiceStatus.DOWN:
                critical_services.append(metrics)
        
        # Check sync status
        logger.info("Checking Data Sync Status")
        sync_status = sync_monitor.check_sync_status()
        
        # Overall health check
        if critical_services:
            logger.critical(
                "Critical service failures detected",
                extra={'critical_services': [s.to_dict() for s in critical_services]}
            )
        
    except Exception as e:
        logger.critical(
            "Monitoring failed",
            exc_info=True,
            extra={'error': str(e)}
        )

def main():
    """Main entry point."""
    # Setup logging
    setup_logging()
    logger = logging.getLogger('salesforce')
    
    logger.info("Starting Salesforce monitoring service")
    
    while True:
        try:
            monitor_salesforce_health()
            time.sleep(60)  # Wait 1 minute before next check
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
            break
        except Exception as e:
            logger.error(
                "Error in monitoring loop",
                exc_info=True,
                extra={'error': str(e)}
            )
            time.sleep(60)  # Wait before retry

if __name__ == "__main__":
    main() 