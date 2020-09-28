'''x=1
while x==(1,2,3,4,5,6,7,8,9,10):
    for n in range(1,11):
        for s in range(1,11):
            print(s, end='')
        print()
        x=x+1


def mySort(v):
    return v[2]


list1=[[2, 'Danny', 45], [3, 'Bob', 15], [1, 'Vikor',90]]
list2=sorted(list1, key=mySort)
list1=list2
print(list2)


name='bob'
v='t'
l=['joe','bob','billy']

if name in l:
    print("true")
else:
    print('false')


v={'a':1,'e':2,'i':3,'o':4,'u':5}
q='banana'
numOfVowels=0

if 'i' in v:
    v.pop('i')
    print(v)
else:
    print('no')'


list=[1,3,36,56,53,7,65,6,3,5,9,4,78,49,100]
for n in list:
    squareroot=n**0.5
    if int(squareroot)==squareroot:
        print(n)


print('imput a number')
n=int(input())
divide=n/10
if int(divide)==divide:
    print('it is multiple of 10')
else:
    print('it is not mutiple of 10')


print('enter a word')
word=input()
divide=len(word)/2
if int(divide)==divide:
    print('there is a even number of leters')
else:
    print('there is an odd number of letters')


print('input a number')
num=int(input())
if num>=10 and num<=19:
    print('you win $2')
elif num>=20 and num<=29:
    print('you win $4')
elif num>=30 and num<=39:
    print('you win $6')
else:
    print('you win nothing')'''


#hw: What if purpous of join method, make chat with threads for recieving and sending and work on lesson 1.5-1.9