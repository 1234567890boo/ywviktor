Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import random
import time
#import this
'''num=random.randint(0,100)
while True:
    print("I am thinking of a number 0-100, can you guess it?")
    n=int(input())
    if n==num:
        print("correct!")
        print("do you want to play again?") 
        e=input()
        if e=="no":
            break
        else:
            print('replaying')
            num=random.randint(0,100)
            time.sleep(5)
    elif num<n:
        print("to High, try again.")
    elif num>n:
        print('too low, try again.')

#differnt game

q=random.randint(0,3)
w=random.randint(0,3)
e=random.randint(0,3)
print('do you want to play?(y/n)')
t=input()
if t=='y':
    while True:
        print(q,w,e)
        if q==w==e:
            print('you win')
            print('do you want to play again((y/n)')
            r=input()
            if r=='n':
                break
            else:
                q=random.randint(0,3)
                w=random.randint(0,3)
                e=random.randint(0,3)
        else:
            print('you loose')
            print('do you want to play again((y/n)')
            r=input()
            if r=='no':
                break
            else:
                q=random.randint(0,3)
                w=random.randint(0,3)
                e=random.randint(0,3)'''
