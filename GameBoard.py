import pygame 
import numpy as np
from Paddle import *
from Brick import *
from Ball import *


class GameBoard():
    '''
    This class will hold all the elements needed for the Brick Breaker game. 
    This includes a 2D array of Brick objects, one Ball object, and one Paddle object. (Attributes)

    A GameBoard has one method to draw the contents of the game board on the screen

    '''
    def __init__(self):
        #numpy array holds all bricks to be hit
        self.bricks = np.empty([3,7], dtype=Brick)
        #x and y starting position of brick 1
        self.x = 5
        self.y = 60
        #create pattern of 14 bricks - update 
        for row in range(3):
            for col in range(7):
                brick = Brick(self.x, self.y)
                self.bricks[row, col] = brick
                self.x+=85 #increment the x value for the next brick
            #starting a new row of bricks, so reset the values 
            self.x = 5
            #self.y = 85
            self.y = self.y + 45


        self.ball = Ball()
        self.paddle = Paddle()
        

    def draw_gameboard(self, window):
        '''
        Inputs: None
        Outputs: An image of the entire Brick Breaker game board interface , given its attributes

        This method will draw the game board elements in the game board. 
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
