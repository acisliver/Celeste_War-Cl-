import pygame


class Sector1(pygame.Rect):
    speed = 0
    screen = None
    sector_arrow = pygame.image.load("resources/images/sector_a1.png")

    def __init__(self, screen, x, y, speed,timer):
        super().__init__(self.sector_arrow.get_rect())
        self.screen = screen
        self.top = x
        self.left = y
        self.speed = speed
        self.timer=timer
        self.name="Sector"

    def move(self):
        self.timer+=1
        self.left -= self.speed
        self.screen.blit(self.sector_arrow,(self.top + 25, self.left))




