numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruits = ["Apple", "Banana", "Pear", "Apple", "Pineapple", "Apple", "Pear", "Guava", "Grapes", "Watermelon"]
dict={}
for n in range(0,10,1): dict[numbers[n]]=fruits[n]
print(dict)

#put lists/dict in same line:
numbers, fruits, NewDict = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["Apple", "Banana", "Pear", "Apple", "Pineapple", "Apple", "Pear", "Guava", "Grapes", "Watermelon"], {}