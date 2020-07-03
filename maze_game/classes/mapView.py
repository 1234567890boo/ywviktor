from classes.empty import *
from classes.view import *
from classes.utils import *
from classes.gridobj import *

class MapView(View):
    def kind(self):
        return "Map_View"

    def __init__(self,gridwidth,gridheight):
        self.grid=[]
        self.gridwidth=gridwidth
        self.gridheight=gridheight
        for x in range(0,gridwidth,1):
            column=[]
            for y in range(0,gridheight,1):
                column.append(Empty())
            self.grid.append(column)
    def handleKey(self,key,pview,x,y):
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                gobj=self.getobj(xgrid,ygrid)
                gobj.handleKey(key,self,xgrid,ygrid)
    def handleCycle(self,pview,x,y):
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                gobj=self.getobj(xgrid,ygrid)
                gobj.setShouldBeHandled(True)
                
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                gobj=self.getobj(xgrid,ygrid)
                if gobj.getShouldBeHandled():
                    res=gobj.handleCycle(self,xgrid,ygrid)
                    gobj.setShouldBeHandled(False)
                    
    def hasPath(self,p1,p2):
        path=get_line(p1,p2)
        path.pop(0)
        path.pop(len(path)-1)
        for p in path:  
            kind=self.getobj(p[0],p[1]).kind()
            if kind!="Empty" and kind!="Enemy":
                return False
        return True
    def giveShift(self,source,dest):
        path=get_line(source,dest)
        nextPoint=path[1]
        shift=(nextPoint[0]-source[0],nextPoint[1]-source[1])
        return shift
    def putobj(self,x,y,obj):
        self.grid[x][y]=obj
    def getobj(self,x,y):
        return self.grid[x][y]

    def moveobj(self,sx,sy,dx,dy):
        if dx<0 or dx>self.gridwidth-1 or dy<0 or dy>self.gridheight-1:
            return

        sobj=self.getobj(sx,sy)
        dobj=self.getobj(dx,dy)
        
        if dobj.canMoveInto(sobj):
            self.putobj(dx,dy,sobj)
            pockettoRestore=sobj.getGridPocket()
            if pockettoRestore is None:
                pockettoRestore =Empty()

            self.putobj(sx,sy,pockettoRestore)
            sobj.setGridPocket(dobj)

    def draw(self,screen, x,y,width,height):
        cellwidth=int(width/self.gridwidth)
        cellheight=int(height/self.gridheight)
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                self.getobj(xgrid,ygrid).draw(screen,x+xgrid*cellwidth,y+ygrid*cellheight,cellwidth,cellheight)

    def get_items(self,kind):
        items=[]
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                gobj=self.getobj(xgrid,ygrid)
                if gobj.kind()==kind:
                    items.append((gobj,xgrid,ygrid))
        return items

