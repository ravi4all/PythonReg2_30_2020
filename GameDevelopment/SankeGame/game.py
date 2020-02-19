import pygame
import random
pygame.init()

width = 1000
height = 500
gameBoard = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

frogImg = pygame.image.load("frog.png")
frogWidth = frogImg.get_width()
frogHeight = frogImg.get_height()

coinSound = pygame.mixer.Sound('point.wav')
bgSound = pygame.mixer.Sound('music_1.wav')
bgSound.play(-1)

gameBgImg = pygame.image.load("snake_bg.png")

def homeScreen():
    msg = "Press SPACE to Start Game"
    font = pygame.font.SysFont(None, 60)
    text = font.render(msg, True, red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        gameBoard.blit(gameBgImg,(0,0))
        gameBoard.blit(text,(100,450))
        pygame.display.flip()

def snake(snakeList,colorList):
    for i in range(len(snakeList)):
        pygame.draw.rect(gameBoard, colorList[i], [snakeList[i][0],snakeList[i][1], 50, 50])

def score(counter):
    font = pygame.font.SysFont(None,30)
    text = font.render("Score : {}".format(counter),True,red)
    gameBoard.blit(text,(10,10))

def main():
    x = 0
    y = 0
    moveX = 0
    moveY = 0
    snakeLength = 1
    snakeList = []
    colorList = []

    frogX = random.randint(0, width - frogWidth)
    frogY = random.randint(0, height - frogHeight)

    FPS = 200
    clock = pygame.time.Clock()
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 3
                    moveY = 0
                elif event.key == pygame.K_LEFT:
                    moveX = -3
                    moveY = 0
                elif event.key == pygame.K_UP:
                    moveY = -3
                    moveX = 0
                elif event.key == pygame.K_DOWN:
                    moveY = 3
                    moveX = 0

        gameBoard.fill(white)
        gameBoard.blit(frogImg,(frogX,frogY))
        snakeRect = pygame.draw.rect(gameBoard,red,[x,y,50,50])
        frogRect = pygame.Rect(frogX,frogY,frogWidth,frogHeight)
        x += moveX
        y += moveY

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)

        snakeList.append(snakeHead)
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        colorList.append(color)

        if len(snakeList) > snakeLength:
            del snakeList[0]
            del colorList[0]

        snake(snakeList,colorList)
        score(counter)

        if frogRect.colliderect(snakeRect):
            frogX = random.randint(0, width - frogWidth)
            frogY = random.randint(0, height - frogHeight)
            snakeLength += 20
            FPS += 10
            counter += 1
            coinSound.play()

        if x > width:
            x = -50
        elif x < -50:
            x = width

        if y > height:
            y = -50
        elif y < -50:
            y = height

        pygame.display.flip()
        clock.tick(FPS)

homeScreen()