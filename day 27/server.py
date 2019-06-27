# -*- coding: utf-8 -*-
# import socket
# server = socket.socket()
# server.bind(('192.168.5.175',80))
# server.listen(5)
# while True:
#     conn,addr = server.accept()
#     while True:
#         data = conn.recv(1024)
#         if data == b'exit':
#             break
#         response = data + b'sb'
#         conn.send(response)
#         print(conn.recv(1024))
#     conn.close()
while 1:
    import socket
    server = socket.socket()
    server.bind(('192.168.5.175',80))
    server.listen(5)
    conn,addr = server.accept()
    data = conn.recv(1024)
    response = data + b'666'
    conn.send(response)
    print(data)
    conn.send(data + b"666")
    conn.close()
    server.close()