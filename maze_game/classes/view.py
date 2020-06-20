class View:
    def setShouldBeHandled(self,state):
        self.state=state
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
