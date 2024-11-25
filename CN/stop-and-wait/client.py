import socket
import time 

HOST='192.168.29.225'
PORT=5000

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

while True:
    message=input("Enter message:")
    client_socket.send(message.encode())
    if message=='end':
        print("Client ended")
        break

    data=client_socket.recv(1024).decode()
    if(data=='ACK'):
        print(f"Acknowlegment received for :{data}")
        time.sleep(1)
    else:
        while data=='NACK':
            print(f"Acknowledge didnt received :{data} ")
            print(f"Resending :{message}")
            client_socket.send(message.encode())
            data=client_socket.recv(1024).decode()
            time.sleep(1)
        print(f"Acknowledgement received :{data}")
    
client_socket.close()