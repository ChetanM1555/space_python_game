import pygame
import space_game as sp


pygame.init()

global_time_elapsed = 0

display_width = 800
display_height = 600

window = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 150, 0)
grey = (70,70,70)
grey2 = (60,60,60)
grey3 = (50,50,50)
grey4 = (100,100,100)
darkgrey = (50,50,50)

# -----------------------------------------------------------

def game_intro():
    """
    creates game intro
    """
    intro = True
    bg = pygame.image.load('space.gif')
    window.blit(bg, (0,0))

    intro = True
    bg = pygame.image.load('space.gif')
    window.blit(bg, (0,0))

    font = pygame.font.Font('freesansbold.ttf', 40)

    text = font.render('Welcome to my Game', True, white)

    textRect = text.get_rect()

    textRect.center = (display_height // 1.5, display_width // 3 )

    while intro:
        window.blit(text, textRect)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("High Scores", 325, 380, 150, 50, grey3, grey4, high_score)
        button("Start Game", 150, 450, 150, 50, grey3, grey4, sp.game_loop)
        button("Quit", 500, 450, 150 ,50, grey3, grey4, quit)

        pygame.display.update()
        clock.tick(15)

# -----------------------------------------------------------

def game_over():
    '''
    Create game over screen
    '''
    intro = True
    bg = pygame.image.load('space.gif')
    window.blit(bg, (0,0))

    font = pygame.font.Font('freesansbold.ttf', 40)

    text = font.render('Game Over', True, white)

    textRect = text.get_rect()

    textRect.center = (display_height // 1.5, display_width //3 )

    while intro:
        window.blit(text, textRect)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("High Scores", 325, 380, 150, 50, grey3, grey4, high_score)
        button("Restart Game", 150, 450, 150, 50, grey3, grey4, sp.game_loop)
        button("Quit", 500, 450, 150 ,50, grey3, grey4, quit)

        pygame.display.update()
        clock.tick(15)
    pass

# -----------------------------------------------------------

def high_score():
    f = open("score.txt", "r")
    content = f.read()
    content=content.splitlines()
    print(content)
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
        window.blit(text_surface, (295, i*30 + 150))

    while intro:
        window.blit(text2, textRect2)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Start Game", 150, 450, 150, 50, grey3, grey4, sp.game_loop)
        button("Quit", 500, 450, 150 ,50, grey3, grey4, quit)

        pygame.display.update()
        clock.tick(15)
    f.close()

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
