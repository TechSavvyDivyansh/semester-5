import socket

# Set up the server address and port
HOST = '192.168.1.9'  # Server's IP address
PORT = 50000        # Port to connect to (should match server)

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send a message to the server
client_socket.sendall(b"Hello, server! This is a client.")

# Receive the server's response
data = client_socket.recv(1024)

# Print the response
print(f"Received from server: {data.decode()}")

code='@'

while(code!="#"):
    message=input("enter a message for server:")
    client_socket.sendall(message.encode())
    if(message == '#'):
        code='#'

# Receive response from server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# Close the client socket
client_socket.close()
