import pygame

class Brick():
    '''
    This class creates one brick, part of the blocks of bricks in the overall game. 

    A Brick has 6 attributes: x position, y position, height, width, color, a hit status
    A Brick has one method to draw the brick onto the screen. 

    '''
    def __init__(self,x,y):
        '''
        Initializes a singular brick. Function takes in the x and y position of the brick
        '''
        self.x = x
        self.y = y
        self.height = 40
        self.width = 80
        self.color = (255,0,0) 
        self.hit_status = False #Boolean value that represents whether the brick has been hit or not
        

    def draw_brick(self, window):
        '''
        Inputs: None
        Outputs: An image of the ball, given its attributes

        This method produces an image of the brick at its current x and y coordinate
        '''
        pygame.draw.rect(window, self.color , (self.x, self.y, self.width, self.height))