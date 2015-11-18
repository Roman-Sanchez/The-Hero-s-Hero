import pygame
import math
from pygame import *


class Entity():
    def __init__(self):
        self.locX = 0
        self.locY = 0
        self.velX = 0
        self.velY = 0
        self.hasPhysics = True
        self.onGround = False
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#FF0000"))
        self.rect = Rect(self.locX, self.locY, 32, 32)

    def __init__(self, x,y ,velx, vely, isStatic, image):
        self.locX = x
        self.locY = y
        self.velX = velx
        self.velY = vely
        self.hasPhysics = isStatic
        self.onGround = False
        self.image = image
        self.rect = Rect(self.locX, self.locY, 32, 32)