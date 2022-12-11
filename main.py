
#import classes and modules to be used
import pygame
from GameBoard import *

# all pygame initiliazations 
pygame.init() #initlizes the pygame and allows us to use the pygame molule
window = pygame.display.set_mode((600, 500)) #makes the window that the game will be displayed on - chose size 
running = True #keeps track of whether the game is running or not
pygame.display.set_caption("Brick Breaker") #sets the window name 

#stuff needed for the fonts & displaying text, later in game loop
pygame.font.init()
font1 = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 24)

#colors
#(R,G,B) <- format
black = (0,0,0)
white = (255,255,255)

#initialize object - gameboard holds all the objects and methods to play the game 
gameboard = GameBoard()

def check_key_input():
    '''
    Inputs: None
    Outputs: None

    Checks if there is a key pressed and if so, move the paddle if the correct key is pressed
    ***Will only allow the paddle to move if the return key has been pressed  

    Left arrow pressed -> move the paddle left 
    Right arrow pressed -> move paddle right 
    Return / Eneter Key pressed -> allow paddle to move
    '''
    if event.type == pygame.KEYDOWN:
        #controls the movement of the paddle 
        #start the game
        if event.key == pygame.K_RETURN:
            gameboard.start = 1
        if gameboard.start == 1:
            if event.key == pygame.K_LEFT:
                gameboard.paddle.move_paddle(0)
            if event.key == pygame.K_RIGHT:
                gameboard.paddle.move_paddle(1)


#main game loop! uses all other functions 
while running: 
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not gameboard.gameover():
        #draw the gameboard every time 
        gameboard.draw_gameboard(window)
        #check for any of the keyinput 
        check_key_input()
        #display lives 
        img = font2.render("Lives: " + str(gameboard.lives), True, (0,255,0))
        window.blit(img, (530,15))
        #will only start if the return/enter key is pressed
        if gameboard.start == 1:
            #move the ball, check for collision and send to move ball function so that the ball moves accordingly
            gameboard.ball.move_ball(gameboard.check_collision_brick(), "b", gameboard.brick_x)
            gameboard.ball.move_ball(gameboard.check_collision_paddle(), "p", gameboard.paddle.x) #have to know where the paddle is which is why i need to send paddle to the move ball function
        #checks if the round if over and if so, incremeners the round count
        gameboard.round_over()
    
    #game ended, now display appripate screen if they won or loss
    else: 
        if gameboard.rounds >= 4:
            img = font1.render('You lost!', True, (255,0,0))
            window.blit(img, (240,250))

        else:
            img = font1.render('You won!', True, (0,230,0))
            window.blit(img, (240,250))
        
    
    pygame.display.update() 

pygame.quit()