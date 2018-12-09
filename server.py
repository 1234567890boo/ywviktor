import socket
host=''
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket binded to', port)
s.listen(2)
conn,addr=s.accept()
print('socket is listening')
while True:
    print(' got connection from', addr)
    name=input('hello keep chat')
    print ('waiting for clients response')
    conn.send(name.encode())
    data=conn.recv(1024).decode('ascii')
    print('receved from client address', addr)
    print('mesage receved:',repr(data))
s.close()
