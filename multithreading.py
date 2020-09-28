import threading,time

'''def digit_counter():
    print('input a number')
    num=input()
    print('there are '+str(len(num))+' digits in '+str(num))

def non_vowel_counter():
    vowels=['a','A','e','E','i','I','o','O','u','U']
    print('input a word.')
    word=input()
    num_of_vowels = 0
    for n in range(0,len(word),1):
        if word[n] in vowels:
            num_of_vowels+=1
    num_of_not_vowels = len(word) - num_of_vowels
    print(num_of_vowels,num_of_not_vowels)

print('what do you want to do?(digit counter=1, non vowel counter=2')
n=input()
if n=='1':
    t.start()
elif n=='2':
    t2.start()'''


def counter_function():
    n=0
    while True:
        if n==10:
            break
        print(n,'n')
        n+=1
        time.sleep(1)

def counter_counter_function():
    s=0
    while True:
        if s==4:
            break
        print(s,'s')
        s+=1
        time.sleep(3)

n=threading.Thread(target=counter_function)
s=threading.Thread(target=counter_counter_function)
n.start()
s.start()
l=97

n.join()
s.join()

while True:
    if l==103:
        break
    print(chr(l))
    l+=1
    time.sleep(2)


exit()
#hw: What if purpous of join method, make chat with threads for recieving and sending