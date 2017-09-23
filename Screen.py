import pygame
import random
from Player import Player
from Badguy import Badguy
from Tanker import Tanker
from Collider import Collider
from WL import WL
from Timer import Timer
from Screen2 import Screen2
class Screen:
    width=800
    height =1000
    badtimer = 10
    tbadtimer=6
    badguys=[]
    tankers=[]
    thealth=[0, 1, 2]   #탱커의 체력
    badguy=None
    x=350
    y=900
    exitcode = 0
    count=60
    one_count=0
    tcheck=False
    tmax=0
    bX=0
    bY=0

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
        self.player = Player(self.screen ,self.x,self.y)
        self.collider=Collider(self.screen,self.player.arrows,self.badguys,self.tankers, self.thealth, self.player)
        self.wl=WL(self.screen,self.exitcode)
        self.timer=Timer(self.screen,self.count)
        self.screen2=Screen2(self.screen,self.width,self.height)

    def Drow_background(self,bY):
        self.screen.blit(self.background, (0,bY))
        if bY>1:
            self.screen.blit(self.background,(0,bY-1000))
    def Move(self,badguys,tankers):
        for badguy in badguys:  # 몹의 객체만큼
            badguy.move()  # 몹 이동 함수
        for tanker in tankers:  # 탱커 만큼
            tanker.move()  # 탱커 무브
        pygame.display.update()

    def Start(self):
        self.badguys=[]
        self.player.arrows=[]
        self.timer.timer()
        self.tmax = self.timer.tmax
        if 1<=self.tmax:
            self.tcheck=True
        while True:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update() #업데이트

            game=Screen()
            game.Drow_background(self.bY)
            self.bY += 10
            if self.bY==1000:
                self.bY=0

            self.timer.print()      #타이머 그리기
            self.player.move()      #플레이어 무브함수
            self.collider.collide() #충돌 함수
            self.collider.badguys = self.badguys
            self.collider.arrows = self.player.arrows
            self.healgauge = self.collider.heallgauge

            game.Move(self.badguys,self.tankers)
            pygame.display.update()

            self.badtimer = self.timer.badtimer
            if self.badtimer == 0:
                for x in range(0, 5):
                    badguy = Badguy(self.screen,
                                    random.randint(50, self.width - 50),0, 20,1,0)  # 위치랜덤의 속도8인 몹 객체 생성
                    self.badguys.append(badguy)  # 리스트에 추가
                if self.timer.max==0:
                    self.timer.badtimer=100
                else:
                    self.timer.badtimer = round(60 / self.timer.max)
            if self.tcheck == True:
                for x in range(0, self.tmax):
                    tanker = Tanker(self.screen, random.randint(50, self.width - 50),200, 8, 1,1,0)
                    self.tankers.append(tanker)
                    self.tcheck = False

            self.one_count = self.timer.count  # 타이머의 count와 같은 one_count
            if self.one_count == 0:     #one_count가 0보다 이하일 때
                self.exitcode = 1
                self.wl.exitcode = self.exitcode    #wl의 exitcode를 1로 바꿈
                break

            if self.healgauge < 0:
                break
        if self.healgauge < 0:  #체력게이지가 0보다 작으면
            self.wl.print()     #win or lose 출력

    def Starting(self):
        while True:
            self.screen2.Start()#스크린2 실행
            game = Screen()
            game.Start()#스크린1 실행


game2 = Screen()
game2.Starting()            #실행부