class bank:
    name=""
    balance=0
    def __init__(self,a,b):
        self.name=a
        self.balance=b
    def display(self):
        print('hello',self.name)
        print('your balance is ',self.balance,'dollars')
    def deposit_money(self):
        print('how much money do you want to deposit?')
        c=int(input())
        self.balance=self.balance+c
        print('Successfully deposited',c,'dolars')
        print('Your new balance is',self.balance,'dollars')
       
    def withdraw_money(self):
        print('how much money do you want to withdraw?')
        q=int(input())
        if self.balance <q:
            print('You cant withdraw that amount of money.')
        else:
            self.balance=self.balance-q
            print('Successfully withdrew',q,'dollars')
            print('Your new balance is',self.balance,'dollars')
