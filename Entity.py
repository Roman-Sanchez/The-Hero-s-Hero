import pygame
import math
from spriteSheet import SpriteSheet
from pygame import *

class Entity(Rect):
    def __init__(self):
        self.velX = 0
        self.velY = 0
        self.hasPhysics = True
        self.onGround = False
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#FF0000"))
        self = Rect(0, 0, 32, 32)

    def __init__(self, imageFilename):
        self.velX = 0
        self.velY = 0
        self.hasPhysics = True
        self.onGround = False
        self.imageFilename = imageFilename
        self.characterSkin = SpriteSheet(self.imageFilename)
    '''
    def __init__(self, x,y ,velx, vely, isStatic, image):
        self.velX = velx
        self.velY = vely
        self.hasPhysics = isStatic
        self.onGround = False
        self.image = image
        self.rect = Rect(x, y, 32, 32)
    '''
