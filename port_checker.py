
import socket

# Get system IP address
host = input("Enter IP address: ")

# Get port number
port = int(input("Enter port number: "))

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set timeout
s.settimeout(3)

# Check port status
result = s.connect_ex((host, port))

if result == 0:
    print("Port", port, "is OPEN")
else:
    print("Port", port, "is CLOSED")

s.close()
