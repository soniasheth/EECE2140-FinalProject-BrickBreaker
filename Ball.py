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
        self.velx = 1
        self.vely = 1
        self.color = (255,255,255) #black

        
    def move_ball(self, hit, item, px):
        '''
        Inputs: 
        Outputs: A new set of x and y coordinates 

        This method will change the x and y position of the ball object in order to move it
        '''
        def paddle_bounce():
            '''
            add doc string
            '''
            #bounces on the left of the paddle
            if self.x >= (px - (115/2)) and self.x <= (px - (115/2)) + 55:
                if self.velx > 0:
                    self.velx = (-1) * self.velx
                if self.vely > 0:
                    self.vely = (-1) * self.vely
                #self.x = (self.x + self.velx)
                #self.y = (self.y + self.vely)
            
            #bounces on the right of the paddle 
            elif self.x >= (px - (115/2)) + 60 and self.x <= (px - (115/2)) + 115:
                if self.velx < 0:
                    self.velx = (-1) * self.velx
                if self.vely > 0:
                    self.vely = (-1) * self.vely
                #self.x = (self.x + self.velx)
                #self.y = (self.y + self.vely)

            #bounces in the middle of the paddle
            elif self.x >= (px - (115/2)) + 55 and self.x <= (px - (115/2)) + 60:
                self.y = (self.y - self.vely)

        def brick_bounce_top():
            '''
            add doc string
            '''
            #bounce on the left of the brick
            if self.x >= px and self.x <= px + 30:
                #print("bounce left")
                if self.velx > 0:
                    self.velx = (-1) * self.velx
                if self.vely > 0:
                    self.vely = (-1) * self.vely
                #self.x = (self.x + self.velx)
                #self.y = (self.y + self.vely)
            
            #bounces on the right of the brick 
            elif self.x >= px + 50 and self.x <= px + 80:
                #print("bounce right")
                if self.velx < 0:
                    self.velx = (-1) * self.velx
                if self.vely > 0:
                    self.vely = (-1) * self.vely
                #self.x = (self.x + self.velx)
                #self.y = (self.y + self.vely)

            #bounces in the middle of the brick
            elif self.x >= px+ 30  and self.x <= px + 50:
                #print("bounce middle")
                self.y = (self.y + self.vely)
         
        def brick_bounce_bottom():
            '''
            add doc string
            '''
            #bounce on the left of the brick (bottom)
            if self.x >= px and self.x <= px + 30:
                if self.velx > 0:
                    self.velx = (-1) * self.velx
                if self.vely < 0:
                    self.vely = (-1) * self.vely
                #self.x = (self.x + self.velx)
                #self.y = (self.y + self.vely)
            
            #bounces on the right of the brick (top)
            elif self.x >= px + 50 and self.x <= px + 80:
                if self.velx < 0:
                    self.velx = (-1) * self.velx
                if self.vely < 0:
                    self.vely = (-1) * self.vely
                #self.x = (self.x + self.velx)
                #self.y = (self.y + self.vely)

            #bounces in the middle of the brick
            elif self.x >= px + 30  and self.x <= px + 50:
                self.y = (self.y + self.vely)


        #check if collide with left and right wall, change velocity to opposite direction 
        if(self.x+self.radius >= 600 or self.x-self.radius <= 0):
            self.velx = (-1) * self.velx

        #checks if collides with top and bottom wall, change velocity to oppsite direction 
        if(self.y+self.radius >= 500 or self.y-self.radius <= 0):
            self.vely = (-1) * self.vely

        #if the ball collides with something, it will bounce in another direction COME BACK AND CHANGE SLOPES AND STUFF 
        if hit and item == "p":
            #if hit, flip the direction 
            #self.velx = (-1) * self.velx
            #self.vely = (-1) * self.vely
            paddle_bounce()
        elif hit and item == "b":
            #hit on the top 
            print("y:",self.y)
            if (self.y >= 60 and self.y <= 62) or (self.y >= 105 and self.y <= 107) or (self.y >= 150 and self.y <= 152):
                print("TOP")
                brick_bounce_top()
            #hit on bottom
            elif (self.y >= 98 and self.y <= 100) or (self.y >= 143 and self.y <= 145) or (self.y >= 188 and self.y <= 190):
                print("bottom")
                brick_bounce_bottom()
               
            else:
               self.velx = (-1) * self.velx
               self.vely = (-1) * self.vely
               print("sides")
               

        self.x = (self.x + self.velx)
        self.y = (self.y + self.vely)


    def draw_ball(self,window):
        '''
        Inputs: None
        Outputs: An image of the ball, given its attributes

        This method will produce an image of the ball at its current x and y coordinates.
        '''
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def top_bounce(width):
        pass
    def bottom_bounce():
        pass



    

