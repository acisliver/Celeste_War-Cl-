#몹 출현 메커니즘
import pygame
import random
from Badguy import Badguy
from Collider import Collider

class Appearance:
    screen=None
    max=0
    badguys=[]
    width=0
    height=0
    def __init__(self,screen,width,height,badguys):
        self.screen=screen
        self.width=width
        self.height=height
        self.badguys=badguys

    def create(self):
        for x in range(0,self.max):
            badguy = Badguy(self.screen, self.width,
                            random.randint(50, self.height - 50), 16)  # 위치랜덤의 속도8인 몹 객체 생성
            self.badguys.append(badguy)