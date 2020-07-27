import pygame
from classes.view import *

class GridObj(View):
    def __init__(self):
        self.pocket=None

    def kind(self):
        return "View"

    def setShouldBeHandled(self, state):
        self.state = state
        return self

    def getShouldBeHandled(self):
        return self.state

    def isInventory(self):
        return False

    def canMoveInto(self, obj):
        return False

    def setGridPocket(self,pocket):
        self.pocket=pocket

    def getGridPocket(self):
        return self.pocket
