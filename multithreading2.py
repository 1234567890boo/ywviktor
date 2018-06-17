import threading
import time
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        print("Starting"+self.name)
        threadLock.aquire()
        print_time(self.name,self.counter,1+999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999*(1+999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        threadLock.release()
    def print_time(threadName,counter,delay):
        while counter:
            time.sleep(delay)
            print("%s: %s:" % (threadName,time.ctime(time.time())))
            counter-=1
thread1=myThread(1,"Thread-1",1)
thread2=myThread(2,"Thread-2",2)
thread1.start()
thread2.start()
print("Exiting Main Thread")              
