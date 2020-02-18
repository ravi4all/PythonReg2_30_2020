import pygame
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

gameBoard.fill(white)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(gameBoard,red,[0,0,50,50])
    pygame.draw.circle(gameBoard,red,[200,200],80)

    pygame.draw.line(gameBoard,red,(400,200),(400,400))

    pygame.display.flip()