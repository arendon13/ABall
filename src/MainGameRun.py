'''
Created on May 6, 2015

@author: Adrian
'''
import pygame
import sys
import random
import math
from pygame.locals import *
from BallTrap.Wall import Wall
from BallTrap.Ball import Ball
from BallTrap.PowerUps import PowerUps
from BallTrap.UserWall import UserWall
from BallTrap.FillWall import FillWall
from pygame.tests.cursors_test import CursorsModuleTest


def main(balls, lvl):
    pygame.init()

    FPS = 30
    FPS_CLOCK = pygame.time.Clock()

    # COLOR LIST
    WHITE = pygame.Color(250, 250, 250)
    BLACK = (0, 0, 0)
    DGREEN = (0, 102, 0)

    # Code to create the initial window
    window_size = (750, 533)
    SCREEN = pygame.display.set_mode(window_size)

    # set the title of the window
    pygame.display.set_caption("A-Ball")

    # List to hold all the sprites
    all_sprite_list = pygame.sprite.Group()
    
    # Load background
    
    BACKGROUND1 = pygame.image.load("background1.jpg").convert()
    SCREEN.blit(BACKGROUND1,(0,0))
    
    BACKGROUND2 = pygame.image.load("background2.jpg").convert()
    SCREEN.blit(BACKGROUND2,(60,50)) # position 60, 50
    
    #Make Cursors
    HORIZONTAL_ARROW =(
                       "                                ",
                       "                                ",
                       "                                ",
                       "        XX            XX        ",
                       "      XXXX            XXXX      ",
                       "    XXX..X            X..XXX    ",
                       "  XXX....XXXXXXXXXXXXXX....XXX  ",
                       "XXX..........................XXX",
                       "XXX..........................XXX",
                       "  XXX....XXXXXXXXXXXXXX....XXX  ",
                       "    XXX..X            X..XXX    ",
                       "      XXXX            XXXX      ",
                       "        XX            XX        ",
                       "                                ",
                       "                                ",
                       "                                "
                       )
    
    VERTICAL_ARROW =(
                       "       XX       ",
                       "       XX       ",
                       "      XXXX      ",
                       "      X..X      ",
                       "     XX..XX     ",
                       "     X....X     ",
                       "    XX....XX    ",
                       "    X......X    ",
                       "   XX......XX   ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "      X..X      ",
                       "   XX......XX   ",
                       "    X......X    ",
                       "    XX....XX    ",
                       "     X....X     ",
                       "     XX..XX     ",
                       "      X..X      ",
                       "      XXXX      ",
                       "       XX       ",
                       "       XX       ",
                       )

    
    data,mask = pygame.cursors.compile(HORIZONTAL_ARROW,black='.',white='X',xor='o')
    horizontal_cursor = ( (32,16), (16,8), data,mask)
    data,mask = pygame.cursors.compile(VERTICAL_ARROW,black='.',white='X',xor='0')
    vertical_cursor = ( (16,32), (8,16), data,mask)
    
    # Make the walls. (x_pos, y_pos, width, height)
    hor_wall_list = pygame.sprite.Group()
    ver_wall_list = pygame.sprite.Group()
 
    wall = Wall(60, 50, 20, 400, DGREEN) #left wall
    ver_wall_list.add(wall)
    all_sprite_list.add(wall)
    
    wall = Wall(669, 50, 20, 400, DGREEN) # right wall
    ver_wall_list.add(wall)
    all_sprite_list.add(wall)
    
    wall = Wall(60, 50, 629, 20, DGREEN) # top wall
    hor_wall_list.add(wall)
    all_sprite_list.add(wall)
    
    wall = Wall(60, 428, 629, 22, DGREEN) # bottom wall
    hor_wall_list.add(wall)
    all_sprite_list.add(wall)
    
    ball_count = balls + 1
    
    #Make a ball
    ball_list = pygame.sprite.Group()
    
    for x in range(1, ball_count):
        randX = random.randint(120, 600)
        randY = random.randint(100, 380)
        randDx = 2
        randDy = 2
        randNx = random.randint(1, 2)
        randNy = random.randint(1, 2)
        if randNy == 1:
            randDy = randDy * -1
        if randNx == 1:
            randDx = randDx * -1
        b = Ball(randX, randY, randDx, randDy, hor_wall_list, ver_wall_list)
        ball_list.add(b)
        all_sprite_list.add(b)
    
