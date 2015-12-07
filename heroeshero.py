import pygame
from pygame import *

import displayhandler
import keyhandler
import json
from Entity import Entity
from MapHandler import MapHandler

DISPLAY = (800, 640)
DEPTH = 32
FLAGS = 0


def main():
    print "main"
    pygame.init()
    screen = display.set_mode(DISPLAY, FLAGS, DEPTH)
    display.set_caption("Use arrows to move!")
    timer = time.Clock()
    dh = displayhandler.DisplayHandler()
    kh = keyhandler.KeyHandler()
    #player = Entity()
    mh = MapHandler()
    player = SpriteSheet("sprites\OptimizedSprites\\nerdOp.png")
    #MapHandler.load('map1.txt','map1b.txt')



    print "before loop"
    done = False
    while not done:
        timer.tick(60)
        dh.update(screen, player, mh)
        done = kh.key_update()
        kh.update_player(player, 5)

    pygame.quit()

if __name__ == "__main__":
    main()