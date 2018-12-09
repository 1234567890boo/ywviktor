import socket
host='192.168.1.79'
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while True:
    data=s.recv(1024)
    print('receved from server', repr(data))
    client=input('say something to server:')
    s.sent(client.encode())
s.close()
