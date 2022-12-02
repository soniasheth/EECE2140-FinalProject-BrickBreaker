import pygame
class Brick():
    '''
    This class will create one brick, part of the blocks of bricks in the overall game. 

    A Brick has 6 attributes: x position, y position, length, width, color, and a hit status 
    A Brick has one method to draw the brick onto the screen. 

    '''
    def __init__(self):
        '''
        Initializes the 
        '''
        self.x = None
        self.y = None 
        self.height = None
        self.width = None 
        self.color = None
        #Boolean value that represents whether the brick has been hit or not 
        self.hit_status = None
        

    def draw_brick(self, window):
        '''
        Inputs: None
        Outputs: An image of the ball, given its attributes

        This method Will produce an image of the brick at its current x and y coordinate
        '''
        pygame.draw.rect(window, self.color , (self.x, self.y, self.width, self.height))