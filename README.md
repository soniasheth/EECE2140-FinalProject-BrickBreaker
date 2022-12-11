# EECE2140-FinalProject-BrickBreaker
Final Project for EECE2140: The Brick Breaker game.

Creator: Sonia Sheth

**Summary**

  Brick Breaker is a classic game in which a player must 'smash' all bricks in a wall by deflecting a boucing ball with a paddle. The player is able to move the paddle from left to right (and vice versa) in order to deflect the ball. If the player fails to catch/deflect the ball with the paddle before all the bricks are gone, the player loses.
  
  The purpose of this program is to create a playable version of the Brick Breaker Game. To begin, the program will display a pattern of 21 bricks and a stationary paddle and ball at the bottom of the screen. Upon the push of the the 'enter' / 'return' key, the game will start and the ball will begin to move. The player can control the paddle's movement with the left and right arrow keys. 
  
  If the ball hits a brick, the brick is 'hit' and will disappear and the ball will deflect in a different direction depending on where the ball hit the brick. If the ball hits the paddle, the ball will also deflect back up in a different direction depending on where the ball hit the paddle. Each time the player fails to 'catch'/ 'deflect' the ball with the paddle, the round is over and the ball and paddle will reset to their original position. To start a new round, the 'enter' key must be pressed again. If the player fails to hit all the bricks in under 3 rounds, the game is over and the player loses. On the contrary, if the player hits all the bricks in 3 rounds or less, the player wins.
  
**Tools & Libraries**
This program includes the use of the Pygame module. 
  
**Code Overview & Structure**

  In this program there are 4 classes and a main. The four classes include: Ball, Paddle, Brick, and GameBoard. At a high level, the Ball, Paddle, and Brick classes all hold the individual attributes and methods to control those individual objects in the game. The GameBoard class contains an initilaized ball, paddle, and an array of brick objects as attributes, along with the methods and other attributes to control game play. See below for detailed description for all classes and main. No inheritance between classes.
  
**Paddle Class** : This class creates the paddle object displayed on the screen which is controlled by the user with key inputs. 

A Paddle has 4 attributes:
  - x position : Number, holds the x coordinate of the paddle 
  - y position : Number, holds thr y coordinate of the paddle
  - height: Number, the height of the rectangle paddle 
  - width : Number, the width of the rectangle paddle object
  - velocity : Number, holds the rate of change of the x position of the ball (that is all that changes for the paddle)
  - color : holds the color of the paddle 
  
A Paddle has 3 methods:
  - Init.
    - This method initializes all the attributes descirbed above to their starting value 
  - draw_paddle
    - This method produces an image of the paddle at its current x and y coordinates.
  - move_paddle 
    - This method changes the x position of the paddle (increasing / decresing by the declared velocity) in order to 'move' it 
    

**Brick Class** : This class creates one brick, part of the blocks of bricks in the overall game. 

A Brick has 6 attributes: 
- x position : Number, holds the x coordinate of the brick
- y position : Number, holds the y coordinate of the brick
- height : Number, holds the height of the brick (rectangle)
- width : Number, holds the width of the brick (rectangle)
- color : hold the color of the brick
- hit status : Boolean, represents whether the brick has been hit or not

A Brick has two methods:
- Init.
  - This method initializes all the attributes descirbed above to their starting value 
- draw_brick
  - This method produces an image of the brick at its x and y coordinates
  
**Ball Class** : This class creates the ball object which moves throughout the brick breaker game.

A Ball has 7 attributes: 
- x position : Number, holds the x coordinate of the ball
- y position : Number, holds the y coordinate of the ball
- radius: Number, holds the radius of the ball
- x-velocity : Number, holds the rate of change of the x position of the ball
- y-velocity : Number, holds the rate of change of the y position of the ball
- color : holds the color of the ball 
- straight_movement: Number, whether the ball is moving straight up and down or not
    
A Ball has 4 methods:
  - Init.
    - This method intializes all the attributes described above to their starting values. 
  - draw_ball: 
    - This method produces an image of the ball on the window at its current x and y coordinates
  - move_ball
    - This method will move the ball by updating the x and y position of the ball object.
    - The method also handles bounces and redirects the direction of the ball if there is a collision with the paddle, walls, or any brick. 
      - Makes use of the helper methods, bounce_ball, in order to do so. 
  - bounce_ball
    - This method called by the move_ball function when the ball has collided with any surface of either the brick or paddle. 
    - The method redirects by negating the x/y velocity of the ball based on where the ball hit the surface:
      - If on the right side, the ball is redirected to bounce to the left (increasing x position)
      - If on the left side, the ball is redirected to bounce to the right (decreasing x position)
      - If in the middle, the ball is redirected to bounce straight up or down (switch y velocity) 
      
      
**GameBoard Class** : This class initializes and holds all the elements and functions needed for the Brick Breaker game. 

