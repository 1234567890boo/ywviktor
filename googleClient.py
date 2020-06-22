import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("https://stackoverflow.com/",80))
print("Connection established")

s.send("GET / HTTP/1.1\r\n\r\n".encode("utf-8"))

while True:
    msg=s.recv(4096).decode("utf-8",errors="ignore")
    print(msg,end="")
s.close()  

#Honework: gets and prints all html code
