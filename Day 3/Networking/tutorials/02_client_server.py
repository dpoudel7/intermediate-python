import socket
import time

# First, let's define a simple echo server that repeats back what it receives
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow reuse of the address (useful for development)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Define the server address (hostname, port)
    server_address = ('localhost', 12345)
    
    # Bind the socket to the address
    server_socket.bind(server_address)
    
    # Listen for incoming connections (queue up to 5 requests)
    server_socket.listen(5)
    
    print(f"Server listening on {server_address}")
    
    try:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Receive and echo data
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
        
        # Add a small delay to simulate processing
        time.sleep(1)
        
        # Echo the data back
        client_socket.send(data)
        print("Sent data back to client")
        
        # Close the client connection
        client_socket.close()
        print("Client connection closed")
        
    finally:
        # Always close the server socket
        server_socket.close()
        print("Server socket closed")

# Now, let's define a simple client that sends a message to the server
def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address to connect to
    server_address = ('localhost', 12345)
    
    try:
        # Connect to the server
        client_socket.connect(server_address)
        print(f"Connected to server at {server_address}")
        
        # Send a message
        message = "Hello from the client!"
        client_socket.send(message.encode('utf-8'))
        print(f"Sent: {message}")
        
        # Receive a response
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
        
    finally:
        # Always close the socket
        client_socket.close()
        print("Client socket closed")

# Note: To run this properly, you would need to run the server and client in separate processes
# For demonstration, we could uncomment one of these:
# start_server()
# start_client()

# For educational purposes, we can print the steps
print("Server Steps:")
print("1. Create socket")
print("2. Bind to address")
print("3. Listen for connections")
print("4. Accept connection")
print("5. Receive data")
print("6. Process data")
print("7. Send response")
print("8. Close connection")

print("\nClient Steps:")
print("1. Create socket")
print("2. Connect to server")
print("3. Send data")
print("4. Receive response")
print("5. Process response")
print("6. Close connection")