import pygame
import sys

pygame.init()

#screen dimensions
WIDTH, HEIGHT = 500, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game start screen")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#FONTS
FONT = pygame.font.Font(None, 36)

def start_screen():
    SCREEN.fill(WHITE)

#title
title_text = FONT.render("welcome to my game", True, WHITE)
title_rect = title_text.get_rect(center=(WIDTH/2,HEIGHT/4))
SCREEN.blit(title_text, title_rect)


#start button
start_text = FONT.render("Start Game", True, BLACK)
start_rect = start_text.get_rect(center=(WIDTH/2,HEIGHT/2))
pygame.draw.rect(SCREEN, (200, 200, 200), start_rect, border_radius = 10)
SCREEN.blit(start_text, start_rect)

pygame.display.flip()

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(mouse_pos):
                print("game started!")
                running = False

import pygame
from pygame.locals import *
import random

pygame.init()

#create the window
width = 500
height = 750
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

#x coordinates of lanes
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

#for animating movement of lane markers
lane_marker_move_y = 0

class Vehicle(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        #scale image down to fit
        image_scale = 100 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class PlayerVehicle(Vehicle):

    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)

#player start coordinates
player_x = 250
player_y = 400

#create the players car
player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

#loop the other vehicle images
image_filenames = ['police.png', 'police.png', 'police.png']
vehicle_images = []
for image_filename in image_filenames :
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)

#sprite group for vehicles
vehicle_group = pygame.sprite.Group()

#load the crash image
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

#game loop
clock = pygame.time.Clock()
fps = 120
running = True
while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        #move the players car with arrows
        if event.type == KEYDOWN:

            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
            elif event.key == K_UP:
                speed += 1
            elif event.key == K_DOWN:
                speed -= 1
            
            #check if theres a side swipe collision after changing lanes
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):

                    gameover = True

                    #place the players carnext to other vehicle
                    #and determine where to position the crash image
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect[1] + vehicle.rect.center[1]) / 2]

    #draw the grass
    screen.fill(green)

    #draw the road
    pygame.draw.rect(screen, gray, road)

    #draw the edge markers
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    #draw lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    #draw players car
    player_group.draw(screen)

    #add up to two vehicles
    if len(vehicle_group) < 2:
        
        #ensure enough gap between vehicles
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        
        if add_vehicle:

            #select a random lane
            lane  = random.choice(lanes)

            #select a random vehicle image
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)

    #make vehicles move
    for vehicle in vehicle_group:
        vehicle.rect.y += speed

        #remove the vehicle one it goes off screen
        if vehicle.rect.top >= height:
            vehicle.kill()

            #add to score
            score += 1

            #speed up the game after passing 5 vehicles
            if score > 0 and score % 5 == 0:
                speed +=1

    #draw the vehicles
    vehicle_group.draw(screen)

    #display the score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 450)
    screen.blit(text, text_rect)

    #check if theres a head on collision
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]

    #display game over
    if gameover:
        screen.blit(crash, crash_rect)

        pygame.draw.rect(screen, red, (0, 50, width, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('game over. play again? (enter 1 or 2)', True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect)


    pygame.display.update()

    #check if player wants to play again
    while gameover:
        
        clock.tick(fps)

        for event in pygame.event.get():

            if event.type == QUIT:
                gameover = False
                running = False

            #get the players input (y or n)
            if event.type == KEYDOWN:
                if event.key == K_1:
                        gameover = False
                        speed = 2
                        score = 0
                        vehicle_group.empty()
                        player.rect.center = [player_x, player_y]
                elif event.key == K_2:
                        gameover = True
                        running = False



pygame.quit()