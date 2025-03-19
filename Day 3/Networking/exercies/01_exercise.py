#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NETWORK PROGRAMMING EXERCISES

This file contains exercises that build on the concepts covered in the theory and
tutorial sections. Each exercise focuses on a specific aspect of network programming
and increases in complexity.

Instructions:
1. Complete the TODO sections in each exercise
2. Run the tests to verify your implementation
3. Review the solution after attempting the exercise

Note: These exercises are designed for Salesforce developers with 3-6 months
Python experience and focus on real-world scenarios they might encounter.
"""

import socket
import json
import requests
import threading
from typing import Dict, List, Any, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# -----------------------------------------------------------------------------
# EXERCISE 1: BASIC HTTP CLIENT
# -----------------------------------------------------------------------------

"""
In this exercise, you'll create a simple HTTP client that can:
1. Make GET and POST requests
2. Handle different response types
3. Implement proper error handling
4. Support custom headers

This is a fundamental skill for working with web services and APIs.
"""

class SimpleHTTPClient:
    def __init__(self):
        self.session = requests.Session()
    
    # TODO: Implement a method to make GET requests
    # The method should:
    # - Accept a URL and optional parameters
    # - Handle different response types (json, text)
    # - Implement proper error handling
    # - Return the processed response
    def get(self, url: str, params: Optional[Dict] = None) -> Any:
        pass
    
    # TODO: Implement a method to make POST requests
    # The method should:
    # - Accept a URL, data, and optional headers
    # - Support both form data and JSON payloads
    # - Implement proper error handling
    # - Return the processed response
    def post(self, url: str, data: Dict, headers: Optional[Dict] = None) -> Any:
        pass


def test_http_client():
    """Test the SimpleHTTPClient implementation."""
    client = SimpleHTTPClient()
    
    # Test GET request
    response = client.get('https://httpbin.org/get', params={'test': 'value'})
    assert response is not None, "GET request failed"
    
    # Test POST request
    data = {'key': 'value'}
    response = client.post('https://httpbin.org/post', data=data)
    assert response is not None, "POST request failed"
