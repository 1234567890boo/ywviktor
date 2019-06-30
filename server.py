##s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.bind((host,port))
##print('socket binded to', port)
##s.listen(2)
##conn,addr=s.accept()
##print('socket is listening')
##print(' got connection from', addr)
##while True:
##    name=input('')
##    conn.send(name.encode())
##    data=conn.recv(1024).decode('utf-8')
##    print('',repr(data))
##    s.close()
##connection=socket(AF_INET,SOCK_STREAM)
##server_ip_address=gethostbyname("google.com")
##server_port=80
##connection.connect((server_ip_address,server_port))
##connection.sendall(b"GET / HTTP/1.1\r\n\r\n")
##while True:
##     received_letter=connection.recv(1).decode("utf-8")
##     if received_letter=='':
##          break
##     print(received_letter,end='')
##connection.close()
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(10)
while True:
     browser,browser_address=s.accept()
     print("Browser connected at address: {}".format(browser_address))
     ch=None
     message=""
     while message[len(message)-2:]!='\r\n':
          ch=browser.recv(1).decode('utf-8')
          message=message+ch
          print("Message from browser: "+message)
          browser.sendall(b"""HTTP/1.1 200 OK\r\n
<!DOCTYPE html>
<html>
 <head>
  <title>
   Python Web Server
  </title>
  <h1>
   Python Web Server
  </h1>
 </head>
 <body>
  <p>A Python web server is serving this webpage.</p>
 </body>
</html>
     """)
browser.close()
