import threading
import time
def print_cube(num):
    while 1:
        time.sleep(0.25)
        print("Cube:{}".format(num*num*num))
        print()
def print_square(num):
    while 1:
        time.sleep(0.25)
        print("Square:{}".format(num*num))
        print()
if __name__=="__main__":
    t1=threading.Thread(target=print_square,args=(10,))
    t2=threading.Thread(target=print_cube,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")

