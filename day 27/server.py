# -*- coding: utf-8 -*-
import socket
server = socket.socket()
server.bind(('192.168.5.175',80))
server.listen(5)
while True:
    conn,addr = server.accept()
    while True:
        data = conn.recv(1024)
        if data == b'exit':
            break
        response = data + b'sb'
        conn.send(response)
    conn.close()