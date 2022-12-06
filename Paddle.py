import pygame

class Paddle():
    '''
    This class will create the paddle object which is controlled by the user with key inputs

    A Ball has 4 attributes: x position, y posiiton, velocity, and color 
    A Ball has 2 methods, one to move the ball by changing the x and y coordinates of the ball and 
    another to draw the ball itself onto the screen.

    '''
    def __init__(self):
       #starting x and y position of the paddle
       self.x = 300
       self.y = 450
       self.height = 15
       self.width = 115
       self.x_vel = 7
       self.color = (0,0,255) #magenta 
       #holds the rectangle
       #self.paddle_rec = pygame.Rect(self.x, self.y, self.width, self.height)
       
    def move_paddle(self, direction):
        '''
        Inputs: None
        Outputs: A new set of x and y coordinates for the paddle

        This method will change the x of the paddle object in order to 'move' it
        '''
        #if(self.x+(self.width/2) >= 600 or self.x-(self.width/2 <= 0):
            #self.x_vel= (-1)*self.x_vel
        #self.x = (self.x + self.x_vel)
        #if direction == 1:
            #self.x = (self.x + self.x_vel) % 600
        #else:
            #self.x = (self.x - self.x_vel) % 600

        if direction == 1 and not self.x+(self.width/2) >= 600:
                self.x = (self.x + self.x_vel)
        if direction == 0 and not self.x-(self.width/2) <= 0:
                self.x = (self.x - self.x_vel)

    def draw_paddle(self, window):
        '''
        Inputs: None
        Outputs: An image of the paddle, given its attributes

        This method Will produce an image of the paddle at its current x and y coordinates.
        '''
        pygame.draw.rect(window, self.color , ((self.x - (self.width/2), self.y, self.width, self.height)))
        #(self.x - (self.width/2)
