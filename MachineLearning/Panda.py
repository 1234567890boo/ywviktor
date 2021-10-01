import pandas as pd
import numpy as np

array=np.array(["A","B","C","D","E","F"])#makes 1d array into series
a=pd.Series(array)

array=[["A","B","C"],["D","E","F"]]#same as series but for 2d arrays
df=pd.DataFrame(array)

array=pd.Series()#shows dype as float64 with nothing in the array

array={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F"}#also works with dictionaries
dic=pd.Series(array)

array=pd.Series(5,index=[0,1,2])

array=pd.Series([1,2,3],index=["A","B","C"])
#print(array.shape)finds shape
#print(array.dtype)#finds dtype