A GameBoard has 9 attributes 
- x: Number, holds the starting x position of the leftmost and topmost brick (top left corner)
- y: Number, holds the starting y position of the leftmost and topmost brick (top left corner)
- bricks: Numpy Array of Brick Objects, a 2d array with 3 rows and 7 columns holding 21 bricks objects in total (holds all the bricks in the game)
- paddle: Paddle, Paddle Object 
- ball: Ball, Ball Object
- rounds: Number, holds current round number the player is on
- lives: Number, holds the amount of lives the player currently has left
- start: Number (0 or 1), holds whether or not whether the ball should be moving
- brick_x: Number, holds the x value of the current / last brick hit

A GameBoard has 6 methods: 
  - Init.
    - This method intializes all the attributes described above to their starting values. This includes filling the array of bricks with the Brick objects
  - draw_gameboard
    - This method draws the game board elements in the game board: ALL the bricks, the ball, and the paddle 
    - Will access the draw functions of the other objects in order to do so 
  - check_collision_brick
    - This method checks if the ball has collided with any brick in the board or not. Returns True is there is a collision and False if not.
    - If so, the hit status if the brick collided with is turned on 
    - Also, stores the x coordinate of the brick hit so that the move_ball function knows where to bounce 
  - check_collion_paddle
    - This method check if the ball has collided with any part of the the paddle. If so, returns true. Else, returns false. 
  - round_over
    - This function will check whether the ball has traveled below the paddle. (Surpassed the paddle's y coodinate)
    - If so, the ball and paddle positions will reset to their starting position because the round is over.
  - gameover
    - This functions checks if the game is over yet: 
        - all bricks are hit: (WIN) OR 3 rounds have been exceeded (LOSE) -> Return True 
        - Else, return False because the game is not over
        
**Main**

Purpose: 
  - The main method contains the main game loop for the brick breaker game. There is a main while loop that checks for events and uses the attributes and   methods within the initliazes GameBoard class to control movement and images printed to the screen.

Variables: 
  - The main initializes one GameBoard object
  
Functions: 
  - check_key_input: Checks if there is a key pressed and if so, move the paddle if the correct key is pressed. Will only allow the paddle to move if the   return key has been pressed 
    - Left arrow pressed -> move the paddle left 
    - Right arrow pressed -> move paddle right 
    - Return / Eneter Key pressed -> allow paddle to move
   
Other: 
- The main also initilizes the pygame module and all the elements needed to use it.


**Instructions for Use**

1. Download and run the main code. (You are going to need pygame installed). A pop up screen with the game will appear. You should see 21 red bricks close to the top of the screen and a white ball on top of a blue paddle towards the bottom. 
2. Press enter / return to start the round. This will prompt the movement of the ball. 
3. After pressing enter, you can use the left and right arrow keys to move the paddle back and forth. The left arrow key will move the paddle left and the right arrow key will move the paddle right.
4. Use the left and right arrow keys to move the paddle and 'catch' / 'deflect' the moving ball. You want the ball to hit the paddle and bounce back up.      If the ball misses the paddle, the round is over and the ball and paddle will rest.
5. When a round is over, repeat steps 2-3
6. For more clarity on the game, review the rules below

Rules 
1. The objective of the game is to hit all the bricks with the ball in 3 rounds or under. If you hit all the bricks in 3 rounds or under, then the player wins the game. Otherwise, they lose.
2. In order to hit the bricks, move the paddle back and forth with the left and right arrow keys to catch/deflect the ball.
3. If you miss the ball with the paddle, the round is over and the ball and paddle will reset. 
4. There are 3 rounds in the game. If the player fail to hit all the bricks in 3 rounds or under, the player loses.


**Future Development**

Below are a couple of ways to further development this Brick Breaker Program. 

1. **Changing Speed of the Ball**: Currently, the value of speed of the ball (x velocity & y velocity) stays the same when it collides with an object, only the direction changes by negating the values. A feature to add to the game is changing the value of the speed of the ball when it collides with an object. The speed of the ball should be adjusted based on WHERE it hits the object. For instance, if the ball hits the corner of the brick or paddle, this could lead to a faster ball. This would make the game more similar to the original Brick Breaker game. 
2. **Give the bricks 'lives'**: Currently, the bricks are considered 'hit' after the ball collides with it one time. A feature to add would be to create certain bricks that need to be hit 2-3 times before being consider 'hit'. This would add some complexity to the game. 
4. **Let the player play again**: Currently, the player is allowed to only play the game once. A loop could be added so that the game keeps playing until the player doesn't want to anymore.
5. **Introduce levels & new brick patterns**: This related to #3. If a player wins the game, a feature that could be added is to have them move onto a new level with high complexity. This high complexity could include a new brick pattern and bricks with more lives as described in #2.

