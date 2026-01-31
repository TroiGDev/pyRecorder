import pygame

import math

import pyRecorder

pygame.init()
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Animation')

pyrecorder = pyRecorder.Recorder()

t = 0

running = True
while running:

    #fill screen
    screen.fill((20, 20, 20))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t += 1
    width = 40
    height = 80
    margin = 10

    fullwidth = 10 * width + margin * (10 - 1)
    initialx = (screenWidth - fullwidth) / 2

    for i in range(10):
        pos = (initialx + (width + margin) * i, screenHeight/2 - height/2 + 50 * math.sin(t * 0.05 + 1/2 *i))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos[0], pos[1], width, height), 2)

    pyrecorder.takeShot(screen, t)
    pygame.display.flip()

    #stop animation after 600 frames
    if t == 600:
        running = False

pyrecorder.compileToVideo(60)

pygame.quit()
