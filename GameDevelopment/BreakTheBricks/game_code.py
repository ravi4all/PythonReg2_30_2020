import pygame
pygame.init()

width = 1045
height = 500
gameBoard = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

def game():
    barWidth = 200
    barHeight = 18
    barX = width // 2 - barWidth // 2
    barY = height - barHeight - 10
    moveX = 0

    ballRadius = 8
    ballX = barX + barWidth // 2
    ballY = barY - ballRadius

    brickWidth = 100
    brickHeight = 30
    bricksList = []
    nrow = 5
    ncol = width // brickWidth
    for i in range(nrow):
        for j in range(ncol):
            brick = pygame.Rect((brickWidth + 5) * j, (brickHeight + 5) * i,
                        brickWidth,brickHeight)
            bricksList.append(brick)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 1
                elif event.key == pygame.K_LEFT:
                    moveX = -1
            else:
                moveX = 0

        gameBoard.fill(white)
        pygame.draw.rect(gameBoard,red,[barX,barY,barWidth,barHeight])
        pygame.draw.circle(gameBoard,black,[ballX,ballY],ballRadius)

        for i in range(len(bricksList)):
            pygame.draw.rect(gameBoard,red,bricksList[i])

        barX += moveX

        if barX > width - 50:
            moveX = -1
        elif barX < 0:
            moveX = 1

        pygame.display.flip()

game()