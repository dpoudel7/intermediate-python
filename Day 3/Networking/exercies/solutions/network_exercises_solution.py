#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NETWORK PROGRAMMING EXERCISES - SOLUTIONS

This file contains complete solutions to the network programming exercises.
Each solution includes detailed comments explaining the implementation and
key concepts.

Note: These solutions demonstrate best practices and proper error handling,
but in a real-world scenario, you might need to add more robust error
handling and logging.
"""

import socket
import json
import requests
import threading
import time
import hmac
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import logging
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# -----------------------------------------------------------------------------
# EXERCISE 1: BASIC HTTP CLIENT - SOLUTION
# -----------------------------------------------------------------------------

class SimpleHTTPClient:
    def __init__(self):
        # Use a session for connection pooling and cookie persistence
        self.session = requests.Session()
        
        # Set default headers and timeouts
        self.session.headers.update({
            'User-Agent': 'SimpleHTTPClient/1.0',
            'Accept': 'application/json, text/plain'
        })
    
    def get(self, url: str, params: Optional[Dict] = None) -> Any:
        """
        Make a GET request to the specified URL.
        
        Args:
            url: The target URL
            params: Optional query parameters
            
        Returns:
            The processed response (JSON or text)
            
        Raises:
            requests.exceptions.RequestException: If the request fails
        """
        try:
            # Make the request with timeout
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            # Process response based on content type
            content_type = response.headers.get('Content-Type', '')
            
            if 'application/json' in content_type:
                return response.json()
            else:
                return response.text
                
        except requests.exceptions.Timeout:
            logging.error(f"Request to {url} timed out")
            raise
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error occurred: {e}")
            raise
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            raise
    
    def post(self, url: str, data: Dict, headers: Optional[Dict] = None) -> Any:
        """
        Make a POST request to the specified URL.
        
        Args:
            url: The target URL
            data: The data to send
            headers: Optional custom headers
            
        Returns:
            The processed response (JSON or text)
            
        Raises:
            requests.exceptions.RequestException: If the request fails
        """
        try:
            # Determine if we're sending JSON or form data
            if headers and headers.get('Content-Type') == 'application/json':
                response = self.session.post(
                    url,
                    json=data,
                    headers=headers,
                    timeout=10
                )
            else:
                response = self.session.post(
                    url,
                    data=data,
                    headers=headers,
                    timeout=10
                )
            
            response.raise_for_status()
            
            # Process response based on content type
            content_type = response.headers.get('Content-Type', '')
            
            if 'application/json' in content_type:
                return response.json()
            else:
                return response.text
                
        except requests.exceptions.Timeout:
            logging.error(f"Request to {url} timed out")
            raise
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error occurred: {e}")
            raise
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            raise

# -----------------------------------------------------------------------------
# EXERCISE 2: SIMPLE ECHO SERVER - SOLUTION
# -----------------------------------------------------------------------------

class EchoServer:
    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
    
    def start(self):
        """
        Start the echo server and listen for connections.
        
        This method:
        1. Creates and configures the server socket
        2. Binds to the specified host and port
        3. Listens for incoming connections
        4. Handles each client in a separate thread
        """
        try:
            # Create TCP socket
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Allow address reuse
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Bind and listen
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True
            
            logging.info(f"Echo server listening on {self.host}:{self.port}")
            
            while self.running:
                try:
                    # Accept new connection
                    client_socket, address = self.server_socket.accept()
                    logging.info(f"New connection from {address}")
                    
                    # Handle client in separate thread
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                    
                except socket.error as e:
                    if self.running:  # Only log if we're still supposed to be running
                        logging.error(f"Error accepting connection: {e}")
                    
        except Exception as e:
            logging.error(f"Server error: {e}")
            self.stop()
    
    def handle_client(self, client_socket: socket.socket, address: tuple):
        """
        Handle a client connection by echoing received data.
        
        Args:
            client_socket: The client's socket
            address: The client's address
        """
        try:
            while True:
                # Receive data
                data = client_socket.recv(1024)
                if not data:
                    break  # Client disconnected
                
                # Echo data back
                client_socket.send(data)
                
        except socket.error as e:
            logging.error(f"Error handling client {address}: {e}")
            
        finally:
            client_socket.close()
            logging.info(f"Connection closed for {address}")
