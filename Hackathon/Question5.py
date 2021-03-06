num=float(input())
num=num.reverse()
print(num)
#didnt finish
#real answer:
num = input('Enter a float number: ')
decimals = list(num.split('.')[1])
decimals.reverse()
print(''.join(decimals))