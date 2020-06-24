import pygame

class Context:
    def __init__(self):
        pygame.init()
        self.font=pygame.font.SysFont(None, 20)
        self.bfont = pygame.font.SysFont(None, 14)

    def getPlayerFont(self):
        return self.font

    def getBarFont(self):
        return self.bfont