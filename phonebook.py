class phonebook1:
    def __init__(self,n):
        self.name2=n
        self.name={'bob':'111-111-1111','joe':'222-222-2222','billy':'333-333-3333'}
    def name1(self):
        print('What is your name?')
        na=input()
        print('What is your phone number?')
        pn=input()
        self.name[na]=pn   
        print(self.name)
