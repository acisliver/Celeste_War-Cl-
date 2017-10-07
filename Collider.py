#모든 충돌
import pygame
from Healbar import Healbar

class Collider:
    arrows=[]
    badguys=[]
    tankers=[]
    thealth=[]
    collplayer=[]
    heallgauge=194
    heal=None
    iscolided=False
    current_frame = 0
    now=0
    num=0
    boom = pygame.image.load("resources/images/boom.png")
    boomlist = []
    backup=[]
    for y in range(8):
        for x in range(9):
            boomlist.append((x * 100, y * 100, 100, 100))

    def __init__(self,sceen,arrows,badguys,tankers,abadguys, thealth, player):
        self.screen=sceen
        self.arrows=arrows
        self.badguys=badguys
        self.tankers = tankers
        self.abadguys=abadguys
        self.thealth = thealth
        self.collplayer=player

    def collide(self):
        self.heal = Healbar(self.screen, self.heallgauge)
        for arrow in self.arrows:
            if arrow.left<0:
                self.arrows.remove(arrow)
        for backupdata in self.backup:
            backupdata.time -= 1
            if backupdata.time == 0:
                if backupdata.num > 68:
                    self.backup.remove(backupdata)
                self.screen.blit(self.boom, (backupdata.top, backupdata.left), self.boomlist[backupdata.num])
                backupdata.left+=10
                backupdata.num += 1
                backupdata.time = 1
        for arrow in self.arrows:           #화살의 개수 만큼 실행
            for tanker in self.tankers:
                if arrow.colliderect(tanker):
                    if tanker.heall == 0:
                        self.backup.append(tanker)
                        self.tankers.remove(tanker)
                        self.iscolided = True
                    else:
                        tanker.heall = tanker.heall - 1
                        self.iscolided = True

            for badguy in self.badguys:     #몹의 개수 만큼 실행
                if arrow.colliderect(badguy):   #충돌시
                    self.backup.append(badguy)
                    self.badguys.remove(badguy) #몹 삭제
                    self.iscolided = True

            for abadguy in self.abadguys:
                if arrow.colliderect(abadguy):
                    self.backup.append(abadguy)
                    self.abadguys.remove(abadguy)
                    self.iscolided=True
            if self.iscolided == True:
                self.arrows.remove(arrow)   #화살 삭제
                self.iscolided = False


        for badguy in self.badguys:
            if self.collplayer.colliderect(badguy):
                self.badguys.remove(badguy)
                self.heallgauge -= 10
                self.heal = Healbar(self.screen, self.heallgauge)
        self.heal.drow()