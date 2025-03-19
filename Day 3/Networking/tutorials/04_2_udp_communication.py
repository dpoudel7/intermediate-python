import socket
import time
import random


def create_udp_client():
    """Create a simple UDP client."""
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set a timeout for receiving responses (if any)
    client_socket.settimeout(1.0)
    
    # Server address
    server_address = ('localhost', 12345)
    
    try:
        # Send multiple datagrams
        for i in range(5):
            # Create a message
            message = f"UDP Datagram #{i+1} - Timestamp: {time.time()}"
            
            # Send the datagram
            print(f"Sending: {message}")
            client_socket.sendto(message.encode('utf-8'), server_address)
            
            # Maybe wait for a response (not required in UDP)
            try:
                data, server = client_socket.recvfrom(1024)
                print(f"Received response: {data.decode('utf-8')}")
            except socket.timeout:
                print("No response received (this is normal in UDP)")
            
            # Wait before sending next datagram
            time.sleep(0.5)
            
    finally:
        # Clean up
        client_socket.close()
        print("Client socket closed")

# For educational purposes, call the demonstration function
create_udp_client()

# Note: To actually run the UDP server and client, you would need separate processes:
# In one terminal: python -c "from 04_udp_communication import create_udp_server; create_udp_server()"
# In another: python -c "from 04_udp_communication import create_udp_client; create_udp_client()"