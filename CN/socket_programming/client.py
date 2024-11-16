import socket

# Set up the server address and port
HOST = '192.168.1.9'  # Server's IP address
PORT = 20000        # Port to connect to (should match server)

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

intro_message=client_socket.recv(1024)
print(f"intro message from server:{intro_message.decode()}")

while True:
    message=input("enter a message for server:")
    client_socket.sendall(message.encode())
    if(message=="bye"):
        break
    server_message=client_socket.recv(1024)
    print(f"message from server: {server_message.decode()}")

print(f"last message from server:{client_socket.recv(1024).decode()}")
# Close the client socket
client_socket.close()
