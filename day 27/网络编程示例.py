# -*- coding: utf-8 -*-
import socket
server = socket.socket()
server.bind(('192.168.5.175',80))
server.listen(80)
server.listen(5)
conn,addr = server.accept()
data = conn.recv(1024)
print(data)
conn.send(b'duwei')
conn.close()
server.close()