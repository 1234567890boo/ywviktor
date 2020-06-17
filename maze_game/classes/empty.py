from classes.view import *
class Empty(View):
    def kind(self):
        return "Empty"
    def draw(self,screen,x,y,width,height):
        pass
    def handleKey(self,key,pview,x,y):
        pass
    def canReplace(self,obj):
        return True
