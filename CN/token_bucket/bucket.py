import socket
import threading
import time

# Global bucket and its size limit
bucket_token_list = []
MAX_BUCKET_SIZE = 10
TIME_LAPSE = 3
lock = threading.Lock()  # as there is a shared resource (bucket_token_list) we need to use lock to ensure thread safety


def create_server_socket():
    host = '127.0.0.1'
    port = 50003

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started and listening on {host}:{port}")
    return server_socket


def add_token_to_bucket():
    
    while True:
        with lock:
            if(len(bucket_token_list)>=MAX_BUCKET_SIZE):
                print("Overflow of tokens")
            else:
                bucket_token_list.append(1)
            print(f"bucket:{bucket_token_list}")
        time.sleep(TIME_LAPSE)


def validate_token(client_socket):

    # while loop required to keep receiving data and adding it in bucket
    while True:
        try:
            incoming_data = client_socket.recv(1024).decode()
            if not incoming_data:
                continue

            print(f"Received: {incoming_data}")

            with lock:
                # Handle bucket overflow
                if len(bucket_token_list)==0:
                    overflow_message = f"token not available wait for token"
                    client_socket.send(overflow_message.encode())
                    print(overflow_message)
                    # time.sleep(TIME_LAPSE)
                else:
                    bucket_token_list.pop(0)
                    print(f"{incoming_data} received, token bucket:{bucket_token_list}")
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()


def start_server():
    server_socket = create_server_socket()

    # Start the bucket leaking thread
    threading.Thread(target=add_token_to_bucket, daemon=True).start()


    # while loop reqd to ensure connection does not close just after receiving single message
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        
        threading.Thread(target=validate_token, args=(client_socket,), daemon=True).start()   # The args parameter expects a tuple, but (client_socket) without a comma is treated as a single value

# Run the server
start_server()
