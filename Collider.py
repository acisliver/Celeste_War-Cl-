#모든 충돌
import pygame
from Healbar import Healbar

class Collider:
    arrows=[]
    badguys=[]
    tankers=[]
    thealth=[]
    collplayer=[]
    heal=None
    iscolided=False
    current_frame = 0
    now=0
    num=0
    boom = pygame.image.load("resources/images/boom.png")
    boomlist = []
    backup=[]
    playtimer=50
    playercheck=True
    for y in range(8):
        for x in range(9):
            boomlist.append((x * 100, y * 100, 100, 100))

    def __init__(self,sceen,arrows,badguys,tankers,abadguys,fixedmob, thealth, player,healgauge):
        self.screen=sceen
        self.arrows=arrows
        self.badguys=badguys
        self.tankers = tankers
        self.abadguys=abadguys
        self.fixedmob=fixedmob
        self.thealth = thealth
        self.collplayer=player
        self.bullet=[]
        self.num=0
        self.heallgauge =healgauge

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
                        tanker.num = 0
                        self.backup.append(tanker)
                        self.tankers.remove(tanker)
                        if arrow.name == "Laser":
                            pass
                        else:
                            self.iscolided = True
                    else:
                        if arrow.name == "Laser":
                            if arrow.chek==True and tanker.num==1:
                                pass

                            else:
                                tanker.num=1
                                arrow.chek=True
                                tanker.heall = tanker.heall - 1
                        else:
                            tanker.heall = tanker.heall - 1
                            self.iscolided = True
                else:
                    tanker.num = 0

            for badguy in self.badguys:     #몹의 개수 만큼 실행
                if arrow.colliderect(badguy):   #충돌시
                    badguy.time=1
                    self.backup.append(badguy)
                    self.badguys.remove(badguy) #몹 삭제
                    if arrow.name == "Laser":
                        pass
                    else:
                        self.iscolided = True

            for abadguy in self.abadguys:
                for bullet in abadguy.bullets:
                    if arrow.name!="Sector":
                        if arrow.colliderect(bullet):
                            abadguy.bullets.remove(bullet)
                            if arrow.name=="Laser":
                                pass
                            else:
                                self.iscolided = True
                if arrow.colliderect(abadguy):
                    abadguy.time=1
                    self.backup.append(abadguy)
                    self.abadguys.remove(abadguy)
                    if arrow.name == "Laser":
                        pass
                    else:
                        self.iscolided = True
            for fixed in self.fixedmob:  # 몹의 개수 만큼 실행
                if arrow.colliderect(fixed):
                    if arrow.name == "Laser":
                        if arrow.chek == True and fixed.num == 1:
                            pass
                        else:
                            fixed.num = 1
                            arrow.chek = True
                            fixed.heall -= 1
                    else:
                        fixed.heall -= 1
                        self.iscolided = True
                    if fixed.heall == 0:
                        fixed.num = 0
                        fixed.time=1
                        self.backup.append(fixed)
                        self.fixedmob.remove(fixed)
                        if arrow.name == "Laser":
                            pass
                        else:
                            self.iscolided = True
                else:
                    fixed.num = 0
            if self.iscolided == True:
                self.arrows.remove(arrow)   #화살 삭제
                self.iscolided = False

        for badguy in self.badguys:
            if self.collplayer.colliderect(badguy):
                self.badguys.remove(badguy)
                if self.playercheck == True:
                    self.num += 1
                    self.heallgauge -= int(194/5)
                    self.heal = Healbar(self.screen, self.heallgauge)
                    self.playercheck = False
        for abad in self.abadguys:
            for bullet in abad.bullets:
                if self.collplayer.colliderect(bullet):
                    abad.bullets.remove(bullet)
                    if self.playercheck == True:
                        self.num+=1
                        self.heallgauge -= int(194 / 5)
                        self.heal = Healbar(self.screen, self.heallgauge)
                        self.playercheck = False
        for fixed in self.collplayer.fixedbullet:
            if self.collplayer.colliderect(fixed):
                self.collplayer.fixedbullet.remove(fixed)
                if self.playercheck == True:
                    self.num += 1
                    self.heallgauge -= int(194 / 5)
                    self.heal = Healbar(self.screen, self.heallgauge)
                    self.playercheck = False

        if self.playtimer>0 and self.playercheck==False:
            self.playtimer-=1
        else:
            self.playercheck=True
            self.playtimer=50

        self.heal.drow()

    def colltext(self,regamet):
        x=[regamet]
        position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for regame in x:
                    if regame.collidepoint(event.pos):  # ^와 마우스가 충돌했을 경우
                        return 0