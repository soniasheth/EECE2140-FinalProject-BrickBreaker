
#import classes and modules to be used
import pygame
from Paddle import *
from Brick import *
from Ball import *
from GameBoard import *

#initlizes the pygame and allows us to use the pygame molule
pygame.init()

#stuff needed for the fonts & displaying text, later in game loop
pygame.font.init()
font1 = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 24)


#makes the window that the game will be displayed on - chose size 
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
#have to keep track of the brick that was hit to control bounce direction 
#ideally, need to find a way not to have this 
brick_x = None
#trackers players lives
LIVES = 2

def check_key_input():
    '''
    Inputs: None
    Outputs: None

    Will check if there is a key pressed and if so, move the paddle if the correct key is pressed
    ***Will only allow the paddle to move if the return key has been pressed  

    Left arrow pressed -> move the paddle left 
    Right arrow pressed -> move paddle right 
    Return / Eneter Key pressed -> allow paddle to move
    '''
    if event.type == pygame.KEYDOWN:
        #controls the movement of the paddle 
        #start the game
        if event.key == pygame.K_RETURN:
            global start
            start = 1
        if start == 1:
            if event.key == pygame.K_LEFT:
                gameboard.paddle.move_paddle(0)
            if event.key == pygame.K_RIGHT:
                gameboard.paddle.move_paddle(1)

def check_collision_brick():
    '''
    Inputs: None 
    Outputs: Boolean, whether there was a collision with the ball and any one of the bricks or not 

    Will check if the ball has collided with any brick in the board or not
    If so, need to access the brick array and turn hit status to the hit brick to on!
    '''
    collision = False
    ball = gameboard.ball
    #loop through the array of Bricks
    for row in range(3):
        for col in range(7):
            current_brick = gameboard.bricks[row,col]
            #the ball's coordinates match the outer rim of the brick AND the brick hasn't been hit before -> mark brick has hit
            #goes through each brick 
            if (current_brick.hit_status == False) and (ball.x >= current_brick.x) and (ball.x <= current_brick.x + current_brick.width) and (ball.y >= current_brick.y) and (ball.y <= current_brick.y + current_brick.height):
                collision = True
                current_brick.hit_status = True
                #need to track which brick has been hit in order for the ball bounce to properly 
                global brick_x
                brick_x = current_brick.x
                break

    return collision


def check_collision_paddle():

    '''
    Inputs: None 
    Outputs: Boolean, whether there was a collision with the ball or paddle or not 

    Will check if the ball collided with any part of the the paddle 
    If so, need to access the x and y coodindate of the ball and change them to redirect the ball movement
    only want the collision to be at the top part of the paddle and the sides 
    '''

    collision = False
    ball = gameboard.ball
    paddle = gameboard.paddle
    #check if the x and y coodinates overlap with the paddle's (within the width and height of the paddle too)
    if (ball.x >= (paddle.x - (paddle.width/2))) and (ball.x <= (paddle.x - (paddle.width/2)) + paddle.width) and (ball.y >= paddle.y) and (ball.y < paddle.y + paddle.height):
        collision = True
    return collision
    

def round_over(): 
    '''
    Inputs: None 
    Outputs: None, just checks and performs the function

    This function will check whether the ball has traveled below the paddle. (Surpassed the paddle's y coodinate)
    If so, the ball and paddle positions will reset to their starting position because the round is over.
    '''
    #have to access global variables 
    global rounds
    global LIVES
    #check if the y coodinate of the ball is below the paddle
    #if so, reset the position of the ball and paddle to the original position & switch start to OFF
    if (gameboard.ball.y + gameboard.ball.radius >= 490):
        #stop the ball from moving -> turn start off 
        global start
        start = 0
        #reset the position of ball & paddle to starting position
        gameboard.ball.x = 300
        gameboard.ball.y = 438
        gameboard.paddle.x = 300
        gameboard.paddle.y = 450
        rounds = rounds + 1
        LIVES = LIVES - 1

def gameover():
    '''
    Inputs: None
    Outputs: Boolean, whether the entire game is over or not yet

    Will check if:
    - all bricks are hit: (WIN)
    - 3 rounds have been exceeded (LOSE)
    '''
    def check_all_hit():
        '''
        Inputs: None 
        Outputs: Boolean: Whether or not all the bricks have been hit yet 

        Checks if all the bricks have been hit by the ball 
        '''
        win = True
        #loops through and checks the hit status of all the bricks 
        #if one brick has a hit status that is not OFF, then all hit is false 
        for row in range(3):
            for col in range(7):
                current_brick = gameboard.bricks[row,col]
                if current_brick.hit_status == False:
                    win = False 
                    break
        return win

    global rounds
    #if all the blocks are hit, then the game is over and you win.
    #if all rounds have exceeded 3, then the game is over and you lose.
    #in both of these cases, return True because the game is over.
    #otherwise, return False because the game isn't over yet.
    if check_all_hit() or rounds >=4:
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
        #draw the gameboard every time 
        gameboard.draw_gameboard(window)
        #check for any of the keyinput 
        check_key_input()
        #display lives 
        img = font2.render("Lives: " + str(LIVES), True, (0,255,0))
        window.blit(img, (530,15))
        #will only start if the return/enter key is pressed
        if start == 1:
            #move the ball, check for collision and send to move ball function so that the ball moves accordingly
            gameboard.ball.move_ball(check_collision_brick(), "b", brick_x)
            gameboard.ball.move_ball(check_collision_paddle(), "p", gameboard.paddle.x) #have to know where the paddle is which is why i need to send paddle to the move ball function
        #checks if the round if over and if so, incremeners the round count
        round_over()
    
    #game ended, now display appripate screen if they won or loss
    else: 
        if rounds >= 4:
            img = font1.render('You lost!', True, (255,0,0))
            window.blit(img, (240,250))

        else:
            img = font1.render('You won!', True, (0,230,0))
            window.blit(img, (240,250))
        
    
    pygame.display.update() 

pygame.quit()