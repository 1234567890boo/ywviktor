import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


array=np.array(["A","B","C","D","E","F"])#makes 1d array into series
a=pd.Series(array)

array=[["A","B","C"],["D","E","F"]]#same as series but for 2d arrays
df=pd.DataFrame(array)

array=pd.Series()#shows dype as float64 with nothing in the array

array={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F"}#also works with dictionaries
dic=pd.Series(array)
#print(dic)#prints series

array=pd.Series(5,index=[0,1,2])

array=pd.Series([1,2,3],index=["A","B","C"])
#print(array.shape)#finds shape
#print(array.dtype)#finds dtype

dict={'id':[1,2,3,6,19,0],'name':['b','a','c','w','t','r']}
df=pd.DataFrame(dict)
#print(df)#makes list with names for columbs must be same lenth

dict={'id':pd.Series([1,2,3,6,19,0]),'name':pd.Series(['b','a','c','w'])}
df=pd.DataFrame(dict)
#print(df['id'])#makes list with names for columbs doesnt need to be same lengths
#print(df['id'])#shows part of list
df['age']=pd.Series(['299','199','10','1','5','500'])#ads another columb
#print(df.loc[3])#finds the row
new_df=pd.DataFrame([[9,'y','35']],columns=['id','name','age'])#makes new row
df=df.append(new_df)#adds new row
#print(df)

df1=pd.DataFrame({'x':[1,2,3,4,5],'y':[1,2,3,4,5]})
df2=pd.DataFrame({'x':[6,7,8,9,10],'y':[6,7,8,9,10]})
df1=df1.append(df2,ignore_index=True)#merges 2 dataframes together lists have to be the same lengths, ignore indexes makes rue the indexes are not reser when merging
#print(df1)

df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['x','y','z'])
#print(df.agg(["sum","min","max"]))#has built infucntions to use to make looking up values easear

data={'a':[1,2,3,4,5],'b':[6,7,8,9,10]}
df=pd.DataFrame(data)
#print(df.assign(c=lambda x:x.b+1, d=lambda x:x.c+1, e=lambda x:x.a+1))#makes it realy easy to add columbs using lambda
#print(df.assign(c=[11,12,13,14,15]))#adds a nother column

data1=pd.DataFrame([[1,2,3,4],[5,6,7,8]])
data2=pd.DataFrame([[11,12],[13,14],[15,16],[17,18]])
data3=data1.copy()
#take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
#print(data1.combine(data2,func=take_smaller))
#print(data1.compare(data2,align_axis=1))
#print(data3)
#print(data1.count())
#print(data1.dot(data2))
#print(data2.drop(2))

dict=pd.DataFrame({'a':[1,2,3,5,6,27,5],'b':[3,68,9,1,3,5,8]},index=[1,2,3,4,5,6,7])
group=dict.groupby('a')
#print(dict.keys())
print(dict.lt(10))
#print(group.groups)
#print(dict.head())
#print(dict.hist())
#plt.show()