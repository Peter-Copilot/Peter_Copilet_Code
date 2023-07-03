import pygame
from pygame import locals
pygame.init()

surface=pygame.display.set_mode((660,480))

body = pygame.image.load('body.png')
apple = pygame.image.load('apple.png')
head = pygame.image.load('right.png')
beijing = pygame.image.load('bg.png')
while True:
    for event in pygame.event.get():
        if event.type == locals.QUIT:
            exit()
    
    surface.blit(beijing,(0,0))
    surface.blit(body,(210,120))
    surface.blit(body,(180,120))
    surface.blit(body,(180,90))
    surface.blit(apple,(210,240))
    surface.blit(head,(240,120))
    pygame.display.update()
    

