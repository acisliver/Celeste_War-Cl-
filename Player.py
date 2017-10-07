#플레이어
import pygame
from Arrow import Arrow
class Player(pygame.Rect):
    screen=None
    arrows=[]
    shot_flag = True
    topBU=900
    Num=0
    playerMove = pygame.image.load('resources/images/PlayerMove.png')
    player = pygame.image.load('resources/images/spaceship.png')
    playerlist = [player, playerMove]
    Start=True

    def __init__(self, screen, x, y):
        super().__init__(self.player.get_rect())    #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.screen=screen
        self.top = x
        self.left =y

    def move(self):                 #wasd 이동키
        pressed=pygame.key.get_pressed()
        if self.left<=300 and self.Start==False:
            self.Num=1
        elif self.left < self.topBU:
            self.topBU = self.left
            self.Num = 1
        else:
            self.topBU = self.left
            self.Num = 0
        if self.Start==False:
            if pressed[pygame.K_UP]!=1 and pressed[pygame.K_DOWN]!=1:
                if self.left <= 800:
                    self.left += 10
            if pressed[pygame.K_UP]:
                if (300 < self.left):
                    self.left -= 15
            if pressed[pygame.K_DOWN]:
                if (self.left < 800):
                    self.left += 15

            if pressed[pygame.K_RIGHT]:
                if (self.top < 600):
                    self.top += 15
            if pressed[pygame.K_LEFT]:
                if (0 < self.top):
                    self.top -= 15
            if pressed[pygame.K_SPACE]:  # 스페이스바를 눌렀을 경우
                if self.shot_flag:  # 먼저 shot_flag의 값 확인(초기에 True로 설정)
                    self.shot()  # 화살이 생성됨
                    self.shot_flag = False  # shot_flag를 False로 바꿔줌
            else:  # 스페이스바를 누르지 않고있을 경우
                self.shot_flag = True  # shot_flag를 다시 True로 바꿔줌
        else:
            if self.left <= 800:
                self.left += 10


                                     # shot_flag가 True일 경우에만 화살이 나가게 함(눌렀다 때야 다시 눌렀을 경우 화살이 날아감)
        for arrow in self.arrows:
            arrow.move()            #화살이 날아감

        self.screen.blit(self.playerlist[self.Num], (self.top, self.left))

    def shot(self):                 #화살생성함수
        arrow = Arrow(self.screen, self.top, self.left, 35 )    #speed가 30인 화살 생성
        self.arrows.append(arrow)                               #list에 arrow객체 추가