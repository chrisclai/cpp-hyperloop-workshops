import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 1234

s.bind((HOST, PORT))
s.listen(1)

while True:
    clientsocket, address = s.accept()
    print(f"Server Established on {address}!")
    while True:
        msg = s.recv(1024).decode('utf-8')
        print(msg)
        time.sleep(1)
        s.send(bytes(msg, 'utf-8')) #encode msg
