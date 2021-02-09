import random
import numpy as np
import pandas as pd
import sys
import pygame
#GAME OF LIFE
#If a living cell has fewer than 2 or greater than 3 neighbours, it dies
#If an empty cell has 3 neighbours exactly, it becomes living
print("Running")
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Game of Life')
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
w = 10
Wide = int(WIDTH/w)
Height = int(HEIGHT/w)
Game = np.zeros((Height,Wide))
# Game = np.random.randint(0,2, size=(Height,Wide))
# print(np.sum(Game))

def Neighbours(Game):
    Game1 = Game.copy()
    k = 0
    for a in range(Height):
        for b in range(Wide):
            for c in range(-1, 2):
                for d in range(-1,2):
                    if (a+c>=0 and b+d>=0) and (a+c<Height and b+d<Wide) and (c!=0 or d!=0):
                        if Game[a+c][b+d] == 1:
                            k = k + 1
            Game1[a,b]=k
            k=0
    return Game1
def LifeorDeath(Game, Game1):
    for a in range(Height):
        for b in range(Wide):
            for c in range(-1, 2):
                for d in range(-1,2):
                    if (a + c >= 0 and b+d >= 0) and (a + c < Height and b + d < Wide):
                        if Game[a][b] ==0:
                            if Game1[a][b]==3:
                                Game[a][b]=1
                        elif Game[a][b]==1:
                            if Game1[a][b]!=2 and Game1[a][b]!=3:
                                Game[a][b] = 0
    return Game

def Plot(Game,C):
    Game[C[0]][C[1]] = 1
    pygame.draw.rect(screen, (0, 0, 200), (C[0] * w, C[1] * w, w, w))
    pygame.display.update()
    return Game

def Draw_Game(Game):
    screen.fill((255, 255, 255))
    for a in range(Height):
        for b in range(Wide):
            if Game[a][b]==1:
                pygame.draw.rect(screen,(0,0,200),(a*w,b*w,w,w))
    pygame.display.update()

screen.fill((255, 255, 255))
pygame.display.update()
Iterations = 1000
k = 0
stop = True
while k < Iterations:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(np.sum(Game))
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            C = np.array(pygame.mouse.get_pos())
            C = [int(C[0]//w),int(C[1]//w)]
            if C[0] > int(WIDTH/w) or C[0] < 0 or C[1] > int(HEIGHT/w) or C[1] < 0:
                continue
            Game = Plot(Game, C)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if stop:
                    stop = False
                    # print(np.sum(Game))
                elif not stop:
                    stop = True
    if not stop:
        k += 1
        N = Neighbours(Game)
        Game = LifeorDeath(Game, N)
        Draw_Game(Game)
        pygame.display.update()
        clock.tick(10)
print(np.sum(Game))