# -*- coding: utf-8 -*-
import socket
import struct
client = socket.socket()
client.connect(("127.0.0.1",80))
while True:
    Exec = input("exec>>>:")
    client.send(Exec.encode('utf-8'))
    if Exec=="":
        continue
    res = client.recv(1024)
    datalen = struct.unpack("i",res)[0]
    print(datalen)
    recv_datalen=0
    recv_data=b""
    while recv_datalen < datalen:
        data = client.recv(1024)
        recv_datalen += len(data)
        recv_data += data
        print(recv_data.decode("gbk"),len(recv_data))
client.close()