# -*- coding: utf-8 -*-
import socket
server = socket.socket()
server.bind(('192.168.5.175',80))
server.listen(5)
while True:
    conn,addr = server.accept()
    print("来了老弟")
    data = conn.recv(1024)
    response = data + b'sb'
    conn.send(response)