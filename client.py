#client
import threading, socket, time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
print("Connection established")

data=''

def send():
    global data
    print('')
    while True:
        data = input()
        if data == 'stop':
            s.send('stop'.encode("utf-8"))
            break
        else:
            s.send(data.encode("utf-8"))

def recive():
    while True:

        if data == 'stop':
            break

        msg = s.recv(1024).decode("utf-8")
        print('server:'+str(msg))
        if msg == 'stop':
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
#HW difference between sql database and not sql database hw Rohit emailed me, revize lesson 1.5-1.9 on yw website