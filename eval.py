'''lst=[]
for s in range(1,31,1):
   lst.append(s)
for i in range(0,10,1):
    lst[i]=(i+1)**3
for s in range(24,30,1):
    lst[s]=(s+1)**2
print("the biggest number is",max(lst),"the smallest number is",min(lst))
lst.pop(15)
lst.pop(16)
print(lst)
for x in range(25,28,1):
   print(lst[x])
   x=x+1

#different code

for s in range(1,51,1):
   if s%5==0 and s%3==0:
      print("FizzBuzz")
   elif s%3==0:
      print("Fizz")
   elif s%5==0:
      print("Buzz")
   else:
      print(s)

#different code

for e in range(1,10,1):
   for s in range(1,10,1):
      print(s*e, end=' ')
   print('')

#different code

f=0
pw=''
print("what is yout password?")
pw=input()
l=len(pw)
while True:
   if 5<=l<=8:
      for i in range(10):
         if str(i) in pw:
            print("valid")
            f=1
            break
      if f==1:
         break
      print("invalid please try again")
      print("what is your password?")
      pw=input()
   else:
      print("invalid please try again")
      print("what is your password?")
      pw=input()
   l=len(pw)

#different code

s={}
for e in range(1,101,1):
   s[e]=e*e
   if e%10==0:
      s.pop(e)
print(s)

#Different code
'''
score={'math':17,'history':99,'science':79,'art':100,'ELA':72}
for s in score:
   print('subject=',s)
total=0
for x in score:
   total=total+score[x]
   print('score=',score[x])
average=total/5

