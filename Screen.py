import pygame
import random
from Player import Player
from Badguy import Badguy
from Collider import Collider
from Food import Food
from WL import WL
from Timer import Timer
from Screen2 import Screen2

class Screen:
    width=1200
    height = 800
    badtimer = 6
    badguys=[]
    tankers=[]
    thealth=[0, 1, 2]   #탱커의 체력
    foods = []
    badguy=None
    x=100
    y=100
    food_x=0
    food_y=105
    exitcode = 0
    count=60
    one_count=0

    background = pygame.image.load('resources/images/grass.png')
    gameover = pygame.image.load("resources/images/gameover.png")
    youwin = pygame.image.load("resources/images/youwin.png")

    player=[]
    collider=None
    wl = None
    food = []
    heallvalue=None
    timer=None

    fpsClock = pygame.time.Clock()
    FPS = 100

    screen = pygame.display.set_mode((width, height))       #화면 해상도
    bg_columns = background.get_width()                     #화면 너비 불러오기
    bg_rows = background.get_height()                       #화면 높이 불러오기

    def __init__(self):
        self.player = Player(self.screen ,self.x,self.y)
        self.collider=Collider(self.screen,self.player.arrows,self.badguys,self.tankers, self.thealth, self.player,self.foods)
        self.food = Food(self.screen,self.food_x, self.food_y)
        self.wl=WL(self.screen,self.exitcode)
        self.timer=Timer(self.screen,self.count)
        self.screen2=Screen2(self.screen,self.width,self.height)

    def Start(self):
        self.timer.timer()
        while True:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update() #업데이트

            for i in range(int(self.width // self.bg_columns) + 1):     #배경 채우기
                for j in range(int(self.height // self.bg_rows) + 1):
                    self.screen.blit(self.background, (i * self.bg_columns, j * self.bg_rows))

            self.timer.print()      #타이머 그리기

            self.food.drow()        #성 그리기

            for i in range(0, 8):   #성 객체 생성 후 리스트에 넣기
                food = Food(self.screen, self.food_x, self.food_y * i)
                self.foods.append(food)

            self.player.move()      #플레이어 무브함수
            self.collider.collide() #충돌 함수
            self.healgauge = self.collider.heallgauge
            self.one_count = self.timer.count       #타이머의 count와 같은 one_count
            pygame.display.update()

            if self.one_count <= 0:     #one_count가 0보다 이하일 때
                self.badguys=[]         #배드가이 사라짐
                self.exitcode = 1
                self.wl.exitcode = self.exitcode    #wl의 exitcode를 1로 바꿈
                break
            else:
                for badguy in self.badguys: #몹의 객체만큼
                    badguy.move()   #몹 이동 함수
                pygame.display.update()

                self.badtimer -= 1
                if self.badtimer == 0:
                    badguy = Badguy(self.screen, self.width,
                                    random.randint(50, self.height - 50), 16)    #위치랜덤의 속도8인 몹 객체 생성
                    self.badguys.append(badguy)                                 #리스트에 추가
                    self.badtimer = 6

            if self.healgauge < 0:
                break
        if self.healgauge < 0:  #체력게이지가 0보다 작으면
            self.wl.print()     #win or lose 출력

    def Starting(self):
        while True:
            self.screen2.Start()    #스크린2 실행
            game = Screen()
            game.Start()            #스크린1 실행


game2 = Screen()
game2.Starting()            #실행부