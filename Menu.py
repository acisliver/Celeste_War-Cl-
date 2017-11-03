import pygame

class Menu:
    Menubar = pygame.image.load("resources/images/메뉴.png") #체력바 겉칸
    Bar=pygame.image.load("resources/images/네모바.png") #체력바 겉칸
    screen=None
    healvalue=0

    def __init__(self,screen,x):
        self.screen=screen
        self.x=x

    def drow(self):
        self.screen.blit(self.Menubar, (530, 5))    #겉칸 칠하기
        self.screen.blit(self.Bar,(self.x,5))
