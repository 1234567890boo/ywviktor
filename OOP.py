'''class Bike:
    def __init__(self,color,num_brakes,num_wheels,sw,frames,size):
        self.color=color
        self.num_brakes=num_brakes
        self.num_wheels=num_wheels
        self.sw=sw
        self.frames=frames
        self.size=size
    def detailed_print(self):
        print(self.color)
        print(self.num_brakes)
        print(self.num_wheels)
        print(self.sw)
        print(self.frames)
        print(self.size)'''

class Bike:
    def __init__(self):
        self.color='red'
        self.num_brakes='2'
        self.num_wheels='2'
        self.sw='1'
        self.frames='1'
        self.size='big'
        self.lock_num='12345'
    def detailed_print(self):
        print(self.color)
        print(self.num_brakes)
        print(self.num_wheels)
        print(self.sw)
        print(self.frames)
        print(self.size)
        print(self.lock_num)
    def change_lock(self):
        
        print('what is the lock password?')
        lock=input()
        if lock!=self.lock_num:
            print('you are not authorised to change the lock number')
        else:
            print('what is the new lock number?')
            self.lock_num=input()
            print('lock number is now '+self.lock_num)
bike=Bike()
#bike2=Bike('blue','0 brakes','2 wheels','2 steering wheels','1 frame','small')
#bike.detailed_print()
