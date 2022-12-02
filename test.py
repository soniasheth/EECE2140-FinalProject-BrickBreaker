# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
 
# Fill the scree with white color
    window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the solid circle
    pygame.draw.circle(window, (0, 255, 0),
                   [300, 300], 170, 0)
 
# Draws the surface object to the screen.
    pygame.display.update()



'''

screen = pygame.display.set_mode([500, 500])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False


screen.fill((255, 255, 255))
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
pygame.display.flip()
pygame.quit()

'''