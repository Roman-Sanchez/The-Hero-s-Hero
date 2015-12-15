import pygame
from pygame import *

def apply_physics(static, dynamic):
    if static.colliderect(dynamic):
        print "collision!"
        print "now"
        clipping = static.clip(dynamic)
        if clipping.left > dynamic.left:
            dynamic.move(-clipping.left,0)
        else:
            dynamic.move(clipping.left,0)
        if clipping.top > dynamic.top:
            dynamic.move(0,-clipping.top)
        else:
            dynamic.move(0,clipping.top)

