class shoping:
    def __init__(self,budget):
        self.budget=budget
        self.shoping_bag={}

    def shoping(self):
        print('what do you want to buy?')
        z=input()
        print('what is the price')
        c=int(input())
        if self.budget <c:
            print('you dont have enough money.')
        else:
            self.shoping_bag[z]=c
            self.budget=self.budget-c
            print('you bought',self.shoping_bag)
            print('you have',self.budget)

    def return_item(self):
        print("what do you want to return?")
        v=input()
        self.budget=self.budget+self.shoping_bag[v]
        del self.shoping_bag[v]
        print(self.shoping_bag,self.budget)
    
