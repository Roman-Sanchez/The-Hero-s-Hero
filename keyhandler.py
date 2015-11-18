import pygame
from pygame import *

class KeyHandler:
    def __init__(self):
        self.kup = False
        self.kdown = False
        self.kleft = False
        self.kright = False



    def key_update(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                return True
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return True
            if e.type == KEYDOWN and (e.key == K_UP or e.key == K_SPACE):
                self.kup = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                self.kdown = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                self.kleft = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                self.kright = True

            if e.type == KEYUP and e.key == K_UP:
                self.kup = False
            if e.type == KEYUP and e.key == K_DOWN:
                self.kdown = False
            if e.type == KEYUP and e.key == K_LEFT:
                self.kleft = False
            if e.type == KEYUP and e.key == K_RIGHT:
                self.kright = False
            if e.type == pygame.QUIT:
                return True
        return False

    def update_player(self,player, max_vel):

        if self.kup: #and player.onGround:
            player.top += -5
            player.velY += 10
        if self.kright:
            # player.move(5,0)
            player.left += 5
            player.velX += 5
        if self.kleft:
            player.left += -5
            player.velX += -5

        if self.kdown:
            # player.move(5,0)
            player.top += 5
            player.velY += -5