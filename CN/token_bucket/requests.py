import socket

def create_client_socket():
    
    host='127.0.0.1'
    port=50003

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")
    return client_socket

def communicate_with_server(client_socket):
    try:
        while True:
            data=input("Enter the data:")
            
            if(data=="exit"):
                break 


            client_socket.send(data.encode())
    finally:
        client_socket.close()

def start_client():
    client_socket = create_client_socket()
    communicate_with_server(client_socket)

# Run the client
start_client()
