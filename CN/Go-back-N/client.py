import socket
import time


def join_socket():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8080
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")
    return client_socket



def client_logic(client_socket):
    base = 0
    retransmit_index = -1                                   # Keeps track of the frame index to retransmit from
    start_time = None                                       # To track custom timer
    data_list = [i for i in range(1, 10)]        # Frames: 1 to 9
    CUSTOM_TIMER = 3                                        # Seconds

    try:
        while base < len(data_list):
            if retransmit_index != -1 and start_time is None:
                
                start_time = time.time()                    # Start custom timer when NACK is received

            frame = f"{data_list[base]}"         # Frame starts from index + 1
            client_socket.send(frame.encode())              # Send frame to the server
            print(f"Sent frame: {frame}")

            try:
                client_socket.settimeout(2)                 # Timeout for ACK/NACK
                response = client_socket.recv(1024).decode()

                if response == "ACK":
                    print(f"Received ACK for frame {base + 1}")
                    base += 1                               # Move to the next frame
                elif response == "NACK":
                    retransmit_index = base + 1             # Set retransmission starting point
                    base += 1                               # Continue sending frames in sequence

            except socket.timeout:
                print("Timeout! Assuming ACK implicitly.")
                base += 1                                   # Move to the next frame

            # If custom timer expires, retransmit from retransmit_index
            if retransmit_index != -1 and start_time is not None and time.time() - start_time >= CUSTOM_TIMER:
                print(f"Received NACK for frame {retransmit_index} \nRetransmitting frames starting from {retransmit_index}")
                base = retransmit_index - 1  # Reset base to retransmit_index for retransmission
                retransmit_index = -1  # Reset retransmit_index
                start_time = None  # Reset timer
            
            print("")

        print("All frames sent successfully.")

        
    finally:
        client_socket.send("connection closed".encode())
        client_socket.close()
        print("Connection closed.")


def start_client():
    socket=join_socket()
    client_logic(socket)



if __name__ == "__main__":
    start_client()