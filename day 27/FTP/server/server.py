# -*- coding: utf-8 -*-
import  socket
import struct
server = socket.socket()
server.bind(("127.0.0.1",80))
server.listen(5)
while True:
    conn,addr = server.accept()
    file_info = eval(conn.recv(1024).decode("gbk"))
    print(file_info,type(file_info))
    filename = file_info["filename"]
    print(filename)
    filesize = file_info["filesize"]
    print(filesize,type(filesize))
    rev_data = b''
    with open(filename, "wb") as f:
        rev_datalen = 0
        while rev_datalen < filesize:
            data = conn.recv(1024)
            rev_datalen += len(data)
            rev_data += data
            f.write(data)
        f.close()
