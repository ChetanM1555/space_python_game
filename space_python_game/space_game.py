# https://pythonprogramming.net/drawing-objects-pygame-tutorial/

import pygame
import random
import drawings
import updateScore
import screens as sc

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

clock = pygame.time.Clock()

bg = pygame.image.load('space.gif')

width = 120
lives = 3
time_elapsed = 0


# -----------------------------------------------------------

def move(x, y, ship):
    """moves the ship

    Args:
        x (int): x coordinate
        y (int): y coordinate
        ship: this is the ship
    """    
    window.blit(ship, (x, y))

# -----------------------------------------------------------

def game_loop():
    """
    The main game loop that runs the game
    """
    lives = 1
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
    height2 = 155
    width2 = 60
    count = 0
    start_time = pygame.time.get_ticks()

    while closed == False and lives > 0:
        current_time = pygame.time.get_ticks()

        # Calculate the elapsed time
        elapsed_time = current_time - start_time
        hours = int(elapsed_time / (1000 * 60 * 60))
        minutes = int((elapsed_time / (1000 * 60)) % 60)
        seconds = int((elapsed_time / 1000) % 60)

        # seconds = int(elapsed_time / 1000)
        time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        
        timer = font.render("Time: " + time_string, True, (255, 255, 255))

        text = font.render(f'Lives left: {lives}', True, white)
        textRect = text.get_rect()
        
        textRectTime = text.get_rect()

        textRect.center = (display_height//5.5, display_width//26)
        
        textRectTime.center = (display_height//0.92, display_width//26)
        window.blit(bg, (0,0))
        window.blit(text, textRect)
        
        window.blit(timer, textRectTime)

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
        if count %2 :
            drawings.draw1(obst_x, obst_y, height, width1)
        else:
            drawings.draw2(obst_x, obst_y, height, width1)
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
            if x > obst_x and x < obst_x + width1 or x+width+5> obst_x and x + width < obst_x + width1:
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
            if lives == 0:
                game_intro(False,time_string)

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
    """_summary_

    Args:
        text (string): words on button
        font (string): font of text

    Returns:
        text: text on buttons
    """    
    textTop = font.render(text, True, white)
    return textTop, textTop.get_rect()

# -----------------------------------------------------------

def button(words,x,y,a,b,c,d,action=None):
    """Creates buttons 

    Args:
        words (_type_): _description_
        x (int): x coordinate
        y (int): y coordinate
        a (int): width of button
        b (int): height of button
        c (color): color grey
        d (color): color lighter grey
        action (none)
    """    
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

def game_intro(start, time):
    """
    creates game intro
    """
    if start == False:
        updateScore.add_new_score(time)
    intro = True
    bg = pygame.image.load('space.gif')
    window.blit(bg, (0,0))

    intro = True
    bg = pygame.image.load('space.gif')
    window.blit(bg, (0,0))

    font = pygame.font.Font('freesansbold.ttf', 40)
    if start == True:
        text = font.render('Welcome to my Game', True, white)
    else:
        text = font.render('Game Over', True, white)
    textRect = text.get_rect()

    textRect.center = (display_height // 1.5, display_width // 3 )

    while intro:
        window.blit(text, textRect)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("High Scores", 325, 380, 150, 50, grey3, grey4, high_score)
        button("Start Game", 325, 450, 150, 50, grey3, grey4, game_loop)
        button("Quit", 325, 520, 150 ,50, grey3, grey4, quit)

        pygame.display.update()
        clock.tick(15)

# -----------------------------------------------------------

def high_score():
    f = open("score.txt", "r")
    content = f.read()
    content=content.splitlines()
    # print(content)
    intro = True
    bg = pygame.image.load('space.gif')
    window.blit(bg, (0,0))
    font1 = pygame.font.Font('freesansbold.ttf', 40)
    font = pygame.font.Font('freesansbold.ttf', 30)

    text2 = font1.render('High Score', True, white)

    textRect2 = text2.get_rect()

    textRect2.center = (display_height // 1.5, display_width //8 )

    for i in range(len(content)):
        text_surface = font.render(content[i], True, (255, 255, 255))
        window.blit(text_surface, (340, i*30 + 150))

    while intro:
        window.blit(text2, textRect2)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Start Game", 325, 450, 150, 50, grey3, grey4, game_loop)
        button("Quit", 325, 520, 150 ,50, grey3, grey4, quit)

        pygame.display.update()
        clock.tick(15)
    f.close()

# -----------------------------------------------------------

    # def game_over(time):
#     '''
#     Create game over screen
#     '''
#     # print(time)
#     # print(type(time))
#     updateScore.add_new_score(time)
#     intro = True
#     bg = pygame.image.load('space.gif')
#     window.blit(bg, (0,0))
    

#     font = pygame.font.Font('freesansbold.ttf', 40)

#     text = font.render('Game Over', True, white)

#     textRect = text.get_rect()

#     textRect.center = (display_height // 1.5, display_width //3 )

#     while intro:
#         window.blit(text, textRect)
#         for event in pygame.event.get():

#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#         button("High Scores", 325, 380, 150, 50, grey3, grey4, high_score)
#         button("Start Game", 325, 450, 150, 50, grey3, grey4, game_loop)
#         button("Quit", 325, 520, 150 ,50, grey3, grey4, quit)

#         pygame.display.update()
#         clock.tick(15)
#     pass

# -----------------------------------------------------------

def quit():
    pygame.quit()
    quit()

# -----------------------------------------------------------

game_intro(True, "")

