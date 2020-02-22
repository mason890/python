#pygame

import pygame,sys
from pygame.locals import *
pygame.init()
SURFACE = pygame.display.set_mode((800,700))
FPSCLOCK = pygame.time.Clock()
# SURFACE.fill((255,255,255))
# while True :
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT :
#             pygame.quit()
#             sys.exit()
#     pygame.draw.circle(SURFACE,(255,0,0),(50,50),20)
#     pygame.draw.circle(SURFACE,(255,0,0),(150,50),20,10)
#     pygame.draw.circle(SURFACE,(0,255,0),(50,150),10)
#     pygame.draw.circle(SURFACE,(0,255,0),(250,150),20)
#     pygame.display.update()
#-------------------------------------------------------------------
# key_status = ""
# key = None
# SURFACE.fill((255,255,255))
# while True :
#     for event in pygame.event.get() :
#         if event.type == pygame.QUIT :
#             pygame.quit(); sys.exit()
#         elif event.type == pygame.KEYDOWN :
#             key_status = "key Down"
#             key = event.key
#         elif event.type == pygame.KEYUP :
#             key_status = "key Up"
#             key = event.key
#     if key :
#         pygame.display.set_caption(pygame.key.name(key) + " " + key_status)
#     pygame.display.update()
#     FPSCLOCK.tick(60)
#-------------------------------------------------------------------
# 
fontObj = pygame.font.Font("freesansbold.ttf",32)
textSurfaceObj = fontObj.render('Hello World!',True,(0,255,0),(0,0,255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)
while True :
    SURFACE.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
    SURFACE.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
#-----------------------------------------------------------------

# def main() :
#     my_image = pygame.image.load('C:/Users/GREEN/Desktop/Mason/up.png')
#     while True :
#         for event in pygame.event.get() :
#             if event.type == pygame.QUIT :
#                 pygame.quit()
#                 sys.exit()
#         SURFACE.fill((255,255,255))
#         SURFACE.blit(my_image, (20,50))
        
#         pygame.display.update()
#         FPSCLOCK.tick(30)
# if __name__ == '__main__' :
#     main()
