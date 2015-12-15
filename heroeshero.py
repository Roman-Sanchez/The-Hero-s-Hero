import pygame
from pygame import *

import displayhandler
import keyhandler
from Entity import Entity
from MapHandler import MapHandler
from physics import apply_physics

DISPLAY = (800, 640)
DEPTH = 32
FLAGS = 0
kh = keyhandler.KeyHandler()

def main():
    print "main"
    pygame.init()
    screen = display.set_mode(DISPLAY, FLAGS, DEPTH)
    display.set_caption("Use arrows to move!")
    timer = time.Clock()
    dh = displayhandler.DisplayHandler()
    #kh = keyhandler.KeyHandler()
    mh = MapHandler()
    player = Entity("sprites\OptimizedSprites\\nerdOp.png")
    #MapHandler.load('map1.txt','map1b.txt')

    print "before loop"
    done = False
    while not done:
        timer.tick(60)
        #print timer.get_fps(), "\n"
        dh.update(screen, player, mh, kh)
        done = kh.key_update()
        kh.update_player(player, 5)
        if kh.check_world():
            for tile in mh.map_b:
                apply_physics(tile, player)
        else:
            for tile in mh.map_a:
                apply_physics(tile, player)

    pygame.quit()

if __name__ == "__main__":
    main()