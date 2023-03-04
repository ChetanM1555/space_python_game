# https://pythonprogramming.net/drawing-objects-pygame-tutorial/

import pygame
import random

pygame.init()

display_width = 800
display_height = 600

window = pygame.display.set_mode((display_width,display_height))

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 150, 0)
grey = (70,70,70)
grey2 = (60,60,60)
grey3 = (50,50,50)
darkgrey = (50,50,50)

clock = pygame.time.Clock()

bg = pygame.image.load('space.gif')
snoop = pygame.image.load('k.png')
width = 120


#-----------------------------------------------------------

def draw1(x,y, height, width):
    """
    draws the obstacles that the user has to dodge
    """
    pygame.draw.circle(window, grey2, (x+height/2,y+width/2), width/2)
    pygame.draw.circle(window, grey, (x+height/2+10,y+width/2+10), width/2+5)
    pygame.draw.circle(window, grey, (x+height/2+10,y+width/2-7), width/2-3)
    pygame.draw.circle(window, darkgrey, (x+height/2+30,y+width/2), width/6)
    pygame.draw.circle(window, darkgrey, (x+height/2-17,y+width/2+15), width/9)
    pygame.draw.circle(window, darkgrey, (x+height/2-10,y+width/2+26), width/9)
    pygame.draw.circle(window, grey3, (x,y+width), width/9)
    pygame.draw.circle(window, grey2, (x+width,y+width +20), width/12)

#-----------------------------------------------------------

def move(x, y):
    """
    moves the user
    """
    window.blit(snoop, (x, y))

#-----------------------------------------------------------

def game_loop():
    closed = False
    x = (display_width * 0.42)
    y = (display_height * 0.8)
    y_change = 0
    x_change = 0
    obst_speed = 5
    obst_speed2 = -5

    obst_x = random.randrange(0,display_width)
    obst_y = -600
    height = 100
    width1 = 100
    count = 0

    while closed == False:
        window.blit(bg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                    x_change = 0

                if event.key == pygame.K_DOWN:
                    y_change = 5
                    x_change = 0

                if event.key == pygame.K_LEFT:
                    x_change = -5
                    y_change = 0

                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    y_change = 0
        x += x_change
        y += y_change
        if x > display_width - width or x < 0:
            x_change = 0
            x += x_change
            y += y_change
            move(x, y)
            pass
        if y > display_height - width or y < 0:
            y_change = 0
            x += x_change
            y += y_change
            move(x, y)
            pass


        draw1(obst_x, obst_y, height, width1)
        if count%4==0:
            speedx=0
            speedy=obst_speed
        elif count%3==0: 
            speedx=obst_speed
            speedy=0
        elif count%2==0:
            speedx=0
            speedy=obst_speed2
            pass
        else:
            speedy=0
            speedx=obst_speed2

        obst_y += speedy
        obst_x += speedx
        move(x, y)

        if y < obst_y + height  and y > obst_y or y+height > obst_y and y + height < obst_y + height:
            if x > obst_x and x < obst_x + width1 or x+width > obst_x and x + width < obst_x + width1:
                closed = True
        
        # reset obst if it goes out of bounds
        if obst_y > display_height or obst_x > display_width or obst_y < 0 -display_width  or obst_x < 0 - height :
            count = random.randint(1,4)

            if count%4==0:
                obst_y = 0 - height
                obst_x = random.randrange(0,display_width)
            elif count%3==0:
                obst_x = 0 - height
                obst_y = random.randrange(0,display_width)

            elif count%2==0:
                obst_y = 600
                obst_x = random.randrange(0,display_width)
                pass
            else:
                obst_x = 800
                obst_y = random.randrange(0,display_width)
                count = 1
        
            # if count%4==0:
            #     obst_speed+=1
            #     obst_speed2-=1
            
        
        pygame.display.update()
        clock.tick(60)


    pygame.quit()
    quit()

game_loop()