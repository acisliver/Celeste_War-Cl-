#모든 충돌
import pygame
from Healbar import Healbar

class Collider:
    arrows=[]
    badguys=[]
    tankers=[]
    thealth=[]
    collplayer=[]
    foods=[]
    heallgauge=194
    heal=None

    def __init__(self,sceen,arrows,badguys,tankers, thealth, player,foods):
        self.screen=sceen
        self.arrows=arrows
        self.badguys=badguys
        self.tankers = tankers
        self.thealth = thealth
        self.collplayer=player
        self.foods=foods

    def collide(self):
        self.heal = Healbar(self.screen, self.heallgauge)
        for arrow in self.arrows:           #화살의 개수 만큼 실행
            for tanker in self.tankers:
                if arrow.colliderect(tanker):
                    if tanker.heall==0:
                        self.tankers.remove(tanker)
                        self.arrows.remove(arrow)
                    else:
                        tanker.heall=tanker.heall-1
                        self.arrows.remove(arrow)
            for badguy in self.badguys:     #몹의 개수 만큼 실행
                if arrow.colliderect(badguy):   #충돌시
                    self.arrows.remove(arrow)   #화살 삭제
                    self.badguys.remove(badguy) #몹 삭제


        for food in self.foods:             #음식(성채)의 개수 만큼
            for badguy in self.badguys:     #몹의 개수 만큼
                if food.colliderect(badguy):#충돌시
                    self.badguys.remove(badguy) #몹 삭제
                    self.heallgauge -= 10
                    self.heal = Healbar(self.screen, self.heallgauge)

        for badguy in self.badguys:
            if self.collplayer.colliderect(badguy):
                self.badguys.remove(badguy)
                self.heallgauge -= 10
                self.heal = Healbar(self.screen, self.heallgauge)
        self.heal.drow()