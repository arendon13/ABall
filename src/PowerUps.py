'''
Created on May 29, 2015

@author: Adrian
'''
import pygame
from pygame.locals import *

#Derive your class from the Sprite super class
class PowerUps(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, h_walls_list, v_walls_list, url, speedUp, slowDown):
        """
            Creates a power up object to increase or decrease ball speed
            :param x: x location of power up origin
            :param y: y location of power up origin
            :param vx: velocity of the power up in the x direction
            :param vy: velocity of the power up in the y direction
            :param h_walls_list: list of pygroup horizontal walls for collisions
            :param v_walls_list: list of pygroup vertical walls for collisions
            :param url: url for power up pictures
            :param speedUp: boolean that signals speeding up of the power ups
            :param slowDown: boolean that signals slowing down of the power ups
            
        """
        # Don't forget to call the super constructor
        super().__init__();
        self.image = pygame.image.load(url).convert()

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
        self.speedUp = speedUp
        self.slowDown = slowDown
        
        self.h_walls = h_walls_list
        self.v_walls = v_walls_list
        
    def update(self, balls, powerUps):
        """
            Responsible testing whether the power ups collide with horizontal 
            walls, vertical walls, or ball. 
            :param balls: list of balls to test for powerUp to ball collision
            :param powerUps: list of powerUps to test for powerUp to powerUps collision
        """
        # Move up/down
        self.rect.y += self.vy
        # Move left/right
        self.rect.x += self.vx
 
        # Did this update cause us to hit a wall?
        tb_hit_list = pygame.sprite.spritecollide(self, self.h_walls, False)
        for p in tb_hit_list:
            self.vy *= -1
            
        lr_hit_list = pygame.sprite.spritecollide(self, self.v_walls, False)
        for p in lr_hit_list:
            self.vx *= -1
            
        collisionList = pygame.sprite.spritecollide(self, powerUps, False)
        for c in collisionList: #if two edges are barely overlapping, then the two objects are colliding on those edges
            if (0 < self.rect.y - c.rect.y + c.image.get_height() <= 10) or (0 < self.rect.y + self.image.get_height() - c.rect.y <= 10):
                self.vy *= -1 #if collide, undo the move in the collion's direction
                self.rect.y += 2*self.vy
                c.vy *= -1 #change the direction of the other sprite, prevents collision when c moves
            if (0 < self.rect.x - c.rect.x + c.image.get_width() <= 10) or (0 < self.rect.x + self.image.get_width() - c.rect.x <= 10):
                self.vx *= -1
                self.rect.x += 2*self.vx
                c.vx *= -1
                
                