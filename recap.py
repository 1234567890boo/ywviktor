"""
print("what is your name?")
var=input()
print("what is your gender?")
var2=input()
if var2=="male":
    var2="mr."
    print("hi",var2,var)
elif var2=="female":
    var2="ms."
    print("hi",var2,var)
else:
    print("enter the correct gender")

for n in range(1,21,1):
    print(n)

x="viktor"
for n in x:
    print(n)

x="viktor"
for n in range(1,4,1):
    print("")
    for s in range(1,4,1):
        print(x)

x=5
while True:
    print(x)
    x=x-1
    if x==0:
        print("blast off!")
        break

x=5
while x>=1:
    print(x)
    x=x-1
print("blast off!")

x=20
y=0
while x>-1:
    print(x)
    x=x-1
    if x<=0:
        print(y)
        if y>0:
            y=y+1
        if y==36:
            break

x=20
y=-1
while x<=35:
    print(x)
    x=x+y
    if x==0:
        y=1

x=10
y=-1
while x<=20:
    print(x)
    x=x+y
    if x==-10:
        y=1
HOMEWORK:
loop form -10 to 10 and to 0
"""
x=-10
y=-1
while x>=-10:
    print(x)
    x=x-y
    if x<=-11:
        y=1
        x=x+y
    elif x>=11:
        y=1
        x=x-y
    elif x==-1 and y==1:
        break
