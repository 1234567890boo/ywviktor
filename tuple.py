total=0
dict={'p':50,'q':78,'r':91}
dict['z']=69
for n in dict:
    dict[n]+=5
    total=total+dict[n]
dict['p']+=30
print(dict)
print(total/len(dict))