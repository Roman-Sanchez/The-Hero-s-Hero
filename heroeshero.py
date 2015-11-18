import pygame
from pygame import *

import displayhandler
import keyhandler
from Entity import Entity

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
    player = Entity()

    print "before loop"
    done = False
    while not done:
        timer.tick(60)
        dh.update(screen, player)
        done = kh.key_update()
        kh.update_player(player, 5)

    pygame.quit()

if __name__ == "__main__":
    main()