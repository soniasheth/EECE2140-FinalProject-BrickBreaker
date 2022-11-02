# EECE2140-FinalProject-BrickBreaker
Final Project for EECE2140. The Brick Breaker game.

Creator: Sonia Sheth

Brick Breaker is a classic game in which a player must 'smash' all bricks in a wall by deflecting a boucing ball with a paddle. The player is able to move the paddle from left to right (and vice versa) in order to delfect the ball. If the player fails to catch/deflect the ball with the paddle before all the bricks are gone, the player loses.

This program will be a version of the Brick Breaker game. To begin, the program will generate a pattern of bricks along with a stationary paddle and ball. Upon the push of a button or click of a mouse, the ball will begin to move around and the player will be able to move the paddle left and right to 'catch'/ 'deflect' the ball. If the ball hits a brick, the brick is 'hit' and will disappear. If the player fails to 'catch'/ 'deflect' the ball with the paddle 3 times, the game is over and the player loses. If the player hits all the bricks in 3 tries or less, the player wins. 

Structure of the Program:
This program will contains the following classes:
- Main: Will control the overal loop of the game 
- GameBoard Class: This class will hold all the elements needs for the game
        = Attributes:
                - An array of Bricks 
                - A Ball
                - A Paddle 
        - Methods:
                - check_key_input: Will check if there is a key pressed and if so, which one 
                - check_mouse_input: Will if there is a mouse input 

- Ball Class: This class will create the ball object which move throughout. 
        -  Attributes: 
                  - x position 
                  - y position 
                  - velocity 
                  - radius 
                  - color?
        -  Methods
                - move_ball: Will change the x and y position of the ball to move it 
                - draw_ball: Will produce an image of the ball         
-  Brick Class: This class will create one brick. 
        -  Attributes: 
                  - x position 
                  - y position 
                  - length
                  - width
                  - color?
                  - hit_status: a boolean value and represents whether it has been hit or not 
        -  Methods
                 - Draw_Brick: Will produce an image of the brick 
                 
- Paddle Class: This class will create the paddle. 
        -  Attributes: 
                  - x position 
                  - y position 
                  - length
                  - width
                  - velocity
        -  Methods
                - move_paddle: Given a key input, will change the x of the paddle. Will increase/decreae by the velocity
                - draw_paddle: Will produce an image of the paddle

*More classes and methods will probabky be added as the program is developed

Tools & Libraries:
This program will include the use of the Pygame module. This module is essential a GUI and will help draw the objects and create graphics. There is a possibility that tkinter can be used instead of Pygame. 

Highest Priority Features:
-
Medium Priority Features:
Lowest Priority Features:
