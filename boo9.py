boo={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i'}
def n2():
    print('1:',boo['1'],'2:',boo['2'],'3:',boo['3'])
    print('4:',boo['4'],'5:',boo['5'],'6:',boo['6'])
    print('7:',boo['7'],'8:',boo['8'],'9:',boo['9'])
    print('pick a number between 1 and 9')
n2()
sym=1
while True:
    
    n=input()
    if boo[n]=='x'or boo[n]=='o':
        print('you cant do that')
    else:
        if sym==1:
            boo[n]='x'
            sym=2
        if sym==2:
            boo[n]='o'    
    n2()
    n=input()
    if boo[n]=='o'or boo[n]=='x':
        print('you cant do that')
    else:
        boo[n]='o'
    n2()
