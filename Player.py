#플레이어
import pygame
from Arrow import Arrow
from Sector1 import Sector1
from Sector2 import Sector2
from Sector3 import Sector3
from Laser import Laser
#from Laser import Laser

class Player(pygame.Rect):
    screen=None
    arrows=[]
    sectors=[]
    shot_flag = True
    weapon = "Normal"
    weapon_flag = True
    topBU=900
    Num=0
    charge=50
    playerMove = pygame.image.load('resources/images/PlayerMove.png')
    player = pygame.image.load('resources/images/spaceship.png')
    playerlist = [player, playerMove]
    Start=True
    alpha=255
    lasertime=1
    lasernum=0

    def __init__(self, screen, x, y):
        super().__init__(self.player.get_rect(center=(x,y)))    #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.height=50
        self.screen=screen
        self.top = x+25
        self.left =y
        self.collidercheck=True
        self.playertimer=5


    def move(self):                 #wasd 이동키

        pressed=pygame.key.get_pressed()
        if self.left<=400 and self.Start==False:
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
                if (400 < self.left):
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
                    if self.weapon=="Sector":
                        self.sector_shot()
                        self.shot_flag = False
                    elif self.weapon=="Normal":
                        self.shot()  # 화살이 생성됨
                        self.shot_flag=False
                    elif self.weapon=="Laser":
                        laser = Laser(self.screen, self.top-25, self.left, self.lasertime, self.lasernum)
                        if self.charge==0:
                            self.laser_shot()
                            self.charge=50
                            self.shot_flag=False
                            if self.lasertime!=2:
                                self.lasertime = 2
                                self.lasernum = 0
                        else:
                            if self.lasertime == 0:
                                self.lasernum += 1
                                self.lasertime = 2
                            else:
                                self.lasertime -= 1
                            if self.lasernum == 13:
                                self.lasernum = 0
                            laser.charge()
                            self.charge-=1
            else:
                self.charge = 50
                self.lasertime = 2
                self.lasernum = 0
                self.shot_flag = True

                    
            if pressed[pygame.K_x]:
                if self.weapon_flag:
                    if self.weapon=="Normal":
                        self.weapon = "Sector"
                    elif self.weapon=="Sector":
                        self.weapon = "Laser"
                    elif self.weapon == "Laser":
                        self.weapon = "Normal"
                    self.weapon_flag = False
            elif pressed[pygame.K_z]:
                if self.weapon_flag:
                    if self.weapon=="Normal":
                        self.weapon = "Laser"
                    elif self.weapon=="Sector":
                        self.weapon = "Normal"
                    elif self.weapon == "Laser":
                        self.weapon = "Sector"
                    self.weapon_flag = False
            else:
                self.weapon_flag = True

        elif self.Start==True:
            self.left+=0
        else:
            if self.left <= 800:
                self.left += 10

        for sector in self.arrows:
            if sector.name == "Sector":
                if sector.timer>=8:
                    self.arrows.remove(sector)

        for arrow in self.arrows:
            arrow.move()            #화살이 날아감

        if self.collidercheck==False:
            image = pygame.Surface((100, 100))
            image.blit(self.playerlist[self.Num], (0, 0))
            image.set_colorkey((0, 0, 0))
            image.set_alpha(self.alpha)
            self.screen.blit(image, (self.top-25, self.left))
            if self.alpha==255 and self.playertimer==0:
                self.alpha=0
                self.playertimer=3
            else:
                self.playertimer-=1
                self.alpha=255
        elif self.collidercheck==True:
            self.screen.blit(self.playerlist[self.Num], (self.top-25, self.left))



    def shot(self):         #화살생성함수
        arrow = Arrow(self.screen, self.top-25, self.left, 35 )    #speed가 30인 화살 생성
        self.arrows.append(arrow)                               #list에 arrow객체 추가

    def sector_shot(self):
        sector1 = Sector1(self.screen, self.top-25, self.left, 35,0)
        self.arrows.append(sector1)
        sector2 = Sector2(self.screen, self.top-25, self.left, 35,0)
        self.arrows.append(sector2)
        sector3 = Sector3(self.screen, self.top-25, self.left, 35,0)
        self.arrows.append(sector3)

    def laser_charge(self):
        print(self.charge)

    def laser_shot(self):
        laser = Laser(self.screen, self.top-25, self.left, self.lasertime, self.lasernum)
        self.arrows.append(laser)