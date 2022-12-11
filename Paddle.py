import pygame

class Paddle():
    '''
    This class creates the paddle object displayed on the screen which is controlled by the user with key inputs. 

    A Paddle has 6 attributes: x position, y posiiton, velocity, height, width, and color 
    A Paddle has 3 methods:
    -  Initialization 
    -  one to move the ball by changing the x and y coordinates of the ball
    -  another to draw the ball itself onto the screen.

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

        This method changes the x position of the paddle object in order to 'move' it
        '''

        if direction == 1 and not self.x+(self.width/2) >= 600:
                self.x = (self.x + self.x_vel)
        if direction == 0 and not self.x-(self.width/2) <= 0:
                self.x = (self.x - self.x_vel)

    def draw_paddle(self, window):
        '''
        Inputs: None
        Outputs: An image of the paddle, given its attributes

        This method produces an image of the paddle at its current x and y coordinates.
        '''
        pygame.draw.rect(window, self.color , ((self.x - (self.width/2), self.y, self.width, self.height)))
        #(self.x - (self.width/2)
