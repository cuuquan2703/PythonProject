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
Speedbuff = 2
Speednerf = 2
Distance_Buff = 100
Distance_Nerf = 100

start_line = 20
end_line = 950

#image
race_track = pygame.image.load("racetrack(snow).png")
race_track_render = pygame.transform.scale (race_track,(1000,350))

clock = pygame.image.load("question.png")
clock_render = pygame.transform.scale(clock,(30,30))

clover = pygame.image.load("question.png")
clover_render = pygame.transform.scale(clover,(30,30))

fire_wheel = pygame.image.load("question.png")
fire_wheel_render = pygame.transform.scale(fire_wheel,(30,30))

lucky = pygame.image.load("question.png")
lucky_render = pygame.transform.scale(lucky,(30,30))

slow_motion = pygame.image.load("question.png")
slow_motion_render = pygame.transform.scale(slow_motion,(30,30))

snail = pygame.image.load("question.png")
snail_render = pygame.transform.scale(snail,(30,30))

snowflake = pygame.image.load("question.png")
snowflake_render = pygame.transform.scale(snowflake,(30,30))

warning = pygame.image.load("question.png")
warning_render = pygame.transform.scale(warning,(30,30))

#image car
carBlue = pygame.image.load("CarBlue.png")
carBlue = pygame.transform.scale (carBlue,(50,30))

carOrange = pygame.image.load("CarOrange.png")
carOrange = pygame.transform.scale (carOrange,(50,30))

carPink = pygame.image.load("CarPink.png")
carPink = pygame.transform.scale (carPink,(50,30))

carGreen = pygame.image.load("CarGreen.png")
carGreen= pygame.transform.scale (carGreen,(50,30))

carYellow = pygame.image.load("CarYelloq.png")
carYellow = pygame.transform.scale (carYellow,(50,30))

carWhite = pygame.image.load("CarWhite1.png")
carWhite = pygame.transform.scale(carWhite,(50,30))
Car = []
Car.append (carBlue)
Car.append (carOrange)
Car.append (carPink)
Car.append (carGreen)
Car.append (carYellow)
Car.append (carWhite)
#Car position
CarXY_Blue = [start_line,210]
CarXY_Orange = [start_line,260]
CarXY_Pink = [start_line,310]
CarXY_Green = [start_line,360]
CarXY_Yellow = [start_line,410]
CarXY_White = [start_line,460]
CarXY = []
CarXY.append(CarXY_Blue)
CarXY.append(CarXY_Orange)
CarXY.append(CarXY_Pink)
CarXY.append(CarXY_Green)
CarXY.append(CarXY_Yellow)
CarXY.append(CarXY_White)
#buff array
buff = []
buff.append(clock_render) #0
buff.append(clover_render) #1
buff.append(fire_wheel_render) #2
buff.append(lucky_render) #3
buff.append(slow_motion_render) #4
buff.append(snail_render) #5
buff.append(snowflake_render) #6
buff.append(warning_render) #7
#dungyen
idungyen = []
idungyen.append(90)
idungyen.append(90)
idungyen.append(90)
idungyen.append(90)
idungyen.append(90)
#tangtoc
itangtoc = []
itangtoc.append(90)
itangtoc.append(90)
itangtoc.append(90)
itangtoc.append(90)
itangtoc.append(90)
#giamtoc
igiamtoc = []
igiamtoc.append(90)
igiamtoc.append(90)
igiamtoc.append(90)
igiamtoc.append(90)
igiamtoc.append(90)

#Draw Car
def draw_car():
    for i in range(5):
        GAMESCREEN.blit(Car[i],(CarXY[i][0],CarXY[i][1]))

def tangtoc(car,Buff,index): #1
    if (car[0]+car_width < Buff[0]):
        GAMESCREEN.blit(buff[2],(Buff[0],Buff[1]))
    if (car[0]+car_width >= Buff[0]) and (car[0]+car_width <= Buff[0]+Distance_Buff) and (car[1]==Buff[1]):
        car[0] += Speedbuff
        itangtoc[index] -=1
        if(itangtoc[index]==0):
            return 1 
    return 0 

