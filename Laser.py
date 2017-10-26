#관통 레이저
import pygame

class Laser():
    screen = None
    bim =  pygame.image.load("resources/images/arrow1.png")
    charge = pygame.image.load("resources/images/arrow1.png")

    def __init__(self, screen, x ,y):
        super().__init__(self.charge.get_rect())
        super().__init__(self.bim.get_rect())
        self.top = x
        self.left = y
        self.screen = screen

    def move(self):
        self.screen.blit(self.bim,(self.top+25,self.left))
        self.screen.blit(self.charge, (self.top + 25, self.left))

