# https://pythonprogramming.net/drawing-objects-pygame-tutorial/

import pygame
import random

pygame.init()

global_time_elapsed = 0

display_width = 800
display_height = 600

window = pygame.display.set_mode((display_width,display_height))

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 150, 0)
grey = (70,70,70)
grey2 = (60,60,60)
grey3 = (50,50,50)
grey4 = (100,100,100)
darkgrey = (50,50,50)

# -----------------------------------------------------------

def draw1(x,y, height, width):
    """Draws the obastcles

    Args:
        x (int): x coordinate
        y (int): x coordinate
        height (int): height of window
        width (int): width of window
    """    

    pygame.draw.circle(window, grey2, (x+height/2,y+width/2), width/2)
    pygame.draw.circle(window, grey, (x+height/2+10,y+width/2+10), width/2+5)
    pygame.draw.circle(window, grey, (x+height/2+10,y+width/2-7), width/2-3)
    pygame.draw.circle(window, darkgrey, (x+height/2+30,y+width/2), width/6)
    pygame.draw.circle(window, darkgrey, (x+height/2-17,y+width/2+15), width/9)
    pygame.draw.circle(window, darkgrey, (x+height/2-10,y+width/2+26), width/9)
    pygame.draw.circle(window, grey3, (x,y+width), width/9)
    pygame.draw.circle(window, grey2, (x+width,y+width +20), width/12)

# -----------------------------------------------------------

def draw2(x,y, height, width):
    """Draws a different obastcles

    Args:
        x (int): x coordinate
        y (int): x coordinate
        height (int): height of window
        width (int): width of window
    """      

    pygame.draw.circle(window, grey2, (x+height/2,y+width/2), width/2)
    pygame.draw.circle(window, grey, (x+height/2+10,y+width/2+15), width/2+5)
    pygame.draw.circle(window, grey, (x+height/2+15,y+width/2-7), width/2-3)
    pygame.draw.circle(window, darkgrey, (x+height/2+30,y+width/2), width/6)
    pygame.draw.circle(window, darkgrey, (x+height/2-17,y+width/2+15), width/9)
    pygame.draw.circle(window, darkgrey, (x+height/2-10,y+width/2+36), width/9)
    pygame.draw.circle(window, darkgrey, (x+height/2-10,y+width/2+26), width/9)
    pygame.draw.circle(window, grey3, (x,y+width), width/9)
    pygame.draw.circle(window, grey2, (x+width,y+width +30), width/12)
    pygame.draw.circle(window, grey3, (x+50,y-30), width/9)

# -----------------------------------------------------------