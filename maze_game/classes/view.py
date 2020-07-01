class View:
    def setShouldBeHandled(self,state):
        self.state=state
        return self
    def getShouldBeHandled(self):
        return self.state
    def kind(self):
        return "View"
    def canReplace(self,obj):
        return False
    def draw(self,screen,x,y,width,height):
        pass
    def handleCycle(self,pview,x,y):
        pass
    def handleKey(self,event,pview,x,y):
        pass
    def isInventory(self):
        return False
