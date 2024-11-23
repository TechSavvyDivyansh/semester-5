import socket
import time
import sys
import select

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080


def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()
    print(f"Server started and listening on {SERVER_HOST}:{SERVER_PORT}")
    return server_socket


def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if "connection closed" in data or not data :
                print("Client requested to close the connection.")
                break

            print(f"Received frame: {data}")


            # Simulating user input for NACK or timeout
            print("Press 1 and Enter to simulate NACK, or wait for timeout to send ACK:")
            start_time = time.time()

            user_input = None
            while time.time() - start_time < 2:
                user_input = input() if input_ready() else None
                if user_input == "1":
                    break

            if user_input == "1":
                print("Sending NACK")
                client_socket.send("NACK".encode())
            else:
                print("Timeout! Sending ACK")
                client_socket.send("ACK".encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed with the client.")


def input_ready():
    # Check if there is input ready on stdin.
    return select.select([sys.stdin], [], [], 0)[0]
    # sys.stdin is for getting all sources which hve readiness to read input, rest 2 parameters are not reqd here hence empty list . 0 so that it checks for 0s if input is there or not so that system is not blocked for input . [0] at last to ensure that only read input souces(rlist) are returned and not wlist and xlist 


def start_server():
    # Main server logic.
    server_socket = create_server_socket()
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            # threading.Thread(target=handle_client, args=(client_socket,)).start()
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    finally:
        server_socket.close()


start_server()
