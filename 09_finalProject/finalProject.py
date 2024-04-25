# Final project, Darryl Mcnish, v0.0
import sys, random, pygame


resolution = 0 # 0 = Low resolution (800, 600), 1 = High resolution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

#pygame.int()

difficulty = int(input("please select a difficulty. Enter 1 foe Easy or 2 for HARD. \n"))

if difficulty == 1:
#    pygame.display.set_caption('NAME OF GAME -- EASY')
#else:
#    pygame.display.set_caption('NAME OF GAME -- HARD')
    
#screen = pygame.display.set_caption('NAME OF GAME -- EASY')
#screen = pygame.display.set_caption('NAME OF GAME -- HARD')

 screen = pygame.display.set_mode((x, y))
#CREATE AN if / else BLOCK TO SET RESOLUTION BASED ON THE VARIABLE ABOVE.


import pygame
import random

#initialize pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
Screen = pygame.display.set_mode((WIDTH, 
HEIGHT))
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
opponent_img = pygame.image.load('opponent_car.png')

#clock
clock = pygame.time.Clock()

# Car class
class car:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect
        self.image.get_rect()

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
    
# Main game loop
def game(difficulty):
 car = car(WIDTH // 2 - car_width // 2, HEIGHT - 100, car_img)
opponent_car = car(random.randint(100, WIDTH - opponent_width - 100), 0, opponent_img)

#ga
score = 0
speed = 5 if difficulty == "easy" else 8

running = True
while running:
     screen.fill(WHITE)

#event handling
for event in pygame.event.get():
     if event.type == pygame.QUIT:
          running = False

#move the players car
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and car.x > 100:
     car.x -= speed 
     if keys[pygame.K_RIGHT] and car.x < WIDTH - car_width - 100: car.x += speed

#move the opponent car
opponent_car.y += speed

#check collision
if car.rect.colliderect(opponent_car.rect):
     running = False

#if opponent car crosses the screen
if opponent_car.y > HEIGHT:
    opponent_car.y = 0
    opponent_car = random.randint(100, WIDTH - opponent_width - 100)
    score += 1

#draw cars
car.draw()
opponent_car.draw()

#display score
display_text(f"score: {score}", WIDTH // 2, 50, font_size=30)
pygame.display.update()
clock.tick(60)

#start game
difficulty = input("choose difficulty(easy/hard): ")
game(difficulty)
pygame.quit()