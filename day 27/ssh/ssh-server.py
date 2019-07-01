# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
server = socket.socket()
server.bind(("127.0.0.1",80))
server.listen(5)
while True:
    conn,addr = server.accept()
    while True:
        try:
            Exec = conn.recv(1024).decode("gbk")
            print(Exec)
            if len(Exec)==0:
                break
            if Exec == b'exit':
                break
            res = subprocess.Popen(Exec,
                             shell=True,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE)
            out = res.stdout.read()
            err = res.stderr.read()
            if err:
                reserr = struct.pack("i",len(err))
                conn.send(reserr)
                conn.send(err) #send不能为空
            else:
                res = struct.pack("i",len(out))
                conn.send(res) #发送数据长度
                conn.send(out) #发送数据
                print("响应长度为",len(out))
        except Exception as e:
            break
    conn.close()
# 通过struct模块对数据长度进行压缩，send给客户端，客户端收到压缩后的数据长度后反解得到数据长度，在根据收到的数据长度和本地每次接受
# 的数据长度对比，大于本地每次能接受的最大数据长度时则利用while循环多次接受。
