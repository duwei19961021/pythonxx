# -*- coding: utf-8 -*-
import socket
import subprocess
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
                conn.send(err) #send不能为空
                print("响应长度为",len(err))
            else:
                conn.send(out)
                print("响应长度为",len(out))
        except Exception as e:
            break
    conn.close()
