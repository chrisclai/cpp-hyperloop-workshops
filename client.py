import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 1234

s.connect((HOST, PORT)) # to connect to the server

while True:
    print("Enter in a message to send to the server!: ")
    msgToSend = input()
    msg = s.send(bytes(msgToSend, 'utf-8'))
    time.sleep(1)
    msg = s.recv(1024).decode('utf-8')
    print(msg)