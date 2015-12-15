import pygame
from pygame import *

movementSpeed = 3

class KeyHandler:
    def __init__(self):
        self.kup = False
        self.kdown = False
        self.kleft = False
        self.kright = False
        self.kworld_swap = True
        self.keyUp = False




    def key_update(self):
        self.keyUp = False
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
                #print "*****", (self.kworld_swap), "*****\n"


            if e.type == KEYUP and e.key == K_UP:
                self.kup = False
                self.keyUp = True
            if e.type == KEYUP and e.key == K_DOWN:
                self.kdown = False
                self.keyUp = True
            if e.type == KEYUP and e.key == K_LEFT:
                self.kleft = False
                self.keyUp = True
            if e.type == KEYUP and e.key == K_RIGHT:
                self.kright = False
                self.keyUp = True
            if e.type == pygame.QUIT:
                return True

        return False

    def check_world(self):
        #print self.kworld_swap
        if(self.kworld_swap):
            return True
        else:
            return False


    def update_player(self, player, max_vel):
        
        playerMoved = False
        movementDirection = "Right"

        if self.kup: #and player.onGround:
            player.move_ip(0,-movementSpeed)

            player.velY += movementSpeed
            movementDirection = "Up"
            playerMoved = True

        if self.kright:
            # player.move(5,0)
            player.move_ip(movementSpeed,0)
            player.velX += movementSpeed
            movementDirection = "Right"
            playerMoved = True
            
        if self.kleft:
            player.move_ip(-movementSpeed,0)
            player.velX += -movementSpeed
            movementDirection = "Left"
            playerMoved = True
            
        if self.kdown:
            # player.move(5,0)
            player.move_ip(0,movementSpeed)
            player.velY += -movementSpeed
            movementDirection = "Down"
            playerMoved = True
            
        if (playerMoved):
            player.characterSkin.updateCurrentImage()

            # updates animation based off the movement
            player.characterSkin.setAnimation(movementDirection)
            player.characterSkin.setImageCoors(movementDirection)

        if (self.keyUp):
            player.characterSkin.resetCurrentImage()


    
