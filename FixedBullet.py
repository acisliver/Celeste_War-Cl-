#몹의 총알
import pygame
import math

class FixedBullet(pygame.Rect):
    speed=0
    screen = None
    bullet = pygame.image.load("resources/images/laser ball3.png")
    bullet2 = pygame.image.load("resources/images/laser ball4.png")
    bulletlist=[bullet,bullet2]


    def __init__(self,screen,x,y,speed,rotate):
        super().__init__(self.bullet.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.width=30
        self.hight=30
        self.top=x
        self.left=y
        self.speed=speed
        self.screen=screen
        self.rotate=rotate
        self.num=0
        self.time=1

    def move(self):         #총알의 움직임 함수
        self.top-=math.cos(self.rotate)*self.speed
        self.left-=math.sin(self.rotate)*self.speed
        if self.time==0:
            if self.num == 0:
                self.num = 1
            else:
                self.num = 0
            self.time=1
        else:
            self.time-=1
        self.screen.blit(self.bulletlist[self.num], (self.top,self.left))