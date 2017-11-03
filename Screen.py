import pygame
import random
import math
from Player import Player
from Badguy import Badguy
from Tanker import Tanker
from Abadguy import Abadguy
from Collider import Collider
from WL import WL
from Timer import Timer
from Screen2 import Screen2
from Menu import Menu
from Bullet import Bullet
class Screen:
    width=700
    height =900
    badtimer = 10
    tbadtimer=6
    bYtimer=200
    badguys=[]
    tankers=[]
    abadguys=[]
    thealth = None
    badguy=None
    abadguy=None
    x=300
    y=900
    exitcode = 0
    count=67
    one_count=0
    tcheck=False
    acheck=False
    tmax=0
    amax=0
    rsX=50
    alpha=255
    bY=0
    bYplus=10
    num=0
    collidercheck=False
    playercheck=False
    startcheck=True

    background = pygame.image.load('resources/images/background.png')
    gameover = pygame.image.load("resources/images/gameover.png")
    youwin = pygame.image.load("resources/images/youwin.png")

    player=[]
    collider=None
    wl = None
    heallvalue=None
    timer=None
    fpsClock = pygame.time.Clock()
    FPS = 100

    screen = pygame.display.set_mode((width, height))       #화면 해상도
    bg_columns = background.get_width()                     #화면 너비 불러오기
    bg_rows = background.get_height()                       #화면 높이 불러오기
    pygame.display.set_caption("Celeste_War")

    def __init__(self):
        self.player = Player(self.screen, self.x, self.y)
        self.healgauge=194
        self.collider=Collider(self.screen,self.player.arrows+self.player.sectors,self.badguys,self.tankers,self.abadguys, self.thealth, self.player,self.healgauge)
        self.wl=WL(self.screen,self.exitcode)
        self.timer=Timer(self.screen,self.count)
        self.screen2=Screen2(self.screen,self.width,self.height)

    def Drow_background(self,bY):
        self.screen.blit(self.background, (0,bY))
        if bY>1:
            self.screen.blit(self.background,(0,bY-1000))

    def Move(self,badguys,tankers, abadguys):
        for badguy in badguys:  # 몹의 객체만큼
            if badguy.time==0:
                badguy.move()  # 몹 이동 함수
            else:
                badguy.time-=1
        for tanker in tankers:  # 탱커 만큼
            tanker.move()  # 탱커 무브
        for abadguy in abadguys:    #원거리 만큼
            abadguy.move()  #원거리 무브
        pygame.display.update()

    def StartPrint(self,timer,rsX ,alpha):
        pygame.font.init()
        font = pygame.font.Font("resources/font/consola.ttf", 50)
        if timer > 61:
            text = font.render(str(timer - 61), True, (255, 0, 0))  # count를 그리는 폰트 생성
        else:
            font = pygame.font.Font("resources/font/consola.ttf",rsX)
            text = font.render(str("Start"), False, (255, 0, 0))  # count를 그리는 폰트 생성
            text.set_alpha(alpha)
        textRect = text.get_rect()
        textRect.center = (350, 500)
        self.screen.blit(text, textRect)
    def StartAbadmove(self,abadguys):
        for abad in abadguys:
            if abad.time == 0:
                if 0 <= abad.round <= 90 or 270 < abad.round <= 360:
                    abad.left -= 10
                else:
                    abad.left -= 11

                if abad.round < 180:
                    abad.round += 1
                elif abad.round > 180:
                    abad.round -= 1
                if abad.round <= 90:
                    abad.top -= 10 * float("%.3f" % math.cos(math.radians(abad.round))) + 2
                    b = abad.round
                elif abad.round >= 270:
                    abad.top += 10 * float("%.3f" % math.cos(math.radians(abad.round))) + 2
                    b = abad.round
                else:
                    if abad.round <= 90:
                        b = 90
                    else:
                        b = 270
            else:
                abad.time -= 1
            if abad.round < 91:
                abad.startmove(90 - b)
            else:
                abad.startmove(270 - b)

    def Start(self):
        self.badguys=[]
        self.player.arrows=[]
        self.player.sectors=[]
        self.abadguys=[]
        self.timer.timer()
        self.tmax = self.timer.tmax
        self.amax = self.timer.amax
        if 1<=self.tmax:
            self.tcheck=True
        if 1<=self.amax:
            self.acheck=True
        while True:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.timer.exidcode=0
                    exit(0)
            pygame.display.update() #업데이트
            game=Screen()
            game.Drow_background(self.bY)

            self.bY += self.bYplus
            if self.bY>=1000:
                self.bY=0
            if self.bYtimer==0:
                self.bYplus+=1
                self.bYtimer=200
            else:
                self.bYtimer-=1

            self.player.move()  # 플레이어 무브함수

            if self.timer.count>60:
                if self.startcheck==True:
                    for x in range(0, 5):
                        abadguy = Abadguy(self.screen, 800, 900, 3, x*10, 0,15)
                        self.abadguys.append(abadguy)
                        abadguy = Abadguy(self.screen, 0, 900, 3, x * 10, 0, 345)
                        self.abadguys.append(abadguy)
                    self.startcheck=False
                game.StartAbadmove(self.abadguys)
                game.StartPrint(self.timer.count,self.rsX,self.alpha)
                if self.timer.count<=61:
                    self.rsX += 4
                    self.alpha -= 6
                    for abad in self.abadguys:
                        self.abadguys.remove(abad)
                    for badguy in self.badguys:
                        self.badguys.remove(badguy)
                    for tanker in self.tankers:
                        self.tankers.remove(tanker) 
                    for Bu in self.collider.backup:
                        self.collider.backup.remove(Bu)
                if self.player.left <= 740:
                    self.playercheck = True

                if self.playercheck == False:
                    self.player.left -= 2
                elif self.playercheck == True and 800 > self.player.left:
                    self.player.left += 1

            else:
                self.player.Start = False
                self.timer.print()  # 타이머 그리기
                self.collider.collide()  # 충돌 함수
                self.player.collidercheck=self.collider.playercheck
                self.collider.badguys = self.badguys
                self.collider.abadguys=self.abadguys
                self.collider.arrows = self.player.arrows
                self.healgauge = self.collider.heallgauge
                if self.collider.playercheck==False:
                    self.collidercheck=True
                game.Move(self.badguys, self.tankers, self.abadguys)
                menu=Menu(self.screen,self.player.menuX)
                menu.drow()
                pygame.display.update()

                self.badtimer = self.timer.badtimer
                if self.badtimer == 0:
                    for x in range(0, 10):
                        badguy = Badguy(self.screen,
                                        random.randint(50, self.width - 50), 0, self.bYplus-5, random.randint(0,20), 0)  # 위치랜덤의 속도8인 몹 객체 생성
                        self.badguys.append(badguy)  # 리스트에 추가
                    if self.timer.max == 0:
                        self.timer.badtimer = 100
                    else:
                        self.timer.badtimer = round(60 / self.timer.max)
                if self.tcheck == True:
                    for x in range(0, self.tmax):
                        tanker = Tanker(self.screen, random.randint(50, self.width - 50), 0, 1, 7, 1, 0)
                        self.tankers.append(tanker)
                        self.tcheck = False
                if self.acheck == True:
                    for x in range(0, self.amax):
                        abadguy = Abadguy(self.screen, random.randint(50, self.width - 50), 0, 3, random.randint(0,7), -1,0)
                        self.abadguys.append(abadguy)
                        self.acheck = False
                self.one_count = self.timer.count  # 타이머의 count와 같은 one_count
                if self.one_count == 0:  # one_count가 0보다 이하일 때
                    self.exitcode = 1
                    self.wl.exitcode = self.exitcode  # wl의 exitcode를 1로 바꿈
                    break

                if self.healgauge < 0:
                    break

        if self.healgauge < 0:  #체력게이지가 0보다 작으면
            while 1:
                for event in pygame.event.get():  # 종료 이벤트
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)
                self.wl.print()  # win or lose 출력
                x=self.collider.colltext(self.wl.regame)
                if x==0:
                    return

    def Starting(self):
        while True:
            self.screen2.Start()#스크린2 실행
            game = Screen()
            game.Start()#스크린1 실행

game2 = Screen()
game2.Starting()            #실행부