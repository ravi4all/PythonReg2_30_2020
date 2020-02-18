import pygame
import random
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

x = 0
y = 0
moveX = 5
moveY = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameBoard.fill(white)
    color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    pygame.draw.circle(gameBoard,color,[x,y],50)
    x += moveX
    y += moveY

    if x > width - 50:
        moveX = -1
    elif x < 50:
        moveX = 1

    if y > height - 50:
        moveY = -1
    elif y < 50:
        moveY = 1

    pygame.display.flip()