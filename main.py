#main 
#imports all other classes and runs the main game loop of the game,
#including getting all user input 

#variables: 
#one GameBoard class 

#import classes and modules to be used
import pygame
from Paddle import *
from Brick import *
from Ball import *
from GameBoard import *

#initlizes the pygame and allows us to use the 
pygame.init()

#makes the window that the game will be displayed on 
window = pygame.display.set_mode((600, 500))

#keeps track of whether the game is running or not 
running = True

#sets the window name 
pygame.display.set_caption("Brick Breaker")

#colors
#(R,G,B) <- format
black = (0,0,0)
white = (255,255,255)

#initialize objects - gameboard holds all the objects
gameboard = GameBoard()

def check_key_input():
    '''
    Inputs: None
    Outputs: None

    Will check if there is a key pressed and if so, move the paddle if the correct key is pressed 
    Left arrow pressed -> move the paddle left 
    Right arrow pressed -> move paddle right 
    '''
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            gameboard.paddle.move_paddle(0)
        if event.key == pygame.K_RIGHT:
            gameboard.paddle.move_paddle(1)


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
    Outputs: Boolean

    Will check if the ball has collided with any brick in the board or not
    If so, need to access the brick array and turn hit status to on!
    AND access the x and y coordinte of the the ball to redirect its movement
    '''
    collision = False
    ball = gameboard.ball
    for row in range(2):
        for col in range(7):
            current_brick = gameboard.bricks[row,col]
            if (ball.x >= current_brick.x) and (ball.x <= current_brick.x + current_brick.width) and (ball.y >= current_brick.y) and (ball.y < current_brick.y + current_brick.height):
                collision = True
                current_brick.hit_status = True
    return collision


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
    window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    check_key_input()
    check_collision_brick()
    gameboard.draw_gameboard(window)
    gameboard.ball.move_ball()
    

    pygame.display.update() 

pygame.quit()