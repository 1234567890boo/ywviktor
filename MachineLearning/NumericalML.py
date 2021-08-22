import numpy as np

array=np.zeros((5,2)) #makes 2d list 1st number is for width the second number is for height
array=np.arange(0,5,1) #sorts numbers least to greatest
array=np.zeros((11,10)) #11 rows of 0 and 10 rows of 0
array=np.zeros((2,2,2)) #makes a 3d list
array=np.array([42.46512,42.46512,42.46512]) #premade array
#.shape functions tells you the shape of the array
#.ndim tells you how many dimentions is in an array
array=np.arange(0,200,5)
array=array.reshape(2,2,-1) #reshape changes the dimentions of your array and arrays neeed to have the same amount of number in them
# remember to use colon for slicing
array1=np.array([1,1,1,5])
array2=np.array([3,5,7,0])
array=np.vstack((array1,array2)) #stacks 2 or more lists verticaly and arrays neeed to have the same amount of number in them
array=np.hstack((array1,array2)) #stacks 2 or more lists horizontaly and arrays neeed to have the same amount of number in them

variable="this is a varable"
array=np.asarray(variable) #turns variable into array



array=np.array([[1,2,3],[4,5,6]])
num=array[1,0:2]

array=np.array([2.3,1.1],dtype='i4')
#I for integer
#F for float
#S for string
#U for unicode


#use copy to make changes to a copy of the array and view to change the original array
array=np.array([1,2,3])
array1=array.view()
array[1]=3

array=np.array([1,2,3])
num=np.max(array)
#min finds smallest value
#max finds Largest value
#mean finds average
#median finds visual middle value

array=np.array([[1,2,3],[4,5,6]])
array1=np.array([[7,8,9],[10,11,12]])
array2=np.concatenate((array,array1),axis=1) #concatenate to merge 2 arrays, axis stacks across rows
array2=np.vstack((array,array1)) #vstack stack across colums
array2=np.dstack((array,array1)) #dstack stacks across the depth


array=np.array([1,2,3,4,5,6])
array=np.array_split(array,7) #array_split splits a array into a number of parts
array=np.array([[1,2,3],[4,5,6]])
array=np.array_split(array,3,axis=1) #array_split can also use axis


array=np.array([1,2,3,4,5,6])
#array=np.where(array==5) #the where functions locates a item in the list and gives us the postions of it
array=np.where(array%2==0) #the where function also does math in the perenthesis


array=np.array([6,7,8,9])
array=np.searchsorted(array,7,side='right') #searches sorted arrays for a numbers and returnds the position of it


array=np.array([1,4,2,6,8,1])
array=np.sort(array) #sorts the array


print(array)




#Homework: do bargraph slide 5