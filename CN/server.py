import socket

HOST='192.168.1.9'
PORT=50000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))


server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}...")


conn, addr = server_socket.accept()
print(f"Connected by {addr}")



with conn:
    while True:
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received from client: {data.decode()}")


        conn.sendall(b"Hello, client! Message received.")

# Close the server socket
server_socket.close()