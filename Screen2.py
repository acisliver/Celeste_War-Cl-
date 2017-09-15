import pygame

class Screen2:
    width = 0
    height = 0
    screen = None

    numlist = [0, 0, 0]
    list = []
    max=0 #숫자의 최종값
    badguyimg = pygame.image.load("resources/images/badguy.png")
    def __init__(self,screen,width,height):
        self.width=width
        self.screen=screen
        self.height=height

    def Start(self):
        finished=0
        while not finished:
            position = pygame.mouse.get_pos()   #마우스 위치 불러오기

            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for lists in self.list:
                        if lists == self.list[0]:               #list = ^
                            if lists.collidepoint(event.pos):   #^와 마우스가 충돌했을 경우
                                if self.numlist[2] < 9:         #1의 자리가 9보다 작으면
                                    self.numlist[2] = self.numlist[2] + 1   #1더하기
                                    break
                        if lists == self.list[1]:               #10의 자리 더하기
                            if lists.collidepoint(event.pos):
                                if self.numlist[1] < 9:
                                    self.numlist[1] = self.numlist[1] + 1
                                    break
                        if lists == self.list[2]:               #100의 자리 더하기
                            if lists.collidepoint(event.pos):
                                if self.numlist[0] < 9:
                                    self.numlist[0] = self.numlist[0] + 1
                                    break
                        if lists == self.list[3]:               #1의 자리 빼기
                            if lists.collidepoint(event.pos):
                                if self.numlist[2] > 0:
                                    self.numlist[2] = self.numlist[2] - 1
                                    break
                        if lists == self.list[4]:               #10의 자리 빼기
                            if lists.collidepoint(event.pos):
                                if self.numlist[1] > 0:
                                    self.numlist[1] = self.numlist[1] - 1
                                    break
                        if lists == self.list[5]:               #100의 자리 빼기
                            if lists.collidepoint(event.pos):
                                if self.numlist[0] > 0:
                                    self.numlist[0] = self.numlist[0] - 1
                                    break
                        if lists == self.list[6]:
                            if lists.collidepoint(event.pos):   #Start를 눌렀을 때
                                self.max = (self.numlist[0] * 100) + (self.numlist[1] * 10) + self.numlist[2]   #몹의 수 총합 계산
                                self.numlist = [0, 0, 0]    #numlist 초기화
                                finished=1                  #while문 종료
                                break

            self.screen.fill((0, 0, 0))     #검정색으로 칠하기
            self.screen.blit(self.badguyimg, (140, 410))        #몹 칠하기

            pygame.font.init()              #폰트 초기화
            font = pygame.font.Font("resources/font/consola.ttf", 40)   #폰트 불러오기
            text = font.render(str(("%d%d%d" % (self.numlist[0], self.numlist[1], self.numlist[2]))), True, (225, 225, 225))    #numlist폰트 객체 생성
            textRect = text.get_rect()      #numlist폰트 위치 불러오기
            textRect.center = (230, 425)    #numlist폰트 중앙 좌표 지정
            self.screen.blit(text, textRect)#numlist 칠하기

            text = font.render("^", True, (225, 225, 225))  #^폰트 객체 생성
            textRect1 = text.get_rect()
            textRect1.center = (248, 405)
            textRect2 = text.get_rect()
            textRect2.center = (231, 405)
            textRect3 = text.get_rect()
            textRect3.center = (214, 405)

            text1 = font.render("v", True, (225, 225, 225)) #v폰트 객체 생성
            MIRect1 = text1.get_rect()
            MIRect1.center = (248, 445)
            MIRect2 = text1.get_rect()
            MIRect2.center = (231, 445)
            MIRect3 = text1.get_rect()
            MIRect3.center = (214, 445)

            Startfont = pygame.font.Font("resources/font/consola.ttf", 40)  #폰트 불러오기
            Starttext = Startfont.render("Start", True, (225, 225, 225))        #Start객체 생성
            StarttextRect = Starttext.get_rect()
            StarttextRect.center = (700, 400)
            self.screen.blit(Starttext, StarttextRect)

            self.list = [textRect1, textRect2, textRect3, MIRect1, MIRect2, MIRect3, StarttextRect] #list에 ^^^vvv 넣기

            for y in range(0, 3):   #^^^그리기
                self.screen.blit(text, self.list[y])
            for x in range(3, 6):   #vvv그리기기
               self.screen.blit(text1, self.list[x])
            pygame.display.flip()   #화면 전체 업데이트