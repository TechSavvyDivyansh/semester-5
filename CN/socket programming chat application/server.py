import socket

HOST='192.168.1.9'
PORT=20000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))


server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}...")


conn, addr = server_socket.accept()
print(f"Connected by {addr}")

conn.sendall(b"hello client server here")


with conn:
    while True:
        
        # Receive data from the client
        data = conn.recv(1024)
        if not data or data.decode()=="bye":
            print("server has left communication")
            conn.sendall(b"bye client")
            break
        print(f"Received from client: {data.decode()}")

        message=input("enter message for client:")
        conn.sendall(message.encode())
# Close the server socket
server_socket.close()