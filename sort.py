import random
list=[2,6,8,3]

# for s in range(0,20,1):
#      list.append(random.randint(0,100))

#selection sort:
# for t in range(0,len(list)-1,1):
#     e=0
#     for n in range(0,len(list)-1,1):
#         e+=1
#         if list[e]<list[n]:
#             list[n],list[e]=list[e],list[n]
#================================================================
#bubble sort:
# for q in range(0,len(list)-1,1):
#     first = 0
#     seccond = 1
#     for e in range(0,len(list)-1,1):
#         if list[first]>list[seccond]:
#             list[first],list[seccond]=list[seccond],list[first]
#         first+=1
#         seccond+=1
#=================================================================
#insertion sort:
for n in range(1,len(list),1):
    saved=list[n]
    previous=n-1
    while previous>=0 and saved<=list[previous]:
        if saved<list[previous]:
            list[previous+1]=list[previous]
        elif saved>list[previous]:
            list[previous+1]=saved
        previous-=1
    list[previous + 1] = saved
print(list)

#homework: file has items and price(every line has 2 things: item name, item price), read the file and make a dictionary