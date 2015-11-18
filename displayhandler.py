
import pygame
from pygame import *


class DisplayHandler:
    def __init__(self):
        self.bg = Surface((800, 640))
        self.bg.convert()
        self.bg.fill(Color("#0000FF"))

    def update(self,screen, player):
                # pygame.draw.rect(player.image,Color("#FFFF00"), player, 0)
                screen.blit(self.bg, (0, 0))
                screen.blit(player.image, (player.left, player.top))
                pygame.display.flip()
