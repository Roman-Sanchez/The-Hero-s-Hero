from pygame import *


class Tile(Rect):
    def __init__(self):
        self.locX = 0
        self.locY = 0

        material = 1

        self.rect = Rect(self.locX, self.locY, 32, 32)
