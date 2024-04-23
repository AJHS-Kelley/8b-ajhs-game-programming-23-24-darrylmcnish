# Final project, Darryl Mcnish, v0.0
import sys, random, pygame
from typing import Self

resolution = 0 # 0 = Low resolution (800, 600), 1 = High resolution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.int()

difficulty = int(input("please select a difficulty. Enter 1 foe Easy or 2 for HARD. \n"))

if difficulty == 1:
    pygame.display.set_caption('NAME OF GAME -- EASY')
else:
    pygame.display.set_caption('NAME OF GAME -- HARD')
    
screen = pygame.display.set_caption('NAME OF GAME -- EASY')
screen = pygame.display.set_caption('NAME OF GAME -- HARD')

screen = pygame.display.set_mode((x, y))
#CREATE AN if / else BLOCK TO SET RESOLUTION BASED ON THE VARIABLE ABOVE.

import pygame
import random

#initialize pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#CAR
car_width = 60
cra_height = 80
car_img = pygame.image.load('car.png')

#OPPONENT CAR
opponent_width = 60
opponent_height = 80
car_img = pygame.image.load('opponent_car.png')

#clock
clock = pygame.time.Clock()

# Car class
class car:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect
Self.image.get_rect()

def draw(self):
        screen.blit(self.image,
(self.x, self.y))

#function to display text on screen
def display_text(text, x, y,
color=BLACK, font_size=30):
    font = pygame.font.FONT(None,
font_size)
    text_surface = font.render(text,
True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface,
text_rect)
    
