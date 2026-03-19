import pygame
from random import *
from time import sleep

pygame.init()

HEIGHT = 700
WIDTH = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
background = pygame.image.load('Egg Catcher/assets/background.jpg')

bowl = pygame.image.load('Egg Catcher/assets/bowl.png')
bowl = pygame.transform.scale(bowl, (200,100))
bowl_rect = bowl.get_rect(midtop=(500, 600))

font = pygame.font.Font("flappy bird/font/Pixeltype.ttf", 50)
points = 0 
lives = 3

game_over = font.render(f"game over\n{points}", False, "white").convert()

egg = pygame.image.load('Egg Catcher/assets/egg.png')
eggs = [
    pygame.transform.scale(egg, (100,100)),
    pygame.transform.scale(egg, (100,100)),
    pygame.transform.scale(egg, (100,100)),
    # pygame.transform.scale(egg, (100,100)),
    # pygame.transform.scale(egg, (100,100))
]
# egg1 = pygame.transform.scale(egg, (100,100))
eggs_rect = [
    eggs[0].get_rect(midbottom=(randint(0,1000), randint(-100,0))),
    eggs[1].get_rect(midbottom=(randint(0,1000), randint(-200,-150))),
    eggs[2].get_rect(midbottom=(randint(0,1000), randint(-300,-250))),
    # eggs[3].get_rect(midbottom=(randint(0,1000), randint(-400,-350))),
    # eggs[4].get_rect(midbottom=(randint(0,1000), randint(-500,-450)))
]
# egg_rect = egg.get_rect(midbottom=(randint(0,1000), 0))
gravity = [
    0.2,
    0.2,
    0.1,
    # 0.2,
    # 0.05
]

d =  randint(1,3)

run = True
while run:
    screen.blit(background, (0,0))
    def func():
        for i in range(len(eggs)):
            if pygame.time.get_ticks() > d:
                screen.blit(eggs[i], eggs_rect[i])
            else:
                func()

    func()


    score = font.render(f"Score: {points}", False, "black").convert()
    screen.blit(score, (25,50))
    life = font.render(f"Lives: {lives}", False, "white").convert()
    screen.blit(life, (800,50))
    screen.blit(bowl, bowl_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        bowl_rect.x -= 10
    if keys[pygame.K_d]:
        bowl_rect.x += 10
    if keys[pygame.K_RIGHT]:
        bowl_rect.x += 10
    if keys[pygame.K_LEFT]:
        bowl_rect.x -= 10

    if bowl_rect.x <= -150:
        bowl_rect.x = 1020

    if bowl_rect.x >= 1150:
        bowl_rect.x = -50

    for i in range(len(eggs)):
        if bowl_rect.colliderect(eggs_rect[i]):
            eggs_rect[i] = eggs[i].get_rect(midbottom=(randint(0,1000), randint(-100,0)))
            points += 1
            gravity[i] = 0.2
            
    for i in range(len(eggs)):
        if eggs_rect[i].y >= 1050:
            eggs_rect[i] = eggs[i].get_rect(midbottom=(randint(0,1000), randint(-100,0)))
            gravity[i] = 0.2
            lives -= 1

    if lives == 0:
        screen.blit(game_over, (WIDTH/2, HEIGHT/2))
        for i in range(100):
            print('')
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(60)
    for i in range(len(eggs)):
        eggs_rect[i].y += gravity[i]
    if points == 0:
        for i in range(len(eggs)):
            gravity[i] += 0.01
    else:
        for i in range(len(eggs)):
            gravity[i] += (points/500)

pygame.quit()