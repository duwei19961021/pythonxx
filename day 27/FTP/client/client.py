import  socket
import os
client = socket.socket()
client.connect(("127.0.0.1",80))
while True:
    action = "put pod.png"
    action,filename = action.split(" ")
    if action == "put":
        filesize = os.path.getsize(filename)
        file_info = str({"action": action, "filename": filename, "filesize": filesize})
        client.send(file_info.encode("utf-8"))
        with open(filename, "rb") as f:
            for line in f:
                client.send(line)
            f.close()
        single = client.recv(1024)
        if single == b'exit':
            break
    elif action == "get":
        file_info = str({"action": action, "filename": filename})
        client.send(file_info.encode("utf-8"))
        filesize = eval(client.recv(1024).decode("utf-8"))
        print(filesize,type(filesize))
        if filesize:
            client.send(b"ok")
            reve_data = b''
            reve_datesize = 0
            while reve_datesize < filesize:
                data = client.recv(1024)
                reve_data += data
                reve_datesize += len(data)
                with open(filename, "wb") as f:
                    f.write(reve_data)
                if reve_datesize == filesize:
                    client.send(b"exit")
                f.close()
