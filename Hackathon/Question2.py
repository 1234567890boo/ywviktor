import random

average=''
for n in range(0,6,1):
    var=random.randint(10,100)
    print(var)
    average=average+str(var)
average=int(average)/6
print(average)

#didnt finish