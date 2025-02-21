import pygame
import sys
import os
import math
import numpy as np
import random

#recorder
from pyRecorder import Recorder
recorder = Recorder("gameoflife")

#------------------------------------------------------------------------------------------------------------------------------------
#world setup
wolrdWidth = 250
worldHeight = 150
drawnCellSize = 3
#------------------------------------------------------------------------------------------------------------------------------------

pygame.init()
screenWidth = wolrdWidth * drawnCellSize
screenHeight = worldHeight * drawnCellSize
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Conways Game of Life')

#remove window icon
transparent_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
transparent_surface.fill((0, 0, 0, 0))
pygame.display.set_icon(transparent_surface)

#------------------------------------------------------------------------------------------------------
def drawWorld():
    #draw squares where there is a 1 in the world array
    for x in range(len(world)):
        for y in range(len(world[x])):
            #draw square with correct scaling size
            pygame.draw.rect(screen, (0, world[x][y], 0), (x * drawnCellSize, y * drawnCellSize, drawnCellSize, drawnCellSize))

            """if world[x][y] > 255/2:
                pygame.draw.rect(screen, (0, world[x][y], 0), (x * drawnCellSize, y * drawnCellSize, drawnCellSize, drawnCellSize))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x * drawnCellSize, y * drawnCellSize, drawnCellSize, drawnCellSize))"""

def updateWorld(world):
    #create next world array
    nextWorld = [[0 for _ in range(worldHeight)] for _ in range(wolrdWidth)]

    #go through each cell and check for rules
    for x in range(len(world)):
        for y in range(len(world[x])):

            #get neighbouring cell count
            neighbours = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
            nStrength = 0
            for n in neighbours:
                nX = (x + n[0]) % wolrdWidth
                nY = (y + n[1]) % worldHeight
    
                nStrength += world[nX][nY]

            #get avarage strength of the neighbour cells
            avStrenght = nStrength/8 

            #-------------------------------------------------------RULES
            if world[x][y] > 60:
                if avStrenght < 60:
                    nextWorld[x][y] = world[x][y] * 0.7
                if avStrenght > 60 and avStrenght < 100:
                    nextWorld[x][y] = world[x][y] * 1.16
                if avStrenght > 100:
                    nextWorld[x][y] = world[x][y] * 0.7
            else:
                if avStrenght > 60 and avStrenght < 80:
                    nextWorld[x][y] = avStrenght * 1.1
            #-------------------------------------------------------RULES

            #clamp to 0 and 255
            if nextWorld[x][y] > 255:
                nextWorld[x][y] = 255
            if nextWorld[x][y] < 0:
                nextWorld[x][y] = 0

    #update the world by overriding it with the next world
    world = nextWorld
    return world

#------------------------------------------------------------------------------------------------------

#initialize 2d arrrays
world = [[0 for _ in range(worldHeight)] for _ in range(wolrdWidth)]

#randomly gemnerate world
for i in range(wolrdWidth):
    for j in range(worldHeight):
        world[i][j] = random.random() * 255

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen
    screen.fill((0, 0, 0))
    
    #update world
    world = updateWorld(world)

    #draw world
    drawWorld()

    # Update the display
    pygame.display.flip()

    #after rendered frame, take recorder shot
    recorder.takeShot(screen)

#get video from taken shots
recorder.getVideo("GOL_Plants.avi", 24)

# Quit Pygame
pygame.quit()
