import pygame
from pygame import *

def apply_physics(static, dynamic):
    if static.colliderect(dynamic):

        clipping = static.clip(dynamic)
        #clipping = dynamic.clip(static)
        '''if clipping.left > dynamic.left:
            dynamic.move(-clipping.left, 0)
            print "col right!"
        else:
            dynamic.move(clipping.left, 0)
            print "col left!"
        if clipping.top > dynamic.top:
            dynamic.move(0,-clipping.top)
            print "col top!"
        else:
            dynamic.move(0,clipping.top)
            print "col bottom!"'''

        if dynamic.velX > 0:
            dynamic.right = static.left
        if dynamic.velX < 0:
            dynamic.left = static.right
        if dynamic.velY > 0:
            dynamic.bottom = static.top
            dynamic.onGround = True
            dynamic.velY = 0
        if dynamic.velY < 0:
            dynamic.top = static.bottom
        if dynamic.velY != 0:
            dynamic.onGround = False
