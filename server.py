#server
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
clientsocket,address=s.accept()
print("Client found with ip:{}".format(address))


while True:
    msg=clientsocket.recv(1024).decode("utf-8")
    msg=int(msg)
    if msg%msg+1==1:
        data='the number '+str(msg)+' is prime!'
    elif msg%msg+1!=1:
        data='the number '+str(msg)+' is not prime!'
    else:
        if data=='stop':
            clientsocket.send('session ended'.encode("utf-8"))
            s.close()
            break

    clientsocket.send(data.encode("utf-8"))

#hw=fix problems and then do multithreading and do data type,data type conversion,data type veriables