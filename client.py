import socket
host='192.168.1.95'
port=6920
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    print('Receved data from server',repr(data))
    message=input('Say something to server:')
    s.send()
    s.close()
