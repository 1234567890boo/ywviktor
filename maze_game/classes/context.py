import pygame

class Context:
    def __init__(self):
        pygame.init()
        self.font=pygame.font.SysFont(None, 20)

    def getFont(self):
        return self.font