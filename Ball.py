import pygame
class Ball():
    '''
    This class will create the ball object which moves throughout the brick breaker game.

    A Ball has 7 attributes: x position, y posiiton, x-velocity, y-velocity, color, and whether the ball is moving up and down or not
    
    A Ball has 4 methods:
    - one to move the ball by changing the x and y coordinates of the ball 
        - this function has two helpers that help change the direction of the ball:
            - one function that handles if the ball needs to bounce off the top surface of the paddle or brick
            - one function that handles if the ball needs to bounce off the bottom of a brick
    - one to draw the ball itself onto the screen

    '''
    def __init__(self):
        self.x = 300 #starting x posiiton, center of ball  
        self.y = 438 #starting y position - needs to be immediatly above the paddle. (substract the radius of the ball) 
        self.radius = 12
        self.velx = 0.5
        self.vely = 0.5
        self.color = (255,255,255) #black
        self.straight_movement = 0 #tracks when the movement of the 

    def bounce(self,position,length):
        '''
        Inputs: 
            - Number, position: the current x coordinate position of the brick or paddle (which ever has been hit & called)
            - Number, length : the width of the brick or paddle 
        Outputs: None, just performs the function  

        This method is called when the ball has collided with top surface of either the brick or paddle. 
        The method redirect the ball based on where the ball hit the surface: 
            -   If on the right side, the ball is redirected to bounce to the left
            - If on the left side, the ball is redirected to bounce to the right 
            - If in the middle, the ball is redirected to bounce straight up 

        '''
        #this first part is just taking the lenght of the object (width) and determining what is middle, left, and right 
        #how long (pixels) on the paddle or brick where the ball will bounce straight up
        middle_width = 15 
        #middle calculation for side_width
        new_length = length - middle_width 
        # how long on the paddle or brick where the ball will bouce to the left or right 
        side_width = new_length / 2 

        self.straight_movement = 0

        #bounces on the left of the object
        #redirect the movement to the right -> this means making sure the x_vel is negative since x of the ball should be decreasing to move this way
        if self.x >= position and self.x <= position + side_width:
            if self.velx > 0:
                self.velx = (-1) * self.velx 

        #bounces on the right of the object 
        #redirect movement to the left -> this means making sure the x_vel is positive since x of the ball should be increasing to move this way
        elif self.x >= position + (side_width + middle_width) and self.x <= position + length:
            if self.velx < 0:
                self.velx = (-1) * self.velx

        #bounces in the middle of the object
        #redirect the ball to move straight up -> this means making making the x position is not changed 
        elif self.x >= position + side_width and self.x <= position + (side_width + middle_width):
            self.straight_movement = 1 #turn straight movement on 

        #in all the cases above, the y vel of the ball needs to be reversed to handle the bounce correctly 
        self.vely = (-1) * self.vely
            
    def brick_bounce_bottom(self,position):
        '''
        Inputs: 
            - Number, position: the current x coordinate position of the brick 

        Outputs: None, just performs the function  

        This method is called when the ball has collided with bottom surface of either the brick
        The method redirect the ball based on where the ball hit the surface: 
            - If on the right side, the ball is redirected to bounce to the right
            - If on the left side, the ball is redirected to bounce to the left
            - If in the middle, the ball is redirected to bounce straight down 
        '''
        self.straight_movement = 0
        #bounce on the left of the brick (bottom)
        #redirect the movement to the left -> this means making sure the x_vel is negative since x of the ball should be decreasing to move this way
        if self.x >= position and self.x <= position + 30:
            if self.velx > 0:
                self.velx = (-1) * self.velx
            
        #bounces on the right of the brick (top)
        #redirect the movement to the right -> this means making sure the x_vel is positive since x of the ball should be increasing to move this way
        elif self.x >= position + 50 and self.x <= position + 80:
            if self.velx < 0:
                    self.velx = (-1) * self.velx

        #bounces in the middle of the brick
        #redirect the ball to move straight down -> this means making sure the x position is not changed 
        elif self.x >= position + 30  and self.x <= position + 50:
            self.straight_movement = 1

        #in all the cases above, the y vel of the ball needs to be reversed to handle the bounce correctly 
        self.vely = (-1) * self.vely
        
    def move_ball(self, hit, item, px):
        '''
        Inputs: 
        Boolean -> 
        Outputs: A new set of x and y coordinates 

        This method will change the x and y position of the ball object in order to move it
        '''
        #check if collide with left and right wall, change velocity to opposite direction 
        if(self.x+self.radius >= 600 or self.x-self.radius <= 0):
            self.velx = (-1) * self.velx

        #checks if collides with top and bottom wall, change velocity to oppsite direction 
        elif(self.y+self.radius >= 500 or self.y-self.radius <= 0):
            self.vely = (-1) * self.vely

        #if the ball collides with something, it will bounce in another direction COME BACK AND CHANGE SLOPES AND STUFF 
        elif hit and item == "p":
            self.bounce((px - (115/2)), 115)

        elif hit and item == "b":
            #hit on the top 
            if (self.y >= 60 and self.y <= 62) or (self.y >= 105 and self.y <= 107) or (self.y >= 150 and self.y <= 152):
                self.bounce(px, 80)
            #hit on bottom
            elif (self.y >= 98 and self.y <= 100) or (self.y >= 143 and self.y <= 145) or (self.y >= 188 and self.y <= 190):
                #self.brick_bounce_bottom(px)
                self.bounce(px, 80)
            
            #hit on the side of the brick
            else:
               self.velx = (-1) * self.velx
               self.vely = (-1) * self.vely
               
        if self.straight_movement == 0:
            self.x = (self.x + self.velx)
            self.y = (self.y + self.vely)
        else:
            self.y = (self.y + self.vely)


    def draw_ball(self,window):
        '''
        Inputs: None
        Outputs: An image of the ball, given its attributes

        This method will produce an image of the ball at its current x and y coordinates.
        '''
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)





    

