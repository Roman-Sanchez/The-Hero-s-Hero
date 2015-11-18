import pygame
from pygame import *

import keyhandler

DISPLAY = (800, 640)
DEPTH = 32
FLAGS = 0


def main():
    print "main"
    pygame.init()
    screen = display.set_mode(DISPLAY, FLAGS, DEPTH)
    display.set_caption("Use arrows to move!")
    timer = time.Clock()
    bg = Surface((32, 32))
    bg.convert()
    bg.fill(Color("#000000"))
    print "before loop"
    done = False
    while not done:
        timer.tick(60)
        pygame.display.flip()
        done = keyhandler.key_update()
    pygame.quit()

if __name__ == "__main__":
    main()