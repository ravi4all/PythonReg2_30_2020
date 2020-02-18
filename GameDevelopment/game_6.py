import pygame
import random
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

img = pygame.image.load("football.png")

x = 0
y = 0
moveX = random.randint(1,5)
moveY = random.randint(1,5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameBoard.fill(white)

    gameBoard.blit(img,(x,y))

    x += moveX
    y += moveY

    if x > width - 100:
        moveX = -random.randint(1,5)
    elif x < 0:
        moveX = random.randint(1,5)

    if y > height - 100:
        moveY = -random.randint(1,5)
    elif y < 0:
        moveY = random.randint(1,5)

    pygame.display.flip()