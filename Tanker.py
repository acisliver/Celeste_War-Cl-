#탱커
import pygame
import random

class Tanker(pygame.Rect):
    speed = 0   #탱커가 좌우로 움직일 경우 속도
    screen = None
    tanker = pygame.image.load("resources/images/badguy2.png")
    heall=0

    def __init__(self, screen, x, y,speed,heall):
        super().__init__(self.tanker.get_rect())
        self.screen = screen
        self.top = x
        self.left = y
        self.speed = speed
        self.heall=heall

    def move(self):
        if random.randint(0, 1) == 0:
            self.left -= self.speed
        else:
            self.left += self.speed
        self.screen.blit(self.tanker, (self.top, self.left))
