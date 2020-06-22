#client
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
print("Connection established")

while True:
    msg=s.recv(1024).decode("utf-8")
    print(msg)

    

    if msg=="stop":
        print("session ended")
        s.close()
        break
    
    if msg!="":
        print("Send something to the server")
        data=input()
        s.send(data.encode("utf-8"))
        if data=="stop":
            print("session ended")
            s.close()
            break
        
#homework: server asks client  2 numbers cliend gives them and server send the sum of both numbers both close after

