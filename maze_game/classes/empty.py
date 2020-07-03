from classes.gridobj import *

class Empty(GridObj):
    def kind(self):
        return "Empty"
    def draw(self,screen,x,y,width,height):
        pass
    def canMoveInto(self, obj):
        return True
