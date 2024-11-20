import socket
import threading
import time

# Global bucket and its size limit
bucket_list = []
MAX_BUCKET_SIZE = 10
TIME_LAPSE=3
lock = threading.Lock()  # as there is a shared resource (bucket_list) we need to use lock to ensure thread safety


def create_server_socket():
    host = '127.0.0.1'
    port = 50003

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started and listening on {host}:{port}")
    return server_socket


def leak_items_from_bucket():
    global bucket_list
    while True:
        with lock:
            if bucket_list:
                print(f"Popped value: {bucket_list.pop(0)}")
            else:
                print("Bucket is empty. Waiting for input...")

            print(f"Current bucket: {bucket_list}")
        time.sleep(TIME_LAPSE)


def add_items_to_bucket(client_socket):
    global bucket_list


    # while loop required to keep receiving data and adding it in bucket
    while True:
        try:
            incoming_data = client_socket.recv(1024).decode()
            if not incoming_data:
                continue

            print(f"Received: {incoming_data}")

            with lock:
                # Handle bucket overflow
                if len(bucket_list) >= MAX_BUCKET_SIZE:
                    overflow_message = f"Bucket is overflowing, please wait for {TIME_LAPSE} seconds and press enter"
                    client_socket.send(overflow_message.encode())
                    print("overflowed")
                    # time.sleep(TIME_LAPSE)
                else:
                    bucket_list.append(int(incoming_data))  # Convert incoming data to integer
                    print(f"Updated bucket: {bucket_list}")
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()


def start_server():
    server_socket = create_server_socket()

    # Start the bucket leaking thread
    threading.Thread(target=leak_items_from_bucket, daemon=True).start()


    # while loop reqd to ensure connection does not close just after receiving single message
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        
        threading.Thread(target=add_items_to_bucket, args=(client_socket,), daemon=True).start()   # The args parameter expects a tuple, but (client_socket) without a comma is treated as a single value

# Run the server
start_server()
