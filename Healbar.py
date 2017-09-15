#체력바
import pygame

class Healbar:
    healthbar = pygame.image.load("resources/images/healthbar.png") #체력바 겉칸
    health = pygame.image.load("resources/images/health.png")       #체력(초록색부분)
    screen=None
    healvalue=0

    def __init__(self,screen,healvalue):
        self.screen=screen
        self.healvalue=healvalue

    def drow(self):
        self.screen.blit(self.healthbar, (5, 5))    #겉칸 칠하기
        for heal in range(self.healvalue):          #체력이 체력값(healvalue)에 만큼 체력 칠하기
            self.screen.blit(self.health, (heal + 8, 8))