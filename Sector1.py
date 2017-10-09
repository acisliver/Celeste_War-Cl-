import pygame


class Sector1(pygame.Rect):
    speed = 0
    screen = None
    sector_arrow = pygame.image.load("resources/images/sector_a1.png")

    def __init__(self, screen, x, y, speed):
        super().__init__(self.sector_arrow.get_rect())
        self.screen = screen
        self.top = x
        self.left = y
        self.speed = speed

    def move(self):
        self.left -= self.speed
        self.screen.blit(self.sector_arrow,(self.top + 25, self.left))




