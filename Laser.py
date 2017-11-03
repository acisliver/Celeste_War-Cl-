#관통 레이저
import pygame

class Laser(pygame.Rect):
    screen = None
    degree=0
    bim =  pygame.image.load("resources/images/laser ball.png")
    charge1 = pygame.image.load("resources/images/laser/laserani1.png")
    charge2 = pygame.image.load("resources/images/laser/laserani2.png")
    charge3 = pygame.image.load("resources/images/laser/laserani3.png")
    charge4 = pygame.image.load("resources/images/laser/laserani4.png")
    charge5 = pygame.image.load("resources/images/laser/laserani5.png")
    charge6 = pygame.image.load("resources/images/laser/laserani6.png")
    charge7 = pygame.image.load("resources/images/laser/laserani7.png")
    charge8 = pygame.image.load("resources/images/laser/laserani8.png")
    charge9 = pygame.image.load("resources/images/laser/laserani9.png")
    charge10 = pygame.image.load("resources/images/laser/laserani10.png")
    charge11 = pygame.image.load("resources/images/laser/laserani11.png")
    charge12 = pygame.image.load("resources/images/laser/laserani12.png")
    charge13 = pygame.image.load("resources/images/laser/laserani13.png")
    bimlist=[]
    for y in range(6):
        for x in range(5):
            bimlist.append((x * 100, y * 100, 100, 100))

    def __init__(self, screen, x ,y,time,num):
        super().__init__(self.bim.get_rect(center=(x-5,y)))
        self.top = x
        self.left = y
        self.height=100
        self.screen = screen
        self.chargelist=[self.charge1,
                         self.charge2,
                         self.charge3,
                         self.charge4,
                         self.charge5,
                         self.charge6,
                         self.charge7,
                         self.charge8,
                         self.charge9,
                         self.charge10,
                         self.charge11,
                         self.charge12,
                         self.charge13,]
        self.time=time
        self.num=num
        self.chek=False
        self.name="Laser"

    def move(self):
        if self.time==0:
            self.time=3
            self.num+=1
        else:
            self.time-=1
        image = pygame.Surface((100, 100))
        image.blit(self.bim,(0, 0),self.bimlist[self.num])
        image.set_colorkey((0, 0, 0))
        self.left-=9
        self.screen.blit(image, (self.top,self.left))
        
    def charge(self):
        self.screen.blit(self.chargelist[self.num], (self.top + 13, self.left - 50))
