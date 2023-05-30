import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed =1

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Move the dot")
screen.fill((60, 220, 0))
pygame.display.update()


dot = pygame.image.load("dot.png")
dot_loc = dot.get_rect()
dot_loc.center = right_lane, height*0.8

stick = pygame.image.load("stick.png")
stick_loc = stick.get_rect()
stick_loc.center = left_lane, height*0.2

counter = 0
while running:
    counter += 1
    
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up",speed)
    
    stick_loc[1] += speed
    if stick_loc[1] > height:
        if random.randint(0,1) == 0:
            stick_loc.center = right_lane, -200
        else:
            stick_loc.center = left_lane, -200

    if dot_loc[0] == stick_loc[0] and stick_loc[1] > dot_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                dot_loc = dot_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                dot_loc = dot_loc.move([int(road_w/2), 0])

    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height))

    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
 
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    screen.blit(dot, dot_loc)
    screen.blit(stick, stick_loc)
    # apply changes
    pygame.display.update()


pygame.quit()