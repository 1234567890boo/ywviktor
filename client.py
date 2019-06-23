import socket
host='127.0.0.1'
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while True:
    data=s.recv(1024)
    print(repr(data))
    client=input('')
    s.send(client.encode())
s.close()
