import random
list=[]

for s in range(0,20,1):
    list.append(random.randint(0,100))

for n in range(0,len(list)-1,1):
    sublist=list[n:]
    locationOfMin=sublist.index(min(sublist))

    list[locationOfMin+n],list[n]=list[n],list[locationOfMin+n]


print(list)

#homework: finish selcted sort