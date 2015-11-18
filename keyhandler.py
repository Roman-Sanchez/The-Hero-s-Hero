import pygame
from pygame import *

up = down = left = right = False


def key_update():
    for e in pygame.event.get():
            if e.type == QUIT:
                return True
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return True
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                print "down!"
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == pygame.QUIT:
                return True
    return False
