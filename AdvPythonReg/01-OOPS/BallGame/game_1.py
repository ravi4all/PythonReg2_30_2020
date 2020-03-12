import pygame
import random
pygame.init()

width = 1100
height = 550

screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0

ballX = 0
ballY = 0
moveX = 1
moveY = 1
radius = 50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.circle(screen,red,(ballX,ballY),radius)

    ballX += moveX
    ballY += moveY

    if ballX > width - radius:
        moveX = -1
    elif ballX < radius:
        moveX = 1
    elif ballY > height - radius:
        moveY = -1
    elif ballY < radius:
        moveY = 1

    pygame.display.flip()