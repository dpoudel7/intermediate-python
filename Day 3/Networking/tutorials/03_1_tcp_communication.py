import socket
import time
import random


def create_tcp_client():
    """Create a simple TCP client."""
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server
    server_address = ('localhost', 12345)
    print(f"Connecting to {server_address}")
    client_socket.connect(server_address)
    
    try:
        # Send data in chunks to demonstrate ordered delivery
        message = "This is a test message showing TCP reliable delivery mechanisms in action."
        chunk_size = 16
        
        for i in range(0, len(message), chunk_size):
            chunk = message[i:i+chunk_size]
            client_socket.send(chunk.encode('utf-8'))
            print(f"Sent chunk: {chunk}")
            
            # Wait for acknowledgment
            ack = client_socket.recv(1024)
            print(f"Received: {ack.decode('utf-8')}")
            time.sleep(0.5)  # Pause between sends to make it clearer
            
    finally:
        # Clean up
        client_socket.close()

# For educational purposes, call the demonstration function
create_tcp_server()

# Note: To actually run the TCP server and client, you would need separate processes:
# In one terminal: python -c "from 03_tcp_communication import create_tcp_server; create_tcp_server()"
# In another: python -c "from 03_tcp_communication import create_tcp_client; create_tcp_client()"