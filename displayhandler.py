
import pygame
from pygame import *

import keyhandler
from heroeshero import kh


class DisplayHandler:
    def __init__(self):
        self.bg = Surface((800, 640))
        self.bg.convert()
        self.bg.fill(Color("#0000FF"))

    def update(self,screen, player, mh):
                # pygame.draw.rect(player.image,Color("#FFFF00"), player, 0)
                screen.blit(self.bg, (0, 0))
                self.updatePlayer(screen, player)
                #screen.blit(player.image, (player.left, player.top))
                solid = Surface((32, 32))
                solid.convert()
                solid.fill(Color("#00FFFF"))
                if (not kh.check_world()):
                    for tile in mh.map_a:
                        screen.blit(solid,(tile.locX,tile.locY ))
                else:
                    for tile in mh.map_b:
                        screen.blit(solid,(tile.locX,tile.locY ))
                        print "B "
                pygame.display.flip()

    def updatePlayer(self, screen, player):

        screen.blit(player.characterSkin.image, (player.left, player.top),
    		(int(player.characterSkin.imageData.imagesCoors[player.characterSkin.currentImage]['xCoor']) / 2,
			int(player.characterSkin.imageData.imagesCoors[player.characterSkin.currentImage]['yCoor']) / 2,
			int(player.characterSkin.imageData.imagesCoors[player.characterSkin.currentImage]['width']) / 2,
			int(player.characterSkin.imageData.imagesCoors[player.characterSkin.currentImage]['height']) / 2))
