import socket
import time
import random

# Create actual UDP example functions
def create_udp_server():
    """Create a simple UDP server."""
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind to localhost port 12345
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    print(f"UDP Server listening on {server_address}")
    
    try:
        # Set a timeout to simulate working with unreliable UDP
        server_socket.settimeout(3.0)
        
        # Listen for incoming datagrams
        print("Waiting for datagrams...")
        
        # Count received datagrams
        count = 0
        start_time = time.time()
        
        # Listen for a few seconds
        while time.time() - start_time < 5:
            try:
                # Receive a datagram
                data, client_address = server_socket.recvfrom(1024)
                count += 1
                
                print(f"Received datagram {count} from {client_address}: {data.decode('utf-8')}")
                
                # Unlike TCP, we don't automatically send a response
                # But we could send one if the application protocol requires it
                if random.random() < 0.7:  # 70% chance to respond (simulating optional response)
                    response = f"Got your message #{count}"
                    server_socket.sendto(response.encode('utf-8'), client_address)
                    print(f"Sent response: {response}")
                
            except socket.timeout:
                print("Timed out waiting for datagram")
                continue
        
    finally:
        # Clean up
        server_socket.close()
        print("Server socket closed")

# For educational purposes, call the demonstration function
create_udp_server()

# Note: To actually run the UDP server and client, you would need separate processes:
# In one terminal: python -c "from 04_udp_communication import create_udp_server; create_udp_server()"
# In another: python -c "from 04_udp_communication import create_udp_client; create_udp_client()"