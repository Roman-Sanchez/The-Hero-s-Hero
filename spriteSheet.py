import pygame
from xmlParser import XmlSpriteParser

class SpriteSheet(object):

    def __init__(self, imageFileName):

        self.imageFileName = imageFileName
        self.image = pygame.transform.scale(pygame.image.load(self.imageFileName), (128, 64))
        #self.image = pygame.image.load(self.imageFileName)
        self.xmlFileName = self.replaceFileExtension(self.imageFileName)

        # gets the x, y coordinates and the width and height for each sprite in
        # the sprite sheet
        self.imageData = XmlSpriteParser(self.replaceFileExtension(imageFileName))

        # this must be 1 less because the dictionary is indexed starting at 0
        # if there is 17 images, then the dictionary index is 0 - 16
        self.numImages = self.imageData.numImages - 1
        self.currentImage = 0

        # controls the rate at which the animation is performed. The higher the
        # number the slower the animation.
        self.animationRate = 10

        # will increment and when it is the number that the animationRate is the
        # currentImage will be incremented to the next image.
        self.animationCounter = 0

    def getImageData(self, fileName):
        self.fileName(self.fileName)

    # Replaces the file extension with .sprites
    def replaceFileExtension(self, fileName):

        # Note: need to implement other file types
        try:
            self.fileName = fileName.replace('.png', '.sprites')
            return self.fileName
        except Exception:
            print ("Wrong file type\n")

    def updateCurrentImage(self):

        if (self.animationRate == self.animationCounter):
            if (self.currentImage < self.numImages):
                self.currentImage += 1
            else:
                self.currentImage = 0
            self.animationCounter = 0

        self.animationCounter = self.animationCounter + 1


'''
# test code
tmp = SpriteSheet("sprites\OptimizedSprites\TetrisPiecesOp.png")
print tmp.imageFileName
print tmp.xmlFileName
print tmp.imageData.imagesCoors[1]
'''
