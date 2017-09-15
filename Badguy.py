import pygame

class Badguy(pygame.Rect):
    speed=0
    screen = None
    badguyimg = pygame.image.load("resources/images/badguy.png")

    def __init__(self, screen, x, y, speed):
        super().__init__(self.badguyimg.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top = x
        self.left = y
        self.speed = speed
        self.screen = screen

    def move(self):             #몹 움직임 함수
        self.top -= self.speed
        self.screen.blit(self.badguyimg,(self.top,self.left))