#     b1 = Ball(373, 266, 2, -2, hor_wall_list, ver_wall_list)
#     ball_list.add(b1)
#     all_sprite_list.add(b1)
#      
#     b2 = Ball(200, 290, -2, 2, hor_wall_list, ver_wall_list)
#     ball_list.add(b2)
#     all_sprite_list.add(b2)
    
    #Make PowerUps
    powerUp_list = pygame.sprite.Group()
    slowURL = "slowDown.png"
    speedURL = "speedCola.jpg"
     
    slow1 = PowerUps(89, 90, 1, 1, hor_wall_list, ver_wall_list, slowURL, False, True)
    powerUp_list.add(slow1)
    all_sprite_list.add(slow1)
     
    speed1 = PowerUps(500, 400, -1, 1, hor_wall_list, ver_wall_list, speedURL, True, False)
    powerUp_list.add(speed1)
    all_sprite_list.add(speed1)
    
    movement = (0, 0)
    max_lives = 3
    current_level = lvl
    percent_completed = 0
    area_covered = 0
    total_area = 476
    userWall_list1 = []
    userWall_list2 = []

    verticalOn = True
    horizontalOn = False
    
    start(SCREEN, BACKGROUND1, BACKGROUND2)
    
    while True:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if verticalOn and horizontalOn == False:
                        verticalOn = False
                        horizontalOn = True
                    else:
                        verticalOn = True
                        horizontalOn = False          
                
                
            if event.type == MOUSEBUTTONDOWN:
                # Get the state(s) of the mouse buttons
                buttons = pygame.mouse.get_pressed()

                if buttons[0]:
                    box_y = []
                    box_x = []
                    init_boxes(box_x, box_y)
                    movement = pygame.mouse.get_pos()
                    x = int(movement[0])
                    y = int(movement[1])
                    newXY = getXandY(x, y, box_x, box_y)
                    newX = newXY[0]
                    newY = newXY[1]
                    if verticalOn:
                        width = 20
                        height = 21
                        wall = UserWall(newX, newY, width, height, BLACK, hor_wall_list, ver_wall_list, True, False, newX, newY) #356
                        userWall_list1.append(wall)
                        userWall_list2.append(wall)
                        ver_wall_list.add(wall)
                        all_sprite_list.add(wall)
                    if horizontalOn:
                        wall = UserWall(newX, newY, 21, 20, BLACK, hor_wall_list, ver_wall_list, False, True, newX, newY)
                        userWall_list1.append(wall)
                        userWall_list2.append(wall)
                        hor_wall_list.add(wall)
                        all_sprite_list.add(wall)   
                        
            if event.type == KEYDOWN:
                if event.key == pygame.K_f and userWall_list1:
                    if userWall_list1[len(userWall_list1) - 1].isDead is False: # checks isDead boolean of latest userWall
                        print("pressing f key!")
                        w = userWall_list1[len(userWall_list1) - 1].finalWidth
                        h = userWall_list1[len(userWall_list1) - 1].finalHeight
                        fx = userWall_list1[len(userWall_list1) - 1].finalX
                        fy = userWall_list1[len(userWall_list1) - 1].finalY
                        fillR = userWall_list1[len(userWall_list1) - 1].wasVer
                        fillB = userWall_list1[len(userWall_list1) - 1].wasHor
                        print("%s, %s, %s, %s" % (h, w, fx, fy))
                        if verticalOn:                      
                            wall = FillWall(fx + 21, fy, w, h, BLACK, hor_wall_list, ver_wall_list, True, False, fx + 21, fy)
                            ver_wall_list.add(wall)
                            all_sprite_list.add(wall)
                        if horizontalOn:
                            print("Horizontal fill")
