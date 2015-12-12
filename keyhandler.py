import pygame
from pygame import *

movementSpeed = 3

class KeyHandler:
    def __init__(self):
        self.kup = False
        self.kdown = False
        self.kleft = False
        self.kright = False
        self.kworld_swap = True;




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
            if e.type == KEYDOWN and e.key == K_z:
                self.kworld_swap = not self.kworld_swap
                print "*****", (self.kworld_swap), "*****\n"


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

    def check_world(self):
        print self.kworld_swap
        if(self.kworld_swap):
            print "true!"
            return True
        else:
            return False


    def update_player(self,player, max_vel):
        
        playerMoved = False

        if self.kup: #and player.onGround:
            player.top += -movementSpeed
            player.velY += movementSpeed
            playerMoved = True

        if self.kright:
            # player.move(5,0)
            player.left += movementSpeed
            player.velX += movementSpeed
            playerMoved = True
            
        if self.kleft:
            player.left += -movementSpeed
            player.velX += -movementSpeed
            playerMoved = True
            
        if self.kdown:
            # player.move(5,0)
            player.top += movementSpeed
            player.velY += -movementSpeed
            playerMoved = True
            
        if (playerMoved):
            player.characterSkin.updateCurrentImage()


    
