
import pygame
from pygame.locals import *
pygame.init()

width,height = 800,600
window = pygame.display.set_mode((width,height))

bg_img = pygame.image.load('b.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))

runing = True
while runing:
    window.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()