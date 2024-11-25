import socket
import random
import time

HOST='0.0.0.0'
PORT=5000

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen()

conn,addr=server_socket.accept()

with conn:
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        if data=='end':
            print("Client ended connection")
            break
        if random.choice([True,False]):
            print(f"Recieved data:{data}")
            message="ACK"
            conn.send(message.encode())
            time.sleep(1)
        else:
            print("Packet lost")
            message="NACK"
            conn.send(message.encode())
            time.sleep(1)

server_socket.close()