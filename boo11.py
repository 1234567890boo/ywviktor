v="player1 win's"
b="player2 win's"
def WIN():
    if boo['1']==boo['2']==boo['3']=='x':
        print(v)
    if boo['4']==boo['5']==boo['6']=='x':
        print(v)
    if boo['7']==boo['8']==boo['9']=='x':
        print(v)
    if boo['3']==boo['6']==boo['9']=='x':
        print(v)
    if boo['2']==boo['5']==boo['8']=='x':
        print(v)
    if boo['1']==boo['4']==boo['7']=='x':
        print(v)
    if boo['3']==boo['5']==boo['7']=='x':
        print(v)
    if boo['1']==boo['4']==boo['9']=='x':
        print(v)
    if boo['1']==boo['2']==boo['3']=='o':
        print(b)
    if boo['4']==boo['5']==boo['6']=='o':
        print(b)
    if boo['7']==boo['8']==boo['9']=='o':
        print(b)
    if boo['3']==boo['6']==boo['9']=='o':
        print(b)
    if boo['2']==boo['5']==boo['8']=='o':
        print(b)
    if boo['1']==boo['4']==boo['7']=='o':
        print(b)
    if boo['3']==boo['5']==boo['7']=='o':
        print(b)
    if boo['1']==boo['4']==boo['9']=='o':
        print(b)
boo={'1':'_','2':'_','3':'_','4':'_','5':'_','6':'_','7':'_','8':'_','9':'_'}
def n2():
    print('1:',boo['1'],'2:',boo['2'],'3:',boo['3'])
    print('4:',boo['4'],'5:',boo['5'],'6:',boo['6'])
    print('7:',boo['7'],'8:',boo['8'],'9:',boo['9'])
    print('x = player1 and o = player2')
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
        elif sym==2:
            boo[n]='o'
            sym=1
    n2()
    WIN()