def giamtoc(car,Buff,index): #2
    if (car[0]+car_width < Buff[0]):
        GAMESCREEN.blit(buff[5],(Buff[0],Buff[1]))
    if (car[0]+car_width >= Buff[0]) and (car[0]+car_width <= Buff[0]+Distance_Nerf)and (car[1]==Buff[1]):
        car[0] -= Speednerf
        igiamtoc[index]  = igiamtoc[index] - 1
        if(igiamtoc[index]==0):
          return 1
    return 0 

def dungyen(car,Buff,Time,Speed,index): #3
    if (car[0]+car_width < Buff[0]):
        GAMESCREEN.blit(buff[6],(Buff[0],Buff[1]))
    elif (car[0]+car_width >= Buff[0]) and (Time <= 3)and (car[1]==Buff[1]):
        idungyen[index] = idungyen[index] - 1
        car[0] -=Speed
        if(idungyen[index]==0):
            return 1
    return 0

def Vevachxuatphat(car,Buff,check): #4
    if (car[0]+car_width < Buff[0]) and check == 0:
        GAMESCREEN.blit(buff[7],(Buff[0],Buff[1]))
    if (car[0]+car_width >= Buff [0])and (car[1]>=Buff[1]) and check ==0:
        car[0]=start_line
        return 1 
    return 0 

def Vevachdich(car,Buff,check): #5
    if (car[0]+car_width < Buff[0]) and (check == 0):
        GAMESCREEN.blit(buff[3],(Buff[0],Buff[1]))
    if (car[0]+car_width >= Buff [0])and (car[1]==Buff[1])and (check == 0):
        check = 1
        car[0]=end_line
        return 1
    return 0




def Move(car,Buff,check,Time,chucnang,index):

    if (car[0]>=0)and(car[0]<950):
        speed = random.randint(2,3)
        car[0]+=speed
        if (chucnang == 0):
            ok = tangtoc(car,Buff,index)
            if(ok==0):
                return 0
            else :
                return -1
        if (chucnang == 1):
            ok = giamtoc(car,Buff,index)
            if(ok==0):
              return 1
            else:
              return -1
        if (chucnang == 2):
            ok = dungyen(car,Buff,Time,speed,index)
            if(ok==0):
                return 2
            else :
                return -1 
        if (chucnang == 3):
          ok = check = Vevachxuatphat(car,Buff,check)
          if(ok==0):
                return 3
          else :
                return -1 
        if (chucnang == 4):
            ok = Vevachdich(car,Buff,check)
            if(ok==0):
                return 3
            else :
                return -1 
    else :
        car[0]=950

def Gameloof():
    check= False
    check1=0
    Time =0


    bua1 = [random.randint(160,800),210]
    bua2 = [random.randint(160,800),260]
    bua3 = [random.randint(160,800),310]
    bua4 = [random.randint(160,800),360]
    bua5 = [random.randint(160,800),410]
    bua6 = [random.randint(160,800),460]


    cn1 = random.randint(0,4)
    cn2 = random.randint(0,4)
    cn3 = random.randint(0,4)
    cn4 = random.randint(0,4)
    cn5 = random.randint(0,4)
    cn6 = random.randint(0,4)



    while True:
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    check =True
        GAMESCREEN.fill(GRAY)
        GAMESCREEN.blit(race_track_render,(0,150))
        draw_car()

        if check :
            cn1 = Move(CarXY[0],bua1,check1,Time,cn1,0)
            cn2 = Move(CarXY[1],bua2,check1,Time,cn2,1)
            cn3 = Move(CarXY[2],bua3,check1,Time,cn3,2)
            cn4 = Move(CarXY[3],bua4,check1,Time,cn4,3)
            cn5 = Move(CarXY[4],bua5,check1,Time,cn5,4)
      #  Move(CarXY[5],bua6,check1,Time,cn4)

            pygame.display.flip()
            fpsClock.tick(FPS)
while True:
    GAMESCREEN.fill(GRAY)
    GAMESCREEN.blit(race_track_render,(0,150))
    draw_car()
    pygame.display.flip()
    Gameloof()
