# Final project, Darryl Mcnish, v0.0
#import sys, random, pygame


#resolution = 0 # 0 = Low resolution (800, 600), 1 = High resolution (1920, 1080)

#if resolution == 0:
#    x = 800
#    y = 600
#else:
#    x = 1920
#    y = 1080

#pygame.int()

#difficulty = int(input("please select a difficulty. Enter 1 foe Easy or 2 for HARD. \n"))

#if difficulty == 1:
#    pygame.display.set_caption('NAME OF GAME -- EASY')
#else:
#    pygame.display.set_caption('NAME OF GAME -- HARD')
    
#screen = pygame.display.set_caption('NAME OF GAME -- EASY')
#screen = pygame.display.set_caption('NAME OF GAME -- HARD')

#screen = pygame.display.set_mode((x, y))
#CREATE AN if / else BLOCK TO SET RESOLUTION BASED ON THE VARIABLE ABOVE.



import pygame
from pygame.locals import *
import random

pygame.init()

#create the window
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

#colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

#game settings
gameover = False
speed = 2
score = 0

#markers size
marker_width = 10
marker_height = 50

#road and edge markers
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

#game loop
clock = pygame.time.Clock()
fps = 120
running = True
while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()

    #draw the grass
    screen.fill(green)

    #draw the road
    pygame.draw.rect(screen, gray, road)

    #draw the edge markers
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    pygame.display.update()

pygame.quit()