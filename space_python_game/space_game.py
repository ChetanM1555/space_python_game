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
grey4 = (100,100,100)
darkgrey = (50,50,50)

clock = pygame.time.Clock()

bg = pygame.image.load('space.gif')

width = 120

lives = 3


# -----------------------------------------------------------

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

# -----------------------------------------------------------

def move(x, y, ship):
    """
    moves the user
    """
    window.blit(ship, (x, y))

# -----------------------------------------------------------

def game_loop():
    """
    The main game loop that runs the game
    """
    lives = 3
    font = pygame.font.Font('freesansbold.ttf', 32)

    clock = pygame.time.Clock()
    ship = pygame.image.load('k.png')
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

    while closed == False and lives > 0:
        text = font.render(f'Lives left: {lives}', True, white)
        textRect = text.get_rect()
        textRect.center = (display_height//5.5, display_width//26)
        window.blit(bg, (0,0))
        window.blit(text, textRect)
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
            move(x, y, ship)
            pass
        if y > display_height - width or y < 0:
            y_change = 0
            x += x_change
            y += y_change
            move(x, y, ship)
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

        timea = 0
        obst_y += speedy
        obst_x += speedx
        move(x, y, ship)
        counta = 0

        if y < obst_y + height  and y > obst_y or y+height > obst_y and y + height < obst_y + height:
            if x > obst_x and x < obst_x + width1 or x+width > obst_x and x + width < obst_x + width1:
                while True:
                    obst_y += speedy
                    obst_x += speedx
                    dt = clock.tick()
                    timea += dt
                    if timea > 2000:
                        break
                    ship = pygame.image.load('k.png')
                counta += 1

        if counta > 0:
            lives -= 1

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
            if count%4==0:
                obst_speed+=1
                obst_speed2-=1

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

# -----------------------------------------------------------

def text_objects(text, font):
    textTop = font.render(text, True, white)
    return textTop, textTop.get_rect()

# -----------------------------------------------------------

def button(words,x,y,a,b,c,d,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+a > mouse[0] > x and y+b > mouse[1] > y:
        pygame.draw.rect(window, d,(x,y,a,b))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(window, c,(x,y,a,b))

    smallText = pygame.font.SysFont("freesansbold.ttf",27)
    textSurf, textRect = text_objects(words, smallText)
    textRect.center = ( (x+(a/2)), (y+(b/2)) )
    window.blit(textSurf, textRect)

# -----------------------------------------------------------

def game_intro():

    intro = True
    bg = pygame.image.load('space.gif')
    window.blit(bg, (0,0))

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Run Game", 150, 450, 100, 50, grey3, grey4, game_loop)
        button("Quit", 550, 450, 100 ,50, grey3, grey4)

        pygame.display.update()
        clock.tick(15)

game_intro()
# game_loop()