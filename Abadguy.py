import pygame
import random
from Bullet import Bullet
from Timer import Timer

class Abadguy(pygame.Rect):
    speed=0
    screen = None

    abadguy = pygame.image.load("resources/images/abadguy.png")
    wallCollX="Left"
    wallCollY="Down"


    def __init__(self, screen, x, y, speed, time,num,round):
        super().__init__(self.abadguy.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top = x-50
        self.left = y
        self.speed = speed
        self.screen = screen
        self.time=time
        self.num = num
        self.round=round
        self.bullets = []

    def startmove(self, sinx):
        rotated = pygame.transform.rotate(self.abadguy, sinx)
        rect = rotated.get_rect()
        rect.center = (self.top + 50, self.left)
        self.screen.blit(rotated, rect)

    def move(self):             #원거리몹 움직임 함수
        if self.time==0 and self.num==-1:
            self.shot()
            self.time=random.randint(0,100)
        else:
            self.time-=1
        for bullet in self.bullets:
            bullet.move()
        rotated = pygame.transform.rotate(self.abadguy, 180)
        rect = rotated.get_rect()
        rect.center = (self.top+50, self.left)

        if self.top>=650:
            self.wallCollX="Right"
        if self.top<=50:
            self.wallCollX="Left"
        if self.left>=200:
            self.wallCollY="Up"
        if self.left<=50:
            self.wallCollY="Down"
        if self.wallCollX=="Left":
            self.top+=self.speed
        if self.wallCollX=="Right":
            self.top-=self.speed
        if self.wallCollY=="Down":
            self.left+=self.speed
        if self.wallCollY=="Up":
            self.left-=self.speed

        self.screen.blit(rotated, rect)



    def shot(self):                 #화살생성함수
        bullet = Bullet(self.screen, self.top, self.left, 20 )    #speed가 30인 화살 생성
        self.bullets.append(bullet)                               #list에 arrow객체 추가