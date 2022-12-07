
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

#global variables 
#keeps tracks of the rounds 
rounds = 1
#toggles back and forth between 0 and 1 to represent the ball movement 
start = 0


def check_key_input():
    '''
    Inputs: None
    Outputs: None

    Will check if there is a key pressed and if so, move the paddle if the correct key is pressed 
    Left arrow pressed -> move the paddle left 
    Right arrow pressed -> move paddle right 
    '''
    if event.type == pygame.KEYDOWN:
        #controls the movement of the paddle 
        if event.key == pygame.K_LEFT:
            gameboard.paddle.move_paddle(0)
        if event.key == pygame.K_RIGHT:
            gameboard.paddle.move_paddle(1)
        #start the game
        if event.key == pygame.K_RETURN:
            global start
            start = 1

def check_collision_brick():
    '''
    Inputs: None 
    Outputs: Boolean, whether there was a collision with the ball and a brick or not 

    Will check if the ball has collided with any brick in the board or not
    If so, need to access the brick array and turn hit status to on!
    AND access the x and y coordinte of the the ball to redirect its movement
    '''
    collision = False
    ball = gameboard.ball
    for row in range(3):
        for col in range(7):
            current_brick = gameboard.bricks[row,col]
            #the ball's coordinates match the outer rim of the brick AND the brick hasn't been hit before
            if (current_brick.hit_status == False) and (ball.x >= current_brick.x) and (ball.x <= current_brick.x + current_brick.width) and (ball.y >= current_brick.y) and (ball.y <= current_brick.y + current_brick.height):
                collision = True
                current_brick.hit_status = True

    return collision


def check_collision_paddle():

    '''
    Inputs: None 
    Outputs: Boolean, whether there was a collision with the ball or paddle or not 

    Will check if the ball collided with the paddle 
    If so, need to access the x and y coodindate of the ball and change them to redirect the ball movement
    only want the collision to be at the top part of the paddle and the sides 
    '''

    collision = False
    ball = gameboard.ball
    paddle = gameboard.paddle
    if (ball.x >= (paddle.x - (paddle.width/2))) and (ball.x <= (paddle.x - (paddle.width/2)) + paddle.width) and (ball.y >= paddle.y) and (ball.y < paddle.y + paddle.height):
        collision = True
    return collision
    

def round_over(): 
    '''
    Inputs: None 
    Outputs: None, just checks and performs the function

    This function will check whether the ball has traveled below the lowest y coordinate.
    If so, the ball and paddle positions will reset to their starting position because the round is over.
    '''
    global rounds
    if (gameboard.ball.y + gameboard.ball.radius >= 500):
        global start 
        #stop the ball from moving
        start = 0
        #reset the position of ball & paddle to starting position
        gameboard.ball.x = 300
        gameboard.ball.y = 438
        gameboard.paddle.x = 300
        gameboard.paddle.y = 450
        rounds = rounds + 1

def gameover():
    '''
    Inputs: None
    Outputs: Boolean, whether the entire game is over or not yet

    Will check if:
    - all bricks are hit: (WIN)
    - 3 rounds have been exceeded (LOSE)
    '''
    def all_hit():
        '''
        Inputs: None 
        Outputs: Boolean: Whether or not all the bricks have been hit yet 
        '''
        win = True
        for row in range(3):
            for col in range(7):
                current_brick = gameboard.bricks[row,col]
                if current_brick.hit_status == False:
                    win = False 
        return win

    global rounds
    #if all the blocks are hit, then the game is over and you win.
    #if all rounds have exceeded 3, then the game is over and you lose.
    #in both of these cases, return True because the game is over.
    #otherwise, return False because the game isn't over yet.
    if all_hit() or rounds >=4:
        return True
    else:
        return False


#main game loop! uses all other functions 
while running: 
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not gameover():
        gameboard.draw_gameboard(window)
        check_key_input()     
        if start == 1:
            gameboard.ball.move_ball(check_collision_brick())
            gameboard.ball.move_ball(check_collision_paddle())
        #checks if the round if over and if so, incremeners the round count.
        round_over()
    
    #game ended, now display appripate screen if they won or loss
    if rounds >= 4:
        #write to screen for losing
        pass

    else:
        #writing to screen for winning 
        pass
        
    
    pygame.display.update() 

pygame.quit()