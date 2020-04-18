import pygame
import time

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('title')
### all functions ####
clock = pygame.time.Clock()
##call functions here to initiate functions##
running = True

while running:
    #game loop, ass long as your game is running
    #this loop will cycle through with every frame
    clock.tick(60)
    
    for event in pygame.event.get():
        ###this is for all your keypress handling,checked per loop###
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    #screen.fill(0,0,0)

    #screen.blit
    #all sprite.draw

    pygame.display.update()
    pygame.display.flip()


pygame.quit()
