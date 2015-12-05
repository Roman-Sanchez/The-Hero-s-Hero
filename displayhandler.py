
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
                self.updatePlayer(screen, player)
                pygame.display.flip()

    def updatePlayer(self, screen, player):

    	screen.blit(player.image, (player.left, player.top),
    		(int(player.imageData.imagesCoors[player.currentImage]['xCoor']), 
			int(player.imageData.imagesCoors[player.currentImage]['yCoor']),
			int(player.imageData.imagesCoors[player.currentImage]['width']), 
			int(player.imageData.imagesCoors[player.currentImage]['height'])))
