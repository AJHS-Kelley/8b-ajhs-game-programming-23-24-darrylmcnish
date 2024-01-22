# Number Slider, by darryl mcnish, based ona project AI sweigart, v0.0

import sys, random, pygame
# sys module provides access to system to resources (i.e. Operating system commands)

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of module.function()
# Example: we can use draw() instead of pygame.draw()

# constants for game board
BOARDWIDTH = 4 # COLUMNS
BOARDHIGHT = 4 # ROWS
TILESIZE = 80 # WHAT UNIT DO YOU THINK THIS IS?
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHIGHT = 480 # MEASURED IN PIXELS
FPS = 30
BLANK = None

# COLOR VALUES in (R, G, B) format.
# 0 = No value, 255 = Max Value
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = ( 0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# BOARD DESIGN SETUP
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20 # pixels

# BUTTON SETUP
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

