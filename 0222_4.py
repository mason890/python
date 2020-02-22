import pygame, sys
from pygame import *
import random

pygame.init()
SURFACE = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()

SIZE = 30
WIDTH = 20
HEIGHT = 20
food_list = []
snake_list = []

def add_food() :
    # x = random.randint(0,WIDTH-1)
    # y = random.randint(0,HEIGHT-1)
    # food_list.append((x,y))
    
    while True:
        pos = random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)
        if pos in food_list or pos in snake_list:
            continue
        food_list.append(pos)
        break

def move_food(pos) :
    idx = food_list.index(pos)
    del food_list[idx]
    add_food()

def paint(meg) :
    SURFACE.fill((0,0,0))
    
    for i in range(20) :
        pygame.draw.line(SURFACE, (64,64,64), (0,i*SIZE), (600,i*SIZE))
    for j in range(20) :
        pygame.draw.line(SURFACE, (64,64,64), (j*SIZE,0), (j*SIZE,600))
    
    for pos in food_list :
        pygame.draw.ellipse(SURFACE, (0,255,0), Rect(pos[0]*SIZE, pos[1]*SIZE, SIZE, SIZE))
    
    for pos in snake_list :
        pygame.draw.rect(SURFACE, (255,0,0), Rect(pos[0]*SIZE, pos[1]*SIZE,SIZE,SIZE))
    
    if meg != None :        
        SURFACE.blit(meg,(20,200))
    
    pygame.display.update()

for _ in range(10) :
    add_food()

snake_list.append((int(WIDTH/2),int(HEIGHT/2)))

key = K_DOWN
game_over = False
message = None

while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        
        elif event.type == KEYDOWN :
            key = event.key
    
    if not game_over :
        if key == K_LEFT :
            head = (snake_list[0][0]-1, snake_list[0][1])
        elif key == K_RIGHT :
            head = (snake_list[0][0]+1, snake_list[0][1])
        elif key == K_UP :
            head = (snake_list[0][0],snake_list[0][1]-1)
        elif key == K_DOWN :
            head = (snake_list[0][0],snake_list[0][1]+1)
        
        #게임종료 상황 체크
        if head in snake_list or \
            head[0] < 0 or head[0] > HEIGHT or \
            head[1] < 0 or head[1] > WIDTH :
            game_over = True
            fontObj = pygame.font.Font("freesansbold.ttf", 80)
            message = fontObj.render('GAME OVER!!!',True,(0,255,0),(0,0,255))
        else :
            snake_list.insert(0,head)
            if head in food_list :
                move_food(head)
            else :
                snake_list.pop()
    paint(message)
    FPSCLOCK.tick(4)