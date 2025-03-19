"""
[CLIENT]                             [SERVER]
   |  create socket()                   |
   |----------------------------------->|  
   |          connect()                 |
   |----------------------------------->|  
   |          send()                    |
   |----------------------------------->|  
   |          recv()                    |
   |<-----------------------------------|  
   |          close()                   |
   |----------------------------------->|  

"""

# Import the socket module
import socket

# Print available socket families (address families)
print("Socket Families:")
print(f"IPv4 (AF_INET): {socket.AF_INET}")
print(f"IPv6 (AF_INET6): {socket.AF_INET6}")

# Print available socket types
print("\nSocket Types:")
print(f"TCP (SOCK_STREAM): {socket.SOCK_STREAM}")
print(f"UDP (SOCK_DGRAM): {socket.SOCK_DGRAM}")

# Create a TCP/IPv4 socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"\nTCP Socket created: {tcp_socket}")

# Create a UDP/IPv4 socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"UDP Socket created: {udp_socket}")

# Get hostname and IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"\nHostname: {hostname}")
print(f"IP Address: {ip_address}")

# Common ports and services
common_ports = {
    20: "FTP (data)",
    21: "FTP (control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP Alternate",
    27017: "MongoDB"
}

print("\nCommon Ports and Services:")
for port, service in common_ports.items():
    print(f"Port {port}: {service}")

# Don't forget to close sockets when done
tcp_socket.close()
udp_socket.close()
print("\nSockets closed")