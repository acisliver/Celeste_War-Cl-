import pygame

class Badguy(pygame.Rect):
    speed=0
    num=0
    timer=1
    screen = None
    MobNum=0
    degree = 0
    badguyimg = pygame.image.load("resources/images/Mob/Mob1.png")


    def __init__(self, screen, x, y, speed,time,num):
        super().__init__(self.badguyimg.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.speed = speed
        self.screen = screen
        self.time=time
        self.num=num
        self.width=70
        self.height=70
        self.top = x - self.height/2
        self.left = y - self.width/2

    def move(self):             #몹 움직임 함수
        rotated = pygame.transform.rotate(self.badguyimg, self.degree)
        rect = rotated.get_rect()
        rect.center = (self.top+self.height/2, self.left+self.width/2)
        self.left += self.speed
        self.screen.blit(rotated,rect)
        self.degree+=5
        if self.degree>359:
            self.degree=0