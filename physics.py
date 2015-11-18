import pygame
from pygame import *

def apply_physics(static, dynamic):

    if coll_check(static, dynamic):
        print "collision!"
        clipping = static.clip(dynamic)
        if clipping.left > dynamic.left:
            dynamic.move(-clipping.left,0)
        else:
            dynamic.move(clipping.left,0)
        if clipping.op > dynamic.top:
            dynamic.move(0,-clipping.top)
        else:
            dynamic.move(0,clipping.top)


def coll_check(entity1, entity2):
    if entity1.colliderect(entity2):
        return True
    else:
        return False

def coll_check(entity1, tile):
        if entity1.colliderect(tile):
            return True
        else:
            return False