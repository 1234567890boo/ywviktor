#server
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket,address=s.accept()
    print("Client found with ip:{}".format(address))
    clientsocket.send("Server connection established".encode("utf-8"))
    
    print("send smething to the client")
    data=input()
    clientsocket.send(data.encode("utf-8"))

    if data=="stop":
        print("Session ended")
        s.close()
        break
    
    msg=clientsocket.recv(1024).decode("utf-8")
    print(msg)
        
    
    
    
