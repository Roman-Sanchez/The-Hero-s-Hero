from pygame import *


class Tile(Rect):
    def __init__(self, locx=0, locy=0, material = 1):
        self.locX = locx
        self.locY = locy

        self.material = material

        super( Tile, self).__init__(self.locX, self.locY, 32, 32)
