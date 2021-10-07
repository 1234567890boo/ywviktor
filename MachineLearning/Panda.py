import pandas as pd
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

df=pd.DataFrame()
df['id']=[1,2,3,4,5]
df1['age']=[]
df.assign(df1)
print(df)