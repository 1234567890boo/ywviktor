'''x=1
while x==(1,2,3,4,5,6,7,8,9,10):
    for n in range(1,11):
        for s in range(1,11):
            print(s, end='')
        print()
        x=x+1'''

def mySort(v):
    return v[2]

list1=[[2, 'Danny', 45], [3, 'Bob', 15], [1, 'Vikor',90]]
list2=sorted(list1, key=mySort)
list1=list2
print(list2)