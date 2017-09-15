#게임 종료시 나타나는 win or lose문구
import pygame

class WL:
    exitcode=0
    screen=None

    def __init__(self,screen,exitcode):
        self.screen=screen
        self.exitcode=exitcode

    def print(self):
        if self.exitcode == 0:              #exitcode는
            pygame.font.init()              #폰트 초기화
            font=pygame.font.Font("resources/font/consola.ttf",100)     #폰트 불러오기
            text=font.render("You Lose",True,(255, 0, 0))                 #빨간색 폰트 객체 생성
            textRect=text.get_rect()                                        #폰트 위치 불러오기
            textRect.center=(600,400)                                       #폰트 위치 지정
            self.screen.blit(text,textRect)                                 #폰트 블릿
        else:
            pygame.font.init()                                              #위와 같은 과정
            font = pygame.font.Font("resources/font/consola.ttf", 100)
            text = font.render("You Win!!", True, (29,219,22))
            textRect = text.get_rect()
            textRect.center = (600, 400)
            self.screen.blit(text, textRect)

        while 1:
            for event in pygame.event.get():            #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.flip()