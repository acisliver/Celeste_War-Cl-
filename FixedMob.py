import pygame
import math
from FixedBullet import FixedBullet
from Player import Player


class FixedMob(pygame.Rect):
    speed=0

    screen = None
    fixedmob = pygame.image.load("resources/images/fixedMob.png")
    fixedmob2 = pygame.image.load("resources/images/fixedMob2.png")
    fixedmob3 = pygame.image.load("resources/images/fixedMob3.png")
    fixedlist=[fixedmob,fixedmob2,fixedmob3]


    def __init__(self, screen, x,  time):
        super().__init__(self.fixedmob.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top = x-50
        self.left = 180
        self.screen = screen
        self.time=time
        self.heal=2
        self.num=0
        self.num2=0

    def move(self,player):             #원거리몹 움직임 함수
        if self.time==0:
            self.num2=0
            self.shot(player)
            self.time=200
        else:
            self.time-=1
        if self.time==50:
            self.num2=1
        elif self.time==20:
            self.num2=2
        self.screen.blit(self.fixedlist[self.num2], (self.top,self.left))

    def shot(self,player):                 #화살생성함수
        fixedblullet = FixedBullet(self.screen, self.top + 32.5, self.left + 32.5, 8,
                                   math.atan2((self.left + 32.5) - (player.left + 132.5),
                                              (self.top + 32.5) - (player.top + 57.5)))
        player.fixedbullet.append(fixedblullet)