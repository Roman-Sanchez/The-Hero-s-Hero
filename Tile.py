from pygame import *


class Tile(Rect):
    def __init__(self, locx=0, locy=0, material = 1):
        self.locX = locx
        self.locY = locy

        self.material = material

        self.rect = Rect(self.locX, self.locY, 32, 32)
