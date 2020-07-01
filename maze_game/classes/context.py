import pygame

class Context:
    def __init__(self):
        pygame.init()
        self.font=pygame.font.SysFont(None, 20)
        self.bfont = pygame.font.SysFont(None, 14)
        self.bigFont = pygame.font.SysFont(None, 30)
        self.mapFont = pygame.font.SysFont(None, 15)

    def getPlayerFont(self):
        return self.font

    def getBarFont(self):
        return self.bfont

    def getBigFont(self):
        return self.bigFont

    def getMapFont(self):
        return self.mapFont

