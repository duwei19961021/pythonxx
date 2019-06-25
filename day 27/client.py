# -*- coding: utf-8 -*-
import socket
sk = socket.socket()
sk.connect(('192.168.5.175',80))
name = input(">>>:")
sk.send(name.encode('utf-8'))
response = sk.recv(1024)
print(response.decode('utf-8'))
sk.close()