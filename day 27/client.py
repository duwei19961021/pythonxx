# -*- coding: utf-8 -*-
# import socket
# sk = socket.socket()
# sk.connect(('192.168.5.175',80))
# # sk.connect(('192.168.5.175',80))
# while True:
#     name = input(">>>:")
#     sk.send(name.encode('utf-8'))
#     if name == 'exit':
#         break
#     response = sk.recv(1024)
#     print(response.decode('utf-8'))
# sk.close()
# import socket
# client = socket.socket()
# client.connect(('192.168.5.175',80))
# client.send(b'duwei')
# print(client.recv(1024))
# client.close()
import socket
socket = socket.socket()
socket.connect(('192.168.5.175',80))
while 1:
    user = input("user>>>:")
    pwd = input("密码>>>:")
    val = ("%s|%s"%(user,pwd)).encode("utf-8")
    print(val)
    socket.send(val)
