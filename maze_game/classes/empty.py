from classes.view import *
class Empty(View):
    def kind(self):
        return "Empty"
    def draw(self,screen,x,y,width,height):
        pass
    def canReplace(self,obj):
        return True
