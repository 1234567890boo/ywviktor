import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("https://www.bing.com",80))
print("Connection established")

s.send("GET / HTTP/1.1\r\r\r\n".encode("utf-8"))

content=''
m=4096

while True:
    msg=s.recv(m).decode("utf-8",errors="ignore")

    print(len(msg))
        
    content=content+msg

    if '</html>' in msg or msg<='':
        break


content=content.split('\n')

    
s.close()
file=open('socketTest.html','w')
file.write(str(content))
file.close()




#Honework: convert list to string and do same thing with other website
