import socket
import time
import random

# Print explanation of what's happening
print("TCP COMMUNICATION DEMONSTRATION")
print("-------------------------------")
print("TCP ensures reliable, ordered, and error-checked delivery of data.")
print("This demonstration will show key TCP features in action.\n")

# Simulate TCP 3-way handshake
print("1. TCP THREE-WAY HANDSHAKE")
print("   Client: SYN - 'Hello, can we talk?'")
time.sleep(0.5)
print("   Server: SYN-ACK - 'Yes, I'm ready to talk, are you?'")
time.sleep(0.5)
print("   Client: ACK - 'Yes, I'm ready too. Connection established!'")
time.sleep(0.5)
print("   [Connection Established]\n")

# Create a simple message to send
message = "Important business data: Customer ID=12345, Order Total=$532.50, Status=Pending"
print(f"2. PREPARING TO SEND: '{message}'")

# Simulate breaking message into segments/packets
segments = []
segment_size = 20
for i in range(0, len(message), segment_size):
    segments.append(message[i:i+segment_size])

print(f"   Breaking message into {len(segments)} segments for transmission")
for i, segment in enumerate(segments):
    print(f"   Segment {i+1}: '{segment}'")
print()

# Simulate sending segments with acknowledgments
print("3. DATA TRANSMISSION WITH ACKNOWLEDGMENTS")
for i, segment in enumerate(segments):
    # Simulate random delay to show TCP handles timing variations
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    
    print(f"   Sending segment {i+1}: '{segment}'")
    time.sleep(0.1)
    
    # Simulate potential packet loss (uncomment to demonstrate retransmission)
    if i == 1 and random.random() < 0.3:  # 30% chance of "losing" the 2nd segment
        print(f"   [Segment {i+1} lost in transmission!]")
        time.sleep(0.5)
        print(f"   [Timeout detected]")
        print(f"   Resending segment {i+1}: '{segment}'")
        time.sleep(0.1)
    
    # Simulate acknowledgment
    print(f"   Received ACK for segment {i+1}")
print()

# Simulate flow control
print("4. FLOW CONTROL")
print("   Server: 'Please slow down, my buffer is getting full'")
print("   Client: 'Adjusting transmission rate'")
time.sleep(0.5)
print("   [Transmission rate adjusted]\n")

# Show connection termination
print("5. CONNECTION TERMINATION (Four-way handshake)")
print("   Client: FIN - 'I'm done sending data'")
time.sleep(0.3)
print("   Server: ACK - 'Got it, you're done'")
time.sleep(0.3)
print("   Server: FIN - 'I'm also done'")
time.sleep(0.3)
print("   Client: ACK - 'Acknowledged, closing connection'")
time.sleep(0.3)
print("   [Connection Closed]\n")

# Explain benefits demonstrated
print("TCP FEATURES DEMONSTRATED:")
print("1. Connection establishment (3-way handshake)")
print("2. Breaking data into manageable segments")
print("3. Acknowledgment of received data")
print("4. Retransmission of lost data")
print("5. Flow control to prevent overwhelming receiver")
print("6. Orderly connection termination")
