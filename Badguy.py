import pygame

class Badguy(pygame.Rect):
    speed=0
    num=0
    timer=4
    screen = None
    badguyimg = pygame.image.load("resources/images/Mob.png")

    def __init__(self, screen, x, y, speed,time,num):
        super().__init__(self.badguyimg.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top = x
        self.left = y
        self.speed = speed
        self.screen = screen
        self.time=time
        self.num=num


    def move(self):             #몹 움직임 함수
        self.left += self.speed
        self.screen.blit(self.badguyimg,(self.top,self.left))