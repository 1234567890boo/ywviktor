#server
import threading, socket, time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
clientsocket,address=s.accept()
print("Client found with ip:{}".format(address))

data=''

def send():
    global data
    print('')
    while True:
        data = input()
        if data == 'stop':
            clientsocket.send('stop'.encode("utf-8"))
            break
        else:
            clientsocket.send(data.encode("utf-8"))

def recive():
    while True:

        if data=='stop':
            break

        msg=clientsocket.recv(1024).decode("utf-8")
        print('Client:'+str(msg))

        if msg=='stop':
            break



se=threading.Thread(target=send)
r=threading.Thread(target=recive)

se.start()
r.start()

se.join()
r.join()

while True:
    if data=='stop' or msg=='stop':
        s.close()
        print('stopping')
        break
#hw=fix problems and then do multithreading and do data type,data type conversion,data type veriables