#                         userWall_list.pop()           

        
        all_sprite_list.update(ball_list, powerUp_list)
        ball_list.clear(SCREEN, BACKGROUND2)
        SCREEN.blit(BACKGROUND1,(0,0))
        SCREEN.blit(BACKGROUND2,(60,50)) # position 60, 50
        
        
        # grid 17x28
        draw_hor_lines(SCREEN, WHITE, 81, 70, 667, 70) #688
        draw_ver_lines(SCREEN, WHITE, 80, 71, 80, 427) #80, 71
        update_sprites = all_sprite_list.draw(SCREEN) # areas that should be redrawn
        pygame.display.update(update_sprites)

        if userWall_list1: #checks if list is not empty
            if userWall_list1[len(userWall_list1) - 1].isDead: # checks isDead boolean of latest userWall
                max_lives -= 1
                userWall_list1.pop()
                if max_lives == 0:
                    gameOver(SCREEN, BACKGROUND1, BACKGROUND2, ball_list)
                     
        if userWall_list2:
            if userWall_list2[len(userWall_list2) - 1].isDrawing is False:
                ac = userWall_list2[len(userWall_list2) - 1].getArea()
                area_covered += ac
                percent_completed = calculate_percent(area_covered, total_area)
                userWall_list2.pop()
                if percent_completed > 75:
                    ball_count
                    current_level += 1
                    main(ball_count, current_level)
                    nextLvl(SCREEN, BACKGROUND1, BACKGROUND2, ball_count, current_level)
                    

        draw_text(SCREEN, "LEVEL %s" % (current_level), 320, 25)       
        draw_text(SCREEN, "Lives: %s" % (max_lives), 60, 460)       
        draw_text(SCREEN, "Percent Completed: " + str(percent_completed) + " %", 455, 460)
        
        
        if verticalOn:
            pygame.mouse.set_cursor(*vertical_cursor)
        else:
            pygame.mouse.set_cursor(*horizontal_cursor)

        pygame.display.update()  # Update the display when all events have been processed
        FPS_CLOCK.tick(FPS)

def getXandY(x, y, b_x, b_y):
    """
        Generates a new x and y coordinate to draw the box
        based on the x and y coordinates of the player's click.
        :param x: the x position of the mouse click
        :param y: the y position of the mouse click
        :param b_x: list of initial x locations for graph lines
        :param b_y: list of initial x locations for graph lines
    """
    midPoint = 11
    y1 = 0
    y2 = 0
    x1 = 0
    x2 = 0
    for i in b_y:
        if y > i and y < (i + 21):
            y1 = i
            y2 = i + 21
    
    checkY = y - y1
    if checkY <= midPoint:
        newY = y1
    else:
        newY = y2
        
    for i in b_x:
        if x > i and x < (i + 21):
            x1 = i
            x2 = i + 21
    
    checkX = x - x1
    if checkX <= midPoint:
        newX = x1
    else:
        newX = x2
        
    return (newX, newY)
            

def init_boxes(b_x, b_y):
    """
        Initializes the x and y positions of the main graph by making 
        a list of x coordinates and a list of y coordinates
        :param b_x: empty list which which will get populated with x values
        :param b_y: empty list which which will get populated with y values
    """
    inc = 81
    for i in range(1, 29):
        b_x.append(inc)
        inc = inc + 21
        
    inc = 71
    for i in range(1, 18):
        b_y.append(inc)
        inc = inc + 21
    
def draw_hor_lines(screen, color, s_x, s_y, e_x, e_y):
    """
        Draws the horizontal lines of the graph
        :param screen: passes the pygame screen
        :param color: passes the color to draw the lines with
        :param s_x: constant x position of starting point
        :param s_y: changing y position of starting point by increments of 21
        :param e_x: constant x position of ending point
        :param e_y: changing y position of ending point by increments of 21
    """
    inc = 0   
    for i in range(1, 19):
        pygame.draw.line(screen, color, (s_x, s_y + inc), (e_x, e_y + inc), 1)
        inc = inc + 21

