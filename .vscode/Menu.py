import pygame, sys
import random
from datetime import datetime
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

#Set  game screen
WIDTH = 1000
HEIGHT = 600
GAMESCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

#set color
WHITE = (255,255,255)
RED = (255,0,0)
LIGHT_RED = (200,0,0)
GREEN = (0,255,0)
LIGHT_GREEN = (0,200,0)
BLUE = (0,0,255)
LIGHT_BLUE = (0,0,200)
BLACK = (0,0,0)
GRAY = (200,200,200)

car_width = 50
Speedbuff = 1
Speednerf = 1
Distance_Buff = 100
Distance_Nerf = 100

start_line = 20
end_line = 950

#font
font = pygame.font.SysFont('batmfo__', 20)
Play_menu = font.render('PLAY', True, BLACK)
Instruction_menu = font.render('INSTRUCTION',True,BLACK)
Exit_menu = font.render('EXIT',True,BLACK)


#image Menu
Menu = pygame.image.load("background.png")
Menu = pygame.transform.scale(Menu,(WIDTH,HEIGHT))

def _Menu(Menu):
    GAMESCREEN.blit(Menu,(0,0))
    #mấy cái này là vẽ hình chữ nhật rồi thêm chữ vào
    pygame.draw.rect(GAMESCREEN,BLACK,(425,275,150,30),2)
    GAMESCREEN.blit(Play_menu,(480,282))
    
    pygame.draw.rect(GAMESCREEN,BLACK,(425,325,150,30),2)
    GAMESCREEN.blit(Instruction_menu,(458,332))
   
    pygame.draw.rect(GAMESCREEN,BLACK,(425,375,150,30),2)
    GAMESCREEN.blit(Exit_menu,(480,382))

def Chonlenh(x,y):
    #Mấy cái này là lúc mình di chuột vô ô của nó nó sẽ đổi thành màu xám
    if (x > 425) and ( x < 575) and (y > 275) and (y < 305):
        pygame.draw.rect(GAMESCREEN,GRAY,(425,275,150,30))
        GAMESCREEN.blit(Play_menu,(480,282))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                #bat dau tro choi
                return 1 # Thực hiện hàm play game nếu giá trị trả về bằng 1
    
    if (x > 425) and ( x < 575) and (y > 325) and (y < 355):
        pygame.draw.rect(GAMESCREEN,GRAY,(425,325,150,30))
        GAMESCREEN.blit(Instruction_menu,(458,332))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                #huong dan choi
                return 2 # Thực hiện hàm hướng dẫn chơi nếu giá trị trả về  bằng 2

    if (x > 425) and ( x < 575) and (y > 375) and (y < 405):
        pygame.draw.rect(GAMESCREEN,GRAY,(425,375,150,30))
        GAMESCREEN.blit(Exit_menu,(480,382))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                #exit game
                return 3#  Ham thoat khoi chuong trinh khi gia tri return tra ve 3
    

while True:
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    _Menu(Menu)
    #cái này là tui test chức năng từng hàm play, exit, instruction thôi, ko quan tâm lắm đâu
    k = Chonlenh(mouse_x,mouse_y)
    if (k == 1):
        print("1")
    if (k == 2):
        print("2")
    if (k == 3) :
        pygame.quit()
        sys.exit()
    pygame.display.flip()