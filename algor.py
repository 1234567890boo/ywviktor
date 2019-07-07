import random
num=[]
for s in range(0,50,1):
    d=random.randint(0,50)
    num.append(d)
num.sort()
for n in num:
    if n%2==0:
        print(n)