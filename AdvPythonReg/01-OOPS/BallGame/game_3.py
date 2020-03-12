import pygame
import random
pygame.init()

width = 1100
height = 550

screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.moveX = random.randint(1,4)
        self.moveY = random.randint(1,4)
        self.radius = 40
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - self.radius:
            self.moveX = -random.randint(1,4)
        elif self.x < self.radius:
            self.moveX = random.randint(1,4)
        elif self.y > height - self.radius:
            self.moveY = -random.randint(1,4)
        elif self.y < self.radius:
            self.moveY = random.randint(1,4)

num = 5
ballsList = []
for i in range(num):
    ball = Ball()
    ballsList.append(ball)

FPS = 100
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    for i in range(len(ballsList)):
        pygame.draw.circle(screen,ballsList[i].color,[ballsList[i].x,ballsList[i].y],ballsList[i].radius)
        ballsList[i].update()

    pygame.display.flip()
    clock.tick(FPS)