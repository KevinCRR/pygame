import pygame
from pygame.locals import *


pygame.init()

pygame.display.set_caption('Tic-Tac-Toe')

run = True


win = pygame.display.set_mode((550, 550))

first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))
second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))
third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))

fourth = pygame.draw.rect(win, (255,255,255), (25, 200,150,150))
fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))
six = pygame.draw.rect(win, (255,255,255), (375,200,150,150))

seven = pygame.draw.rect(win, (255,255,255), (25, 375,150,150))
eigh = pygame.draw.rect(win, (255,255,255), (200,375,150,150))
nine = pygame.draw.rect(win, (255,255,255), (375,375,150,150))

player = 1
firstO = True
secondO = True
thirdO = True

forthO = True
fifO = True
sixO = True

sevO = True
eighO = True
nineO = True

while run:
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player = 1
                firstO = True
                secondO = True
                thirdO = True

                forthO = True
                fifO = True
                sixO = True

                sevO = True
                eighO = True
                nineO = True
                first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))
                second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))
                third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))

                fourth = pygame.draw.rect(win, (255,255,255), (25, 200,150,150))
                fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))
                six = pygame.draw.rect(win, (255,255,255), (375,200,150,150))

                seven = pygame.draw.rect(win, (255,255,255), (25, 375,150,150))
                eigh = pygame.draw.rect(win, (255,255,255), (200,375,150,150))
                nine = pygame.draw.rect(win, (255,255,255), (375,375,150,150))

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            
            if first.collidepoint(pos) and firstO:
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (50, 50, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (100,100), 50) 
                    player = 1
                firstO = False
                    
            if second.collidepoint(pos) and secondO:
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (225, 50, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (275,100), 50)
                    player = 1
                secondO = False
                    
            if third.collidepoint(pos) and thirdO:
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (400, 50, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (450,100), 50)
                    player = 1
                thirdO = False
                
                
            if fourth.collidepoint(pos) and forthO :
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (50, 225, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (100,275), 50) 
                    player = 1
                forthO = False
                    
            if fifth.collidepoint(pos) and fifO:
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (225, 225, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (275,275), 50)
                    player = 1
                fifO = False
                
            if six.collidepoint(pos) and sixO:
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (400, 225, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (450,275), 50)
                    player = 1
                sixO = False
                
                
            
            if seven.collidepoint(pos) and sevO:
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (50, 400, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (100,450), 50)
                    player = 1 
                sevO = False
                    
            if eigh.collidepoint(pos) and eighO:
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (225, 400, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (275,450), 50)
                    player = 1
                eighO = False
                    
            if nine.collidepoint(pos) and nineO:
                if player == 1:
                    pygame.draw.rect(win, (255, 0, 0), (400, 400, 100, 100))
                    player = 2
                else:
                    pygame.draw.circle(win, (0,255,0), (450,450), 50)
                    player = 1
                nineO = False
                
    pygame.display.update()
pygame.quit()