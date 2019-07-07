import random
import statistics

'''
num1=[]
num2=[]
print('give me a number')
num1=int(input())
print('give me a number')
num2=int(input())
if num2 < num1:
    print("the smallest number is "+str(num2))
if num1 < num2:
    print("the smallest number is "+str(num1))
if num1 == num2:
    print("they are the same")

#different code

num1=[]
num2=[]
num3=[]
print('give me a number')
num1=int(input())
print('give me a number')
num2=int(input())
print("give me a number")
num3=int(input())
if num1 < num2 and num3 < num2:
    print("the largest number is" + str(num2))
if num1 < num3 and num2 <num3:
    print("the largest number is" + str(num3))
if num2 < num1 and num3 < num1:
    print("the largest number is" + str(num1))
if num1==num2 and num2==num3:
    print("they are the same")
if num2 < num1 and num1==num3:
    print("the largest number is"+str(num1))
if num3 < num1 and num1==num2:
    print("the largest numberis"+str(num1))
if num1 < num2 and num2==num3:
    print("the largest number is"+str(num2))
if num3 < num1 and num2==num3:
    print("the largest number is"+str(num2))


#different code

s=[]
for n in range(0,10,1):
    z=random.randint(1,100)
    s.append(z)
big=1
small=100
for x in s:
    if big<x:
        big=x
print('the largest number is '+str(big))
for y in s:
    if small>y:
        small=y
print('the smallest number is '+str(small))
s.remove(big)
s.append(big)
s.remove(small)
s.insert(0,small)
a=0
for x in s:
    a=a+x,
a=a/10
print(a)
print(s)
for q in range(7,10,1):
    print(s[q],end= ' ')
s.pop(4)
s.pop(8)
print(s)

#different code
s=['I','Like','Pie','!!!']
for x in range(0,len(s),1):
    print(s[x])

#different code
s={'a ':'human','is not':'a monster','a':'monster','is  not':'a human','i like':'trains'}
print(s['a'])
print(s)
s['a']='troll'
print(s['a'])
'
#different code

s={'pop':4 ,'POP':5,'Pop':2,'POp':1,'PoP':3}
sval=s.values()
sval=list(sval)
sval.sort()
print(sval)
for n in range(0,5,1):
    big=0
    valbig=''
    for x in s:
        if big<s[x]:
            big=s[x]
            valbig=x
    print('the bigest number is',big,valbig)
    s.pop(valbig)

#diferent code
f=1
print('what is the factorial?')
F=int(input())
for s in range(F,0,-1):
    f=f*s
print(f)

#different code

print('what is the factorial?')
F=int(input())
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
value=factorial(F)
print(value)

#different code

gcd=1024
gcd2=1996
def gcd(gcd1,gcd2):
    if gcd2%gcd1==0:
        return gcd
    else gcd1%gcd2!=0:
        gcd1=gcd2
        gcd1/gcd2=gcd1
gcd()

#Different Code

num=''
print('what number?')
num=int(input())
flag=False
for  x in range (2,num,1):
    if num%x==0:
        print('Not Prime')
        flag=True
        break
if flag==False:
    print('Prime')

#different code
#sieve of erasthosthenes
print('what is the staring number?')
start=int(input())
print('what is the ending number?')
end=int(input())
for s in range(start,end,1):
    flag=False
    for  x in range (2,s,1):
        if s%x==0:
            print('Not Prime')
            flag=True
            break
    if flag==False:
        print('Prime')

#different code
#ordinal code(ASCII)
print(ord('1'))
print(chr())
'''
#continuation
#cesars cypher
passw=('')
print('what is the pasword')
passw=input()
passl=passw.__len__()
cipher=random.randint(1,10000)
for a in range(0,passl,1):
    ordvar=(ord(passw)+cipher)
print(chr(ordvar))
