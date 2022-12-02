import pygame

class Paddle():
    '''
    This class will create the paddle object which is controlled by the user with key inputs

    A Ball has 4 attributes: x position, y posiiton, velocity, and color 
    A Ball has 2 methods, one to move the ball by changing the x and y coordinates of the ball and 
    another to draw the ball itself onto the screen.

    '''
    def __init__(self):
    
       self.x = 300
       self.y = 450
       self.height = 10
       self.width = 150
       self.x_vel = 7
       self.color = (255,0,255)
       
    def move_paddle(self, direction):
        '''
        Inputs: None
        Outputs: A new set of x and y coordinates for the paddle

        This method will change the x of the paddle object in order to 'move' it
        '''
        if direction == 1:
            self.x = (self.x + self.x_vel) % 600
        else:
            self.x = (self.x - self.x_vel) % 600

    def draw_paddle(self, window):
        '''
        Inputs: None
        Outputs: An image of the paddle, given its attributes

        This method Will produce an image of the paddle at its current x and y coordinates.
        '''
        pygame.draw.rect(window, self.color , (self.x, self.y, self.width, self.height))

        