import pygame
from xmlParser import XmlSpriteParser

class SpriteSheet(object):

    def __init__(self, imageFileName):

        self.imageFileName = imageFileName

        #self.image = pygame.image.load(self.imageFileName)
        #self.xmlFileName = self.replaceFileExtension(self.imageFileName)

        # Other animation filenames, initialized to nothing but later changed to their appropriate names
        self.walkLeftFileName = ""
        self.walkUpFileName = ""
        self.walkDownFileName = ""
        self.getOtherImageNames(imageFileName)

        # assuming that the filename passed in is the walkRight animation the walkRightImage is set
        # to the imageFileName variable that is passed into the current instance object
        self.walkRightImage = pygame.transform.scale(pygame.image.load(self.imageFileName), (128, 64))
        self.walkLeftImage = pygame.transform.scale(pygame.image.load(self.walkLeftFileName), (128, 64))
        self.walkUpImage = pygame.transform.scale(pygame.image.load(self.walkUpFileName), (128, 64))
        self.walkDownImage = pygame.transform.scale(pygame.image.load(self.walkDownFileName), (128, 64))

        # gets the x, y coordinates and the width and height for each sprite in
        # the sprite sheet
        self.imageData = XmlSpriteParser(self.replaceFileExtension(imageFileName))

        # Variables that hold that various animation coordinates. Each one is an XmlSpriteParser
        self.walkDownImageData = XmlSpriteParser(self.replaceFileExtension(self.walkDownFileName))
        self.walkRightImageData = XmlSpriteParser(self.replaceFileExtension(self.imageFileName))
        self.walkLeftImageData = XmlSpriteParser(self.replaceFileExtension(self.walkLeftFileName))
        self.walkUpImageData = XmlSpriteParser(self.replaceFileExtension(self.walkUpFileName))

        self.animation = pygame.transform.scale(pygame.image.load(self.imageFileName), (128, 64))

        # this must be 1 less because the dictionary is indexed starting at 0
        # if there is 17 images, then the dictionary index is 0 - 16
        self.numImages = self.imageData.numImages - 1
        self.currentImage = 0

        # controls the rate at which the animation is performed. The higher the
        # number the slower the animation.
        self.animationRate = 5

        # will increment and when it is the number that the animationRate is the
        # currentImage will be incremented to the next image.
        self.animationCounter = 0

    # Based off what direction the player is moving will determine what coordinate data is selected
    def setImageCoors(self, direction):
        if (direction == "Right"):
            self.imageData = self.walkRightImageData
        elif (direction == "Left"):
            self.imageData = self.walkLeftImageData
        elif (direction == "Up"):
            self.imageData = self.walkUpImageData
        elif (direction == "Down"):
            self.imageData = self.walkDownImageData

    # Based off what direction the player is moving will determine what animation is selected
    def setAnimation(self, direction):
        if (direction == "Right"):
            self.animation = self.walkRightImage
        elif (direction == "Left"):
            self.animation = self.walkLeftImage
        elif (direction == "Up"):
            self.animation = self.walkUpImage
        elif (direction == "Down"):
            self.animation = self.walkDownImage

    # Creates the other filenames for the other movement directions
    def getOtherImageNames(self, filename):
        self.walkLeftFileName = filename.replace('Op.png', 'OpWL.png')
        self.walkUpFileName = filename.replace('Op.png', 'OpUp.png')
        self.walkDownFileName = filename.replace('Op.png', 'OpDown.png')

    # Replaces the file extension with .sprites
    def replaceFileExtension(self, fileName):

        coordinateFileName = fileName.replace('.png', '.sprites')
        return coordinateFileName

    # This increments the animationCounter and controls when the next image in the sprite sheet should be displayed
    def updateCurrentImage(self):

        if (self.animationRate == self.animationCounter):
            if (self.currentImage < self.numImages):
                self.currentImage += 1
            else:
                self.currentImage = 0
            self.animationCounter = 0

        self.animationCounter = self.animationCounter + 1

    def resetCurrentImage(self):
        self.currentImage = 0