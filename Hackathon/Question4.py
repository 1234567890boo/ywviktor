import random
num={random.randint(10,100),random.randint(10,100),random.randint(10,100)}
print(num[random.randint(len(num),len(num))])

#didnt finish
#real abswer:
from random import randint
print([randint(1, 100) for i in range(3)][randint(0, 2)])