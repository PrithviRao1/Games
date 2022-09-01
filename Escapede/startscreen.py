import pygame
import time
from menu import character_selected
startime = time.perf_counter()
pygame.init()
screen = pygame.display.set_mode((800,600))
#countdown sequence
num1 = pygame.image.load('pics/1.png')
num2 = pygame.image.load('pics/2.png')
num3 = pygame.image.load('pics/3.png')
SS = pygame.image.load('pics/Startscreen.png')


xcor3 = -100
while time.perf_counter()-startime < 0.75:
    screen.blit(SS,(0,0))
    screen.blit(num3,(xcor3,220))
    if xcor3 < 250:
        xcor3 += 15
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

ycor2 = 600
while time.perf_counter()-startime < 1.5:
    screen.blit(SS, (0, 0))
    screen.blit(num2,(250,ycor2))
    if ycor2 > 220:
        ycor2 -= 15
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

xcor1 = 600
while time.perf_counter()-startime < 2.25:
    screen.blit(SS, (0, 0))
    screen.blit(num1,(xcor1,220))
    if xcor1 > 250:
        xcor1 -= 15
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            break
pygame.quit()
import Yee