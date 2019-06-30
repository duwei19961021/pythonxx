# -*- coding: utf-8 -*-
import socket
client = socket.socket()
client.connect(("127.0.0.1",80))
while True:
    Exec = input("exec>>>:")
    client.send(Exec.encode('utf-8'))
    if Exec=="":
        continue
    response = client.recv(1024)
    print(response.decode('gbk'))
    print("接受长度为",len(response))
client.close()