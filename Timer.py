#타이머(게임 남은 시간)
import pygame
import threading

class Timer:
    screen=None
    tmax=0
    max=0
    count=0
    exidcode=1
    badtimer=0
    tbadtimer=0

    def __init__(self,screen,count):
        self.screen=screen
        self.count=count

    def timer(self):
        time=threading.Timer(1,self.timer)  #1초마다 반복
        if self.badtimer==0:
            self.badtimer = round(60 / self.max)
        self.count -= 1                     #1씩 빠짐
        self.badtimer=self.badtimer-1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                time.cancel()               #1초마다 반복 취소

        time.start()                        #시작

        if self.count<=0:
            time.cancel()

    def print(self):
        pygame.font.init()
        font = pygame.font.Font("resources/font/consola.ttf", 35)
        text = font.render(str(self.count), True, (255, 0, 0))      #count를 그리는 폰트 생성
        textRect = text.get_rect()
        textRect.center = (600, 35)
        self.screen.blit(text, textRect)