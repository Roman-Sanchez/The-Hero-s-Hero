
import pygame
from pygame import *

import keyhandler
from heroeshero import kh


class DisplayHandler:
    def __init__(self):
        self.bg = Surface((800, 640))
        self.bg.convert()
        self.bg.fill(Color("#0000FF"))

    def update(self,screen, player, mh, kh):

                screen.blit(self.bg, (0, 0))
                self.updatePlayer(screen, player)
                solid = Surface((32, 32))
                solid.convert()
                solid.fill(Color("#00FFFF"))

                # Will check to see if the world needs to be swapped and will display the appropriate map
                if (kh.kworld_swap == True):
                    for tile in mh.map_a:
                        screen.blit(solid,(tile.locX,tile.locY ))
                elif (kh.kworld_swap == False):
                    for tile in mh.map_b:
                        screen.blit(solid,(tile.locX,tile.locY ))

                pygame.display.flip()

    def updatePlayer(self, screen, player):

        screen.blit(player.characterSkin.image, (player.left, player.top),
    		(int(player.characterSkin.imageData.imagesCoors[player.characterSkin.currentImage]['xCoor']) / 2,
			int(player.characterSkin.imageData.imagesCoors[player.characterSkin.currentImage]['yCoor']) / 2,
			int(player.characterSkin.imageData.imagesCoors[player.characterSkin.currentImage]['width']) / 2,
			int(player.characterSkin.imageData.imagesCoors[player.characterSkin.currentImage]['height']) / 2))
