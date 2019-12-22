import random
'''num=[]
count=0
for s in range(0,50,1):
    d=random.randint(0,50)
    num.append(d)
num.sort()
for n in num:
    if n%2==0:
        print(n)
        count=count+1
print("even =",count)
count2=50-count
print("odd =",count2)

wierd=[2,4.6,"hi",False]
for n in range(0,len(wierd),1):
    print(wierd[n])

lst=[]
n=random.randint(0,5)
h=random.randint(0,5)
lst.append(h)
lst.insert(1,n)
print(lst)

lst2=[1,2,3,4,5]
lst2.remove(2)
print(lst2)

lst3=['A','B','60','D','d','t','2','e']
print(lst3)
#lst3.reverse()
print(lst3[::-2])

str='I like to eat pie and pie is great, YUM!!'
print(str[::-1])'''

str2=''
print('give me a word or sentance')
str2=input()
if str2[::-1]==str2:
    print('its a palendrome')
else:
    print('its not a palendrome')