import socket
host='127.0.0.1'
port=6920
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while True:
    data=s.recv(1024)
    print('receved from server', repr(data))
    client=input('say something to server:')
    s.sent(client.encode())
s.close()
