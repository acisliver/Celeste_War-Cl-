#플레이어
import pygame
from Arrow import Arrow
class Player(pygame.Rect):
    screen=None
    arrows=[]
    shot_flag = True
    player = pygame.image.load('resources/images/dude2.png')

    def __init__(self, screen, x, y):
        super().__init__(self.player.get_rect())    #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.screen=screen
        self.top = x
        self.left =y

    def move(self):                 #wasd 이동키
        pressed=pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            if (0 < self.left):
                self.left -= 20
        if pressed[pygame.K_s]:
            if (self.left < 760):
                self.left += 20
        if pressed[pygame.K_d]:
            if (self.top < 1200):
                self.top += 20
        if pressed[pygame.K_a]:
            if (0 < self.top):
                self.top -= 20
        if pressed[pygame.K_SPACE]: #스페이스바를 눌렀을 경우
            if self.shot_flag:      #먼저 shot_flag의 값 확인(초기에 True로 설정)
                self.shot()         #화살이 생성됨
                self.shot_flag=False #shot_flag를 False로 바꿔줌

        else:                       #스페이스바를 누르지 않고있을 경우
            self.shot_flag=True     #shot_flag를 다시 True로 바꿔줌
                                     # shot_flag가 True일 경우에만 화살이 나가게 함(눌렀다 때야 다시 눌렀을 경우 화살이 날아감)
        for arrow in self.arrows:
            arrow.move()            #화살이 날아감

        self.screen.blit(self.player,(self.top,self.left))

    def shot(self):                 #화살생성함수
        arrow = Arrow(self.screen, self.top, self.left, 30 )    #speed가 30인 화살 생성
        self.arrows.append(arrow)                               #list에 arrow객체 추가