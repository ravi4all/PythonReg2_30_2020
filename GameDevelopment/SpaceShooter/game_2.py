import pygame
import random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

myShip = pygame.image.load("images/ship_1.png")
myShipWidth = myShip.get_width()
myShipHeight = myShip.get_height()

enemyShip = pygame.image.load("images/enemy_2.png")
enemyShipWidth = enemyShip.get_width()
enemyShipHeight = enemyShip.get_height()

def enemy(enemyShipList,enemyBullets,moveEnemyY,moveEnemyBullet,enemyBulletWidth, enemyBulletHeight):
    for i in range(len(enemyShipList)):
        screen.blit(enemyShip, (enemyShipList[i][0], enemyShipList[i][1]))
        enemyShipList[i][1] += moveEnemyY

        pygame.draw.rect(screen, red, [enemyBullets[i][0], enemyBullets[i][1], enemyBulletWidth, enemyBulletHeight])
        enemyBullets[i][1] += moveEnemyBullet

        if enemyShipList[i][1] > height:
            enemyShipList[i][0] = random.randint(0, width - enemyShipWidth)
            enemyShipList[i][1] = random.randint(-height, -enemyShipHeight)
            enemyBullets[i][0] = enemyShipList[i][0] + enemyShipWidth / 2
            enemyBullets[i][1] = -enemyShipHeight

def main():
    myShipX = width // 2 - myShipWidth // 2
    myShipY = height - myShipHeight
    moveShipX = 0

    enemyShipList = []
    row = 2
    col = width // enemyShipWidth

    enemyBullets = []
    moveEnemyBullet = 2
    enemyBulletWidth = 6
    enemyBulletHeight = 12
    for i in range(5):
        enemyShipX = random.randint(0,width - enemyShipWidth)
        enemyShipY = random.randint(-height,-enemyShipHeight)
        enemyShipList.append([enemyShipX,enemyShipY])
        enemyBulletX = enemyShipX + enemyShipWidth/2
        enemyBulletY = -enemyShipHeight
        enemyBullets.append([enemyBulletX,enemyBulletY])

    enemyShipRectList = []
    for i in range(len(enemyShipList)):
        enemyShipRectList.append(pygame.Rect(enemyShipList[i][0],enemyShipList[i][1],enemyShipWidth,enemyShipHeight))
    moveEnemyY = 1

    shoot = False

    bulletWidth = 8
    bulletHeight = 14
    bulletY = myShipY
    moveBullet = 0
    while True:
        if not shoot:
            bulletX = myShipX + myShipWidth / 2 - bulletWidth/2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveShipX = 3
                elif event.key == pygame.K_LEFT:
                    moveShipX = -3
                elif event.key == pygame.K_SPACE:
                    moveBullet = -3
                    shoot = True
            elif event.type == pygame.KEYUP:
                moveShipX = 0

        screen.fill(white)

        bulletRect = pygame.draw.rect(screen, red, [bulletX, bulletY, bulletWidth, bulletHeight])

        screen.blit(myShip,(myShipX,myShipY))

        enemy(enemyShipList,enemyBullets,moveEnemyY,moveEnemyBullet,enemyBulletWidth, enemyBulletHeight)

        myShipX += moveShipX
        bulletY += moveBullet

        for i in range(len(enemyShipRectList)):
            if enemyShipRectList[i].colliderect(bulletRect):
                del enemyShipRectList[i]
                del enemyShipList[i]
                moveBullet = 0
                bulletY = myShipY
                bulletX = myShipX + myShipWidth / 2 - bulletWidth / 2
                shoot = False
                break

        if bulletY < 0:
            moveBullet = 0
            bulletY = myShipY
            bulletX = myShipX + myShipWidth / 2 - bulletWidth / 2
            shoot = False

        pygame.display.flip()

main()