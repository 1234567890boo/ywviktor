import random,time

def num(n):
    n.append(random.randint(0,50))
    if len(n)>=10:
        return n
    num(n)

def ownsort():
    n.sort()
    return n

num([])
ownsort()



'''
def p(x=5,y=5):
    for s in range(0,x,1):
        print('')
        for n in range(0,y,1):
            print('*',end='')
p()
'''

#HW Do functions level 1 python
