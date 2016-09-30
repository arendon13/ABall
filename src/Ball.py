'''
Created on May 6, 2015

@author: Adrian
'''
import pygame
from pygame.locals import *

#Derive your class from the Sprite super class
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, h_walls_list, v_walls_list):
        """
            Creates a new ball object to display on the screen
            :param x: x location of ball origin
            :param y: y location of ball origin
            :param vx: velocity of the ball in the x direction
            :param vy: velocity of the ball in the y direction
            :param h_walls_list: list of pygroup horizontal walls for collisions
            :param v_walls_list: list of pygroup vertical walls for collisions
        """
        # Don't forget to call the super constructor
        super().__init__();
        self.image = pygame.image.load("white_ball.png").convert()

        # Set the color that should be transparent
#         self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.image.set_colorkey(pygame.Color(255, 255, 255))

        # Required for collision detection
        # HINT: You will need this for the lab
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy
        
        self.h_walls = h_walls_list
        self.v_walls = v_walls_list
        
    def changeVelocity(self, dx, dy):
        """
            Responsible for changing ball velocity when it gains a powerup
            :param dx: passes the velocity in the x direction that will be added
            :param dy: passes the velocity in the y direction that will be added
        """
        vxNeg = False
        vyNeg = False
        if self.vx < 0:
            vxNeg = True
        if self.vy < 0:
            vyNeg = True
            
        if vxNeg:
            self.vx = self.vx * -1
            self.vx = self.vx + dx
            self.vx = self.vx * -1
        else:
            self.vx = self.vx + dx
        
        if vyNeg:
            self.vy = self.vy * -1
            self.vy = self.vy + dy
            self.vy = self.vy * -1 
        else:
            self.vy = self.vy + dy
        
    def update(self, balls, powerUps):
        """
            Responsible updating the current ball position and testing whether it 
            collides with powerups, horizontal walls, or vertical walls
            :param balls: list of balls to test for ball to ball collision
            :param powerUps: list of powerUps to test for ball to powerUps collision
        """
        # Move up/down
        self.rect.y += self.vy
        # Move left/right
        self.rect.x += self.vx
 
        # Did this update cause us to hit a wall?
        tb_hit_list = pygame.sprite.spritecollide(self, self.h_walls, False)
        for ball in tb_hit_list:
            self.vy *= -1
            
        lr_hit_list = pygame.sprite.spritecollide(self, self.v_walls, False)
        for ball in lr_hit_list:
            self.vx *= -1
        
#         # Did this update cause us to hit another ball?
#         ball_hit_list = pygame.sprite.spritecollide(self, balls, False)
#         for ball in ball_hit_list:
#             self.vx *= -1
#             ball.vx *= -1
            
        powerUp_list = pygame.sprite.spritecollide(self, powerUps, True)
        for pup in powerUp_list:
            if pup.speedUp:
                self.changeVelocity(1, 1)
            if pup.slowDown:
                self.changeVelocity(-1, -1)
                
        collisionList = pygame.sprite.spritecollide(self, balls, False)
        for c in collisionList: #if two edges are barely overlapping, then the two objects are colliding on those edges
            if (0 < self.rect.y - c.rect.y + c.image.get_height() <= 5) or (0 < self.rect.y + self.image.get_height() - c.rect.y <= 5):
                self.vy *= -1 #if collide, undo the move in the collion's direction
                self.rect.y += 2*self.vy
                c.vy *= -1 #change the direction of the other sprite, prevents collision when c moves
            if (0 < self.rect.x - c.rect.x + c.image.get_width() <= 5) or (0 < self.rect.x + self.image.get_width() - c.rect.x <= 5):
                self.vx *= -1
                self.rect.x += 2*self.vx
                c.vx *= -1
                
                