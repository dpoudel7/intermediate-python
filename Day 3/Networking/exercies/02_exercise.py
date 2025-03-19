
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
# EXERCISE 2: SIMPLE ECHO SERVER
# -----------------------------------------------------------------------------

"""
In this exercise, you'll create a simple echo server that:
1. Listens for incoming TCP connections
2. Accepts and handles multiple clients
3. Echoes back any received data
4. Implements proper connection handling and cleanup

This exercise helps understand socket programming fundamentals.
"""

class EchoServer:
    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
    
    # TODO: Implement the server start method
    # The method should:
    # - Create and configure the server socket
    # - Bind to the specified host and port
    # - Listen for incoming connections
    # - Handle multiple clients using threading
    def start(self):
        pass
    
    # TODO: Implement the client handler method
    # The method should:
    # - Receive data from the client
    # - Echo the data back to the client
    # - Handle client disconnection
    # - Clean up the connection
    def handle_client(self, client_socket: socket.socket, address: tuple):
        pass
    
    def stop(self):
        """Stop the echo server."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()




def test_echo_server():
    """Test the EchoServer implementation."""
    server = EchoServer()
    server_thread = threading.Thread(target=server.start)
    server_thread.daemon = True
    server_thread.start()
    
    # Test client connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))
    
    # Send and receive data
    message = b"Hello, Echo Server!"
    client_socket.send(message)
    response = client_socket.recv(1024)
    
    assert response == message, "Echo response doesn't match"
    
    client_socket.close()
    server.stop()

test_echo_server()