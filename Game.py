import pygame
import sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH=800 
WINDOWHEIGHT=1000
WHITE = (255, 255, 255)
check=False



FPS = 120
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Racing')

class Cars():
    def __init__(self):
        self.x=0
        self.y=500
    def update(self, moveLeft, moveRight, moveUp,moveDown,move,enter): 
        
  
        if enter==True:
            self.x+=2
     


    def draw(self):
        pygame.draw.rect(DISPLAYSURF,(0,0,0),(self.x,self.y,10,10))


def check_win(p1,p2):
    if p1==p2 :
        return True
    return False
def over(car,goal):
    if check_win(car.x,goal.x)==True :
        DISPLAYSURF.blit(label,(0,0))



class Goal():
    def __init__(self):
        self.x=700
        self.y=500
    def draw(self):
        pygame.draw.rect(DISPLAYSURF,(0,0,0),(self.x,self.y,50,200))


car=Cars()
enter=False
goal=Goal()
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
move = False
font=pygame.font.SysFont("consolar",20)
label=font.render("f",True,(0,255,255),(0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                enter=True
        
        
        if event.type == KEYUP:
            if event.key == K_RETURN:
                enter=True
    
    DISPLAYSURF.blit(label,(50,100))
    over(car,goal)
    DISPLAYSURF.fill(WHITE)
    car.draw()
    goal.draw()
    car.update(moveLeft, moveRight,moveUp,moveDown,move,enter)
    
    pygame.display.update()
    fpsClock.tick(FPS)
