#client
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
print("Connection established")

while True:
    print("what number do you want to send to the server?(put the number only)")
    data = input()
    if data=='stop':
        s.send('stop'.encode("utf-8"))
        s.close()
        break
    s.send(data.encode('utf-8'))

    msg=s.recv(1024).decode("utf-8")
    print(msg)

#hw=fix problems and then do multithreading and do data type,data type conversion,data type veriables