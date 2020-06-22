#server
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
clientsocket,address=s.accept()
print("Client found with ip:{}".format(address))


while True:
    print("send something to the client")
    data=input()
    clientsocket.send(data.encode("utf-8"))

    msg=clientsocket.recv(1024).decode("utf-8")
    print(msg)

    if data=="stop"or msg=="stop":
        print("Session ended")
        s.close()
        break

    
    
        
    
    
    
