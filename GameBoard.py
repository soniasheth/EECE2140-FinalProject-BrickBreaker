
import pygame 
import numpy as np
from Paddle import *
from Brick import *
from Ball import *

#class has access to all the objects in the 
class GameBoard():
    '''
    This class initializes and holds all the elements and functions needed for the Brick Breaker game. 
    This includes a 2D array of Brick objects, one Ball object, and one Paddle object. (Attributes)

    A GameBoard has 9 attributes ...

    A GameBoard has 6 methods:
    - Initializtion
    - one to draw the contents of the game board on the screen
    - one to check if there is a collision between the ball and the paddle
    - one to check if there is a collsion between the ball and any of the bricks 
    - one to check if the round is over 
    - one to check if the round is over 

    '''
    def __init__(self):
        #numpy array holds all bricks to be hit
        self.bricks = np.empty([3,7], dtype=Brick)
        #x and y starting position of brick 1, rest of the coordinates of the bricks build off of this
        self.x = 5
        self.y = 60
        #create pattern of 21 bricks - initliaze the array of brick objects 
        for row in range(3):
            for col in range(7):
                brick = Brick(self.x, self.y)
                self.bricks[row, col] = brick
                self.x+=85 #increment the x value for the next brick
            #starting a new row of bricks, so reset the values ; increase y value
            self.x = 5
            self.y = self.y + 45

        self.ball = Ball()
        self.paddle = Paddle()

        #keeps tracks of the rounds 
        self.rounds = 1 
        #toggles back and forth between 0 and 1 to represent the ball movement 
        self.start = 0
        #have to keep track of the brick that was hit to control bounce direction 
        self.brick_x = None
        #trackers players lives
        self.lives = 2


    def draw_gameboard(self, window):
        '''
        Inputs: None
        Outputs: An image of the entire Brick Breaker game board interface , given its attributes

        This method draws the game board elements in the game board. 
        Will access the draw functions of the other objects in order to do so 

        '''
        self.ball.draw_ball(window)
        self.paddle.draw_paddle(window)
        #goes through the array and draws all the bricks which havent been hit yet
        for row in range(3):
            for col in range(7):
                #check if the brick has been hit, and draw if it not 
                if self.bricks[row][col].hit_status == False:
                    self.bricks[row, col].draw_brick(window)
                    

    def check_collision_brick(self):
        '''
        Inputs: None 
        Outputs: Boolean, whether there was a collision with the ball and any one of the bricks or not 

        Checks if the ball has collided with any brick in the board or not
        If so, accesses the brick array and turn hit status to the hit brick to on
        '''
        collision = False
        #loop through the array of Bricks
        for row in range(3):
            for col in range(7):
                current_brick = self.bricks[row,col]
                #the ball's coordinates match the outer rim of the brick AND the brick hasn't been hit before -> mark brick has hit
                #goes through each brick 
                if (current_brick.hit_status == False) and (self.ball.x >= current_brick.x) and (self.ball.x <= current_brick.x + current_brick.width) and (self.ball.y >= current_brick.y) and (self.ball.y <= current_brick.y + current_brick.height):
                    collision = True
                    current_brick.hit_status = True
                    #need to track which brick has been hit in order for the ball bounce to properly 
                    self.brick_x = current_brick.x

        return collision

    def check_collision_paddle(self):

        '''
        Inputs: None 
        Outputs: Boolean, whether there was a collision with the ball or paddle or not 

        Check if the ball collided with any part of the the paddle 
        If so, returns true. Else, returns false. 
        '''

        collision = False
        #check if the x and y coodinates overlap with the paddle's (within the width and height of the paddle too)
        if (self.ball.x >= (self.paddle.x - (self.paddle.width/2))) and (self.ball.x <= (self.paddle.x - (self.paddle.width/2)) + self.paddle.width) and (self.ball.y >= self.paddle.y) and (self.ball.y < self.paddle.y + self.paddle.height):
            collision = True
        return collision
    
    def round_over(self): 
        '''
        Inputs: None 
        Outputs: None, just checks and performs the function

        This function checks whether the ball has traveled below the paddle. (Surpassed the paddle's y coodinate)
        If so, the ball and paddle positions will reset to their starting position because the round is over.
        '''
        #check if the y coodinate of the ball is below the paddle
        #if so, reset the position of the ball and paddle to the original position & switch start to OFF
        if (self.ball.y + self.ball.radius >= 490):
            #stop the ball from moving -> turn start off 
            self.start = 0
            #reset the position of ball & paddle to starting position
            self.ball.x = 300
            self.ball.y = 438
            self.paddle.x = 300
            self.paddle.y = 450
            self.rounds = self.rounds + 1
            self.lives = self.lives - 1
    
    def gameover(self):
        '''
        Inputs: None
        Outputs: Boolean, whether the entire game is over or not yet

        This functions checks if the game is over yet: 
        - all bricks are hit: (WIN) OR 3 rounds have been exceeded (LOSE) -> Return True 
        - Else, return False because the game is not over 
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
                    current_brick = self.bricks[row,col]
                    if current_brick.hit_status == False:
                        win = False 
                        break
            return win

        #if all the blocks are hit, then the game is over and you win.
        #if all rounds have exceeded 3, then the game is over and you lose.
        #in both of these cases, return True because the game is over.
        #otherwise, return False because the game isn't over yet.
        if check_all_hit() or self.rounds >= 4:
            return True
        else:
            return False
   
