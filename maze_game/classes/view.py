class View:
    def kind(self):
        return "View"
    def canReplace(self,obj):
        return False
    def handleCycle(self,pview,x,y):
        pass
