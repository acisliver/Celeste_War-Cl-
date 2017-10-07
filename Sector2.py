import pygame
import math

class Sector1(pygame.Rect):
    speed = 0
    screen = None
    s_a = pygame.image.load("resources/images/sector_a1.png")
    sector_arrow = pygame.transform.rotate(s_a, 30)

    def __init__(self, screen, x, y, speed):
        super().__init__(self.arrow.get_rect())
        self.screen = screen
        self.top = x
        self.left = y
        self.speed = speed

    def move(self):
        self.top += self.speed/2
        self.left += self.speed/2 * math.sqrt(3)
        self.screen.blit(self.sector_arrow, (self.top + 25, self.left))