def draw_ver_lines(screen, color, s_x, s_y, e_x, e_y): 
    """
        Draws the vertical lines of the graph
        :param screen: passes the pygame screen
        :param color: passes the color to draw the lines with
        :param s_x: constant x position of starting point
        :param s_y: changing y position of starting point by increments of 21
        :param e_x: constant x position of ending point
        :param e_y: changing y position of ending point by increments of 21
    """
    inc = 0   
    for i in range(1, 30):
        pygame.draw.line(screen, color, (s_x + inc, s_y), (e_x + inc, e_y), 1)
        inc = inc + 21
        
def draw_text(SCREEN, text, x, y):
    """
        Function responsible for displaying text on the game screen
        :param screen: passes the pygame screen
        :param color: passes the color to draw the text with
        :param x: x location of beginning text
        :param y: y location of beginning text
    """
    font = pygame.font.SysFont('Consolas', 30, False, False)
    text_to_draw = font.render(text, True, Color(255,255,255))
    SCREEN.blit(text_to_draw, (x, y))
    
def calculate_percent(num, denum): 
    """
        Function responsible for calculating the percentage of lines drawn as a
        means to help pass the current level
        :param num: numerator of percentage calculation formula
        :param denum: denominator of percentage calculation formula
    """
    p1 = num / denum
    p2 = p1 * 100
    percent = math.ceil(p2)
    return percent
def gameOver(SCREEN, BACKGROUND1, BACKGROUND2, ball_list):
    """
        Function responsible for displaying the game over screen after a player loses
        :param screen: passes the pygame screen
        :param BACKGROUND1: passes background 1 for redraw
        :param BACKGROUND2: passes background 2 for redraw
        :param ball_list: passes ball_list for redraw
    """
    pause = True
    WHITE = pygame.Color(250, 250, 250)
    
    SCREEN.fill(WHITE)
    ball_list.clear(SCREEN, BACKGROUND2)
    SCREEN.blit(BACKGROUND1,(0,0))
    SCREEN.blit(BACKGROUND2,(60,50)) # position 60, 50
    
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    main(2, 1)
                    


        draw_text(SCREEN, "Game Over!", 320, 230)
        draw_text(SCREEN, "Press Space Bar to Play again.", 240, 250)
        
        pygame.display.update()
        
def nextLvl(SCREEN, BACKGROUND1, BACKGROUND2, balls, lvl):
    """
        Function responsible for displaying the next level screen after a person
        completes a level
        :param screen: passes the pygame screen
        :param BACKGROUND1: passes background 1 for redraw
        :param BACKGROUND2: passes background 2 for redraw
        :param balls: passes the number of balls to start the next level at
        :param lvl: passes the number for the level display
    """
    pause = True
    WHITE = pygame.Color(250, 250, 250)
    
    SCREEN.fill(WHITE)
    SCREEN.blit(BACKGROUND1,(0,0))
    SCREEN.blit(BACKGROUND2,(60,50)) # position 60, 50
    
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    main(balls, lvl)
                    


        draw_text(SCREEN, "Congratulations!", 320, 230)
        draw_text(SCREEN, "Press Space Bar for the next level.", 240, 250)
        
        pygame.display.update()   
    
def start(SCREEN, BACKGROUND1, BACKGROUND2):
    """
        Function responsible for displaying the start screen of the game
        :param screen: passes the pygame screen
        :param BACKGROUND1: passes background 1 for redraw
        :param BACKGROUND2: passes background 2 for redraw
    """
    pause = True
    WHITE = pygame.Color(250, 250, 250)
    
    SCREEN.fill(WHITE)
    SCREEN.blit(BACKGROUND1,(0,0))
    SCREEN.blit(BACKGROUND2,(60,50)) # position 60, 50
    
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return
                    


        draw_text(SCREEN, "Welcome to A-Ball!", 290, 230)
        draw_text(SCREEN, "Press Space to begin.", 280, 250)
        
        pygame.display.update()
        
if __name__ == "__main__":
#     window_size = (750, 533)
#     SCREEN = pygame.display.set_mode(window_size)
#     start(SCREEN, getB1())
    main(2, 1)