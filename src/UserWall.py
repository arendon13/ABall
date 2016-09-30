'''
Created on May 29, 2015

@author: Adrian
'''
import pygame
import math


class UserWall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, h_walls_list, v_walls_list, ver, hor, setx, sety):
        """
            Creates a user wall object to display on the screen. The user wall
            will be fully drawn if there is no ball collision while drawing, if
            there is then it will be destroyed
            :param x: x location of user wall origin
            :param y: y location of user wall origin
            :param width: initial width of user wall
            :param height: initial height of user wall
            :param color: color of the wall
            :param h_walls_list: list of horizontal walls for collision
            :param v_walls_list: list of vertical walls for collision
            :param ver: boolean to state if the user wall is a vertical wall
            :param hor: boolean to state if the user wall is a horizontal wall
            :param setx: x location that will be set to draw appropriate user wall
            :param sety: y location that will be set to draw appropriate user wall
            
        """
        # Call the parent's constructor
        super().__init__()
 
        self.color = color
        self.width = width
        self.height = height
        # Make a black wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.h_walls = h_walls_list
        self.v_walls = v_walls_list
        
        self.ver = ver
        self.hor = hor
#         self.wasVer = none
#         self.wasHor = not
        
        if self.ver:
            self.wasVer = True
            self.wasHor = False
        else:
            self.wasHor = True
            self.wasVer = False
        
        self.setx = setx
        self.sety = sety
        
        self.isDead = False
        self.isDrawing = True
        
        self.isExpanding = True
        self.finalWidth = 0
        self.finalHeight = 0
        self.finalX = 0
        self.finalY = 0
        
    def setWidth(self, inc):
        """
            Responsible for incrementing the width of the user wall
            :param inc: integer that states the amount to be incremented by
            
        """
        self.width += inc
        self.rect = self.rect.inflate(inc, 0)
        self.setX(self.setx)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        print("height: %s, width: %s, x: %s, y: %s " % (self.height, self.width,
              self.rect.x, self.rect.y))
        
    def setHeight(self, inc):
        """
            Responsible for incrementing the height of the user wall
            :param inc: integer that states the amount to be incremented by
            
        """
        self.height += inc
        self.rect = self.rect.inflate(0, inc)
        self.setY(self.sety)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        print("height: %s, width: %s, x: %s, y: %s " % (self.height, self.width,
              self.rect.x, self.rect.y))
        
    def setY(self, newY):
        """
            Responsible for changing the initial y value
            :param newY: the new value for the y location
        """
        self.rect.y = newY
    def setX(self, newX):
        """
            Responsible for changing the initial x value
            :param newY: the new value for the x location
        """
        self.rect.x = newX
        
    def update(self, balls, powerUps):
        """
            Responsible testing whether the user wall collides with horizontal 
            walls, vertical walls, or ball. 
            :param balls: list of balls to test for wall to ball collision
            :param powerUps: list of powerUps to test for wall to powerUps collision
        """
 
        # Did this update cause us to hit a horizontal wall?
        count = 0
        tb_hit_list = pygame.sprite.spritecollide(self, self.h_walls, False)
        if len(tb_hit_list)> 0 and self.ver:
            for newWall in tb_hit_list:
                count += 1
                if count == 1:
                    self.ver = False
                    self.isDrawing = False
                    self.finalWidth = self.width
                    self.finalHeight = self.height
                    self.finalX = self.rect.x
                    self.finalY = self.rect.y
                    break
        
        count = 0
        lr_hit_list = pygame.sprite.spritecollide(self, self.v_walls, False)
        if len(lr_hit_list)>0 and self.hor:
            for newWall in lr_hit_list:
                count += 1
                if count == 1:
                    self.hor = False
                    self.isDrawing = False
                    self.finalWidth = self.width
                    self.finalHeight = self.height
                    self.finalX = self.rect.x
                    self.finalY = self.rect.y
                    break
        
        if self.isDrawing:
            ball_hit_list = pygame.sprite.spritecollide(self, balls, False)
            for newWall in ball_hit_list:
                self.selfDestruct()
                self.isDead = True
                
        # increment vertical wall height
        if self.ver:
            self.setHeight(3)
        # increment horizontal wall width
        if self.hor:
            self.setWidth(3)            

    def getIsDrawing(self):
        """
            Returns true if the wall is currently being drawn, false if its not
        """
        return self.isDrawing
    
    def selfDestruct(self):
        """
            Kills the wall which removes it from the pygroup 
        """
        pygame.sprite.Sprite.kill(self)
        
    def getArea(self):
        """
            Returns the area of space that the wall is taking up based on width 
            and height
        """
        if self.isDrawing is False:
            #360 height, 
            if self.wasVer:
                length = math.floor(self.finalHeight / 21)
                width = 1
                area = length * width
                return area
            if self.wasHor:
                length = 1
                width = math.floor(self.finalWidth / 21)
                area = length * width
                return area
    
#     def 