'''
Created on Jun 7, 2015

@author: Adrian
'''

import pygame

class FillWall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, h_walls_list, v_walls_list, fillR, fillB, setx, sety):
        """
            Creates a fill wall object to display on the screen. The fill wall
            object is meant to fill up the space where a ball is not located in
            order to help complete levels faster
            there is then it will be destroyed
            :param x: x location of fill wall origin
            :param y: y location of fill wall origin
            :param width: initial width of fill wall
            :param height: initial height of fill wall
            :param color: color of the wall
            :param h_walls_list: list of horizontal walls for collision
            :param v_walls_list: list of vertical walls for collision
            :param fillR: boolean to state if the fill wall is filling to the right
            :param fillB: boolean to state if the fill wall is filling to the left
            :param setx: x location that will be set to draw appropriate fill wall
            :param sety: y location that will be set to draw appropriate fill wall
            
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
        
        self.fillR = fillR
        self.fillB = fillB
        
        self.setx = setx
        self.sety = sety
        
        self.isDead = False
        self.isDrawing = True
       
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
            Responsible testing whether the fill wall collides with horizontal 
            walls, vertical walls, or ball. 
            :param balls: list of balls to test for wall to ball collision
            :param powerUps: list of powerUps to test for wall to powerUps collision
        """
        # increment vertical wall height
#         if self.fillB:
#             self.setHeight(3)
#         # increment horizontal wall width
#         print("%s, %s" % (self.fillB, self.fillR))
#         if self.fillR:
#             self.setWidth(3)
 
#         # Did this update cause us to hit a horizontal wall?
#         count = 0
#         tb_hit_list = pygame.sprite.spritecollide(self, self.h_walls, False)
#         if len(tb_hit_list)> 0 and self.fillB:
#             for newWall in tb_hit_list:
#                 print("top bottom collision")
#                 count += 1
#                 if count == 1:
#                     self.fillB = False
#                     break
        
        lr_hit_list = pygame.sprite.spritecollide(self, self.v_walls, False)
        while len(lr_hit_list) < 1 and self.fillR:
            print("right left collision")
            self.setWidth(3)
        
#         if self.isDrawing:
#             ball_hit_list = pygame.sprite.spritecollide(self, balls, False)
#             for newWall in ball_hit_list:
#                 self.selfDestruct()
#                 self.isDead = True
#                 self.isDrawing = False
                


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
        