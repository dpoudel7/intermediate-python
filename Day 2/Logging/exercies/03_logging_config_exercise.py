#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCISE 3: LOGGING CONFIGURATION AND HANDLERS

In this exercise, you'll improve the logging configuration for a
Salesforce integration monitoring system. The system needs to:
1. Log different levels to different destinations
2. Implement log rotation
3. Send critical errors via email
4. Format logs appropriately for each handler

Tasks:
1. Configure file-based logging with rotation
2. Setup email notifications for critical errors
3. Implement different formatters for different handlers
4. Create a configuration file for logging settings

The code below monitors Salesforce API health and data synchronization.
Your task is to implement proper logging configuration.
"""

import time
import random
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

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

class SalesforceMonitor:
    """Monitors Salesforce services and API health."""
    
    def __init__(self):
        self.services = [
            "REST API",
            "Bulk API",
            "Streaming API",
            "Metadata API"
        ]
        # TODO: Setup logging configuration here
    
    def check_service_health(self, service: str) -> ServiceMetrics:
        """Check health of a specific service."""
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
        
        # TODO: Replace prints with appropriate logging
        print(f"Service check completed for {service}")
        print(f"Status: {status.value}")
        print(f"Response Time: {response_time:.2f}ms")
        print(f"Success Rate: {success_rate*100:.1f}%")
        
        if status != ServiceStatus.HEALTHY:
            print(f"WARNING: Service {service} is {status.value}")
            if status == ServiceStatus.DOWN:
                print(f"CRITICAL: Service {service} is DOWN!")
        
        return metrics

class DataSyncMonitor:
    """Monitors data synchronization processes."""
    
    def __init__(self):
        self.sync_processes = {
            "accounts": {"interval_minutes": 60, "last_sync": None},
            "contacts": {"interval_minutes": 30, "last_sync": None},
            "opportunities": {"interval_minutes": 15, "last_sync": None}
        }
        # TODO: Setup logging configuration here
    
    def check_sync_status(self) -> Dict[str, Dict]:
        """Check status of all sync processes."""
        results = {}
        
        for process, config in self.sync_processes.items():
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
            
            # TODO: Replace prints with appropriate logging
            print(f"\nChecking sync status for {process}")
            print(f"Last sync: {last_sync}")
            print(f"Success rate: {success_rate*100:.1f}%")
            
            if is_overdue:
                print(f"WARNING: {process} sync is overdue!")
            if success_rate < 0.9:
                print(f"WARNING: {process} sync success rate is low!")
            if error_count > 3:
                print(f"ERROR: High error count in {process} sync!")
        
        return results

def monitor_salesforce_health():
    """Main monitoring function."""
    # Create monitors
    sf_monitor = SalesforceMonitor()
    sync_monitor = DataSyncMonitor()
    
    try:
        # Check service health
        print("\n=== Checking Salesforce Service Health ===")
        for service in sf_monitor.services:
            metrics = sf_monitor.check_service_health(service)
            
            if metrics.status == ServiceStatus.DOWN:
                # TODO: This should trigger email notification
                print(f"CRITICAL: Service {service} is DOWN!")
        
        # Check sync status
        print("\n=== Checking Data Sync Status ===")
        sync_status = sync_monitor.check_sync_status()
        
        # Overall health check
        critical_services = [m for m in metrics if m.status == ServiceStatus.DOWN]
        if critical_services:
            print("\nCRITICAL: Some services are DOWN!")
        
    except Exception as e:
        print(f"ERROR: Monitoring failed: {str(e)}")

def main():
    """Main entry point."""
    # TODO: Setup logging configuration here
    # Should include:
    # 1. Console output for INFO and above
    # 2. File output with rotation for DEBUG and above
    # 3. Error log file for ERROR and above
    # 4. Email notifications for CRITICAL
    
    while True:
        try:
            monitor_salesforce_health()
            time.sleep(60)  # Wait 1 minute before next check
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
            break
        except Exception as e:
            print(f"ERROR: {str(e)}")
            time.sleep(60)  # Wait before retry

if __name__ == "__main__":
    main() 