'''
Created on May 6, 2015

@author: Adrian
'''
import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        """
            Creates a new main wall object to display on the screen. 
            There are only four main walls in the game
            :param x: x location of wall origin
            :param y: y location of wall origin
            :param width: width of wall
            :param height: height of wall
            :param color: color of the wall
        """
        # Call the parent's constructor
        super().__init__()
 
        # Make a black wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        