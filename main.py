#main 
#imports all other classes and runs the main game loop of the game,
#including getting all user input 

#variables: 
#one GameBoard class 

'''
Will be a a large while loop that utilizes the functions to run the game

'''

import pygame
from Paddle import *

#initlizes the pygame 
pygame.init()

#makes the window that the game will be displayed on 
window = pygame.display.set_mode((600, 500))

#keeps track of whether the game is running or not 
running = True

#sets the window name 
pygame.display.set_caption("Brick Breaker")

#colors
black = (0,0,0)
white = None

#initialize objects 

paddle = Paddle()

def check_key_input():
    '''
    Inputs: 
    Outputs: String, returns the specific key that is being pressed 

    Will check if there is a key pressed and if so, move the paddle if the correct key is pressed 
    '''
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            paddle.move_paddle(0)
        if event.key == pygame.K_RIGHT:
            paddle.move_paddle(1)


def check_mouse_input():
    '''
    Inputs: 
    Outputs: Boolean, returns the specific ke that is being pressed 

    Will check if there is a key pressed and if so, which one
    '''
    pass

def check_collision_brick():

    '''
    Inputs: 
    Outputs: 

    Will check if the ball has collided with any brick in the board or not
    If so, need to access the brick array and delete it
    AND access the x and y coordinte of the the ball to redirect its movement
    '''
    pass

def check_collision_paddle():

    '''

    Inputs: 
    Outputs: 

    Will check if the ball collided with the paddle 
    If so, need to access the x and y coodindate of the ball and change them to redirect the ball movement
    '''
    
    pass

def done():
    '''
    Inputs: 
    Outputs: Boolean, whether the game is done or not 

    Will check if the ball goes below the lowest y coordinate (PLAYER LOSES) OR if all the bricks are done (PLAYER WINS)
    '''
    pass

#main game loop
while running: 
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    check_key_input()
    paddle.draw_paddle(window)

    pygame.display.update() 

pygame.quit()