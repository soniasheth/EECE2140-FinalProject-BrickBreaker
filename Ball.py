import pygame

class Ball():
    '''
    This class will create the ball object which moves throughout the brick breaker game.

    A Ball has 4 attributes: x position, y posiiton, velocity, and color 
    A Ball has 2 methods, one to move the ball by changing the x and y coordinates of the ball and 
    another to draw the ball itself onto the screen.

    '''
    def __init__(self):
        self.x = 300 #starting x posiiton, center of ball  
        self.y = 438 #starting y position - needs to be immediatly above the paddle. (substract the radius of the ball) 
        self.radius = 12
        self.velx = 1
        self.vely = 1
        self.color = (255,255,255) #black
        
    def move_ball(self, hit):
        '''
        Inputs: None
        Outputs: A new set of x and y coordinates 

        This method will change the x and y position of the ball object in order to move it
        '''
        #check if collide with walls, change velocity if so 
        if(self.x+self.radius >= 600 or self.x-self.radius <= 0):
            self.velx = (-1) * self.velx

        if(self.y+self.radius >= 500 or self.y-self.radius <= 0):
            self.vely = (-1) * self.vely
        #if the ball collides with something, it will bounce in another direction COME BACK AND CHANGE SLOPES AND STUFF 
        if hit:
            self.velx = (-1) * self.velx
            self.vely = (-1) * self.vely

        self.x = (self.x + self.velx)
        self.y = (self.y + self.vely)

    def draw_ball(self,window):
        '''
        Inputs: None
        Outputs: An image of the ball, given its attributes

        This method will produce an image of the ball at its current x and y coordinates.
        '''
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)