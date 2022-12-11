import pygame

class Ball():
    '''
    This class will create the ball object which moves throughout the brick breaker game.

    A Ball has 4 attributes: x position, y posiiton, velocity, and color 
    A Ball has 2 methods, one to move the ball by changing the x and y coordinates of the ball and 
    another to draw the ball itself onto the screen.

    '''
    def __init__(self):
        self.x = 300 #starting x posiiton, center of ball  300
        self.y = 438 #starting y position - needs to be immediatly above the paddle. (substract the radius of the ball) 438
        self.radius = 12
        self.velx = 1.5
        self.vely = 1.5
        self.color = (255,255,255) #black
        self.straight_movement = 0 #tracks when the movement of the 

    def bounce_up(self,position,length):
        '''
        add doc string
        '''
        #how long on the paddle or brick where the ball will bounce up 
        middle_width = 15 
        new_length = length - middle_width #100
        # how long on the paddle ot brick where the ball will bouce to the
        side_width = new_length / 2 #50

        self.straight_movement = 0
            #bounces on the left of the paddle
        if self.x >= position and self.x <= position + side_width:
            if self.velx > 0:
                self.velx = (-1) * self.velx
        #bounces on the right of the paddle 
        elif self.x >= position + (side_width + middle_width) and self.x <= position + length:
            if self.velx < 0:
                self.velx = (-1) * self.velx
        #bounces in the middle of the paddle
        elif self.x >= position + side_width and self.x <= position + (side_width + middle_width):
            self.straight_movement = 1

        self.vely = (-1) * self.vely
            
    def brick_bounce_bottom(self,px):
        '''
        add doc string
        '''
        self.straight_movement = 0
        #bounce on the left of the brick (bottom)
        if self.x >= px and self.x <= px + 30:
            if self.velx > 0:
                self.velx = (-1) * self.velx
            if self.vely < 0:
                self.vely = (-1) * self.vely
            
        #bounces on the right of the brick (top)
        elif self.x >= px + 50 and self.x <= px + 80:
            if self.velx < 0:
                    self.velx = (-1) * self.velx
            if self.vely < 0:
                self.vely = (-1) * self.vely

        #bounces in the middle of the brick
        elif self.x >= px + 30  and self.x <= px + 50:
            self.vely = (-1) * self.vely
            self.straight_movement = 1

        
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
            self.bounce_up((px - (115/2)), 115)

        elif hit and item == "b":
            #hit on the top 
            if (self.y >= 60 and self.y <= 62) or (self.y >= 105 and self.y <= 107) or (self.y >= 150 and self.y <= 152):
                self.bounce_up(px, 80)
            #hit on bottom
            elif (self.y >= 98 and self.y <= 100) or (self.y >= 143 and self.y <= 145) or (self.y >= 188 and self.y <= 190):
                self.brick_bounce_bottom(px)
            
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





    

