import pygame
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,155,100

gameBoard.fill(red)
pygame.display.flip()


