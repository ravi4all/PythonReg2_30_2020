import pygame
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameBoard.fill(white)
    pygame.draw.rect(gameBoard,red,[x,y,50,50])
    x += 1
    y += 1

    pygame.display.flip()