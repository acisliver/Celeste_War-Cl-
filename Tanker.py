#탱커
import pygame
import random

class Tanker(pygame.Rect):
    speed = 0   #탱커가 좌우로 움직일 경우 속도
    screen = None
    tanker = pygame.image.load("resources/images/badguy.png")

    def __init__(self, screen, x, y, speed):
        self.screen = screen
        self.top = x
        self.left = y
        self.speed = speed

    def move(self):
        while True:
            if random.randint(0, 1) == 0:
                self.top -= self.speed
            else:
                self.top += self.speed


