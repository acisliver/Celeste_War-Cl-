import pygame


class Food(pygame.Rect):
    screen=None
    castle = pygame.image.load('resources/images/castle.png')

    def __init__(self, screen,x, y):
        super().__init__(self.castle.get_rect())        #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.screen=screen
        self.top=x
        self.left=y

    def drow(self):                                     #성을 8개 그리는 함수
        for i in range(0,8):
            self.screen.blit(self.castle, (self.top, self.left*i))