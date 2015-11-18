import pygame
import math
from pygame import *

DISPLAY = (800, 640)
DEPTH = 32
FLAGS = 0


# in blocks, 25 x 20

def main():
    pygame.init()
    screen = display.set_mode(DISPLAY, FLAGS, DEPTH)
    display.set_caption("Use arrows to move!")
    timer = time.Clock()

    up = down = left = right = False
    bg = Surface((32, 32))
    bg.convert()
    bg.fill(Color("#000000"))
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []

    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPP",
        "P  P                    P",
        "P  PPPPPP               P",
        "P  P     P    P         P",
        "P  P      P   P         P",
        "P  P       P  P         P",
        "P  P         PP    PPPPPP",
        "P  P          P         P",
        "P  P          P         P",
        "P  P          PPPPPP    P",
        "P  P          PP        P",
        "P  P          PPP      PP",
        "P  PPPPPPPPPPPPPPP    PPP",
        "P             PPPPP  PPPP",
        "P             P         P",
        "P  PPPPPPPPPPPP         P",
        "P          PP P         P",
        "P       PP    P         P",
        "P      PPPP   PE        P",
        "PPPPPPPPPPPPPPPPPPPPPPPPP", ]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y, 1)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            x += 32
        y += 32
        x = 0

        #Level 2 initilization
        entities2 = pygame.sprite.Group()
        platforms2 = []
        x2 = y2 = 0
    level2 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPP",
        "P  P                    P",
        "P  PPPPPP               P",
        "P  P     P    P         P",
        "P  P      P   P         P",
        "P  P       P  P         P",
        "P  P         PP    PPPPPP",
        "P  P        P P         P",
        "P  P       P  P         P",
        "P  P      P   PPPPPP    P",
        "P  P     P    PP        P",
        "P  P PP       PPP      PP",
        "P  PPPPP      PPPP    PPP",
        "P       P     PPPPP  PPPP",
        "P        PP   P         P",
        "P            PP         P",
        "P          PP P         P",
        "P       PPPPP P         P",
        "PPPPPPPPPPPPPPPE        P",
        "PPPPPPPPPPPPPPPPPPPPPPPPP", ]
    # build the level

    for row in level2:
        for col in row:
            if col == "P":
                # if level[row][col] == "P":
                #    p = Platform(x2, y2, 3)
                # else:
                p = Platform(x2, y2, 2)
                platforms2.append(p)
                entities2.add(p)
            if col == "E":
                e = ExitBlock(x2, y2)
                platforms2.append(e)
                entities2.add(e)
            x2 += 32
        y2 += 32
        x2 = 0

        # end level intersect initialization
        eIntersect = pygame.sprite.Group()
        platintersect = []
        x3 = y3 = 0
    levintersect = [
        "PPPPPPPPPPPPPPPPPPPPPPPPP",
        "P  P                    P",
        "P  PPPPPP               P",
        "P  P     P    P         P",
        "P  P      P   P         P",
        "P  P       P  P         P",
        "P  P         PP    PPPPPP",
        "P  P          P         P",
        "P  P          P         P",
        "P  P          PPPPPP    P",
        "P  P          PP        P",
        "P  P          PPP      PP",
        "P  PPPPP      PPPP    PPP",
        "P             PPPPP  PPPP",
        "P             P         P",
        "P            PP         P",
        "P          PP P         P",
        "P       PP    P         P",
        "P      PPPP   PE        P",
        "PPPPPPPPPPPPPPPPPPPPPPPPP", ]
    # build the level

    for row in levintersect:
        for col in row:
            if col == "P":
                # if level[row][col] == "P":
                #    p = Platform(x2, y2, 3)
                # else:
                p = Platform(x3, y3, 4)
                platintersect.append(p)
                eIntersect.add(p)
            x3 += 32
        y3 += 32
        x3 = 0

        # end level intersect initialization


    entities3 = pygame.sprite.Group()
    entities3.add(player)

    done = False
    while not done:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                done = True
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                done = True
            if e.type == KEYDOWN and e.key == K_UP or e.type == KEYDOWN and e.key == K_z:
                up = True
            if e.type == KEYDOWN and e.key == K_x:
                pass
                # down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_UP or e.type == KEYUP and e.key == K_z:
                up = False
            if e.type == KEYUP and e.key == K_x:
                if not player.coll_check(1,platforms) and not player.coll_check(-1,platforms):
                    down = not down
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == pygame.QUIT:
                done = True

        # draw background
        for y in range(20):
            for x in range(25):
                screen.blit(bg, (x * 32, y * 32))

        # update player, draw everything else
        if down:
            player.update(up, down, left, right, platforms2)
            entities.draw(screen)
            s = pygame.Surface((1000,750))  # the size of your rect
            s.set_alpha(100)                # alpha level
            s.fill((0,0,0))           # this fills the entire surface
            screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
            entities2.draw(screen)


        else:
            player.update(up, down, left, right, platforms)
            entities2.draw(screen)
            s = pygame.Surface((1000,750))  # the size of your rect
            s.set_alpha(128)                # alpha level
            s.fill((0,0,0))           # this fills the entire surface
            screen.blit(s, (30,30))    # (0,0) are the top-left coordinates
            entities.draw(screen)

        entities3.draw(screen)
        eIntersect.draw(screen)
        pygame.display.flip()

    pygame.quit()

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)



class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#FF0000"))
        self.rect = Rect(x, y, 32, 32)

    def update(self, up, down, left, right, platforms):
        if up:
            # only jump if on the ground
            if self.onGround:
                self.yvel -= 10
        if down:
            pass
        if left:
            self.xvel = -5
        if right:
            self.xvel = 5
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.5
            # max falling speed
            if self.yvel > 30:
                self.yvel = 30
        if not (left or right):
            self.xvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    event.post(event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def coll_check(self, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                print "collision!"
                return True
            else:
                print "No collision!"
                return False


class Platform(Entity):
    def __init__(self, x, y, white):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        if white == 1:
            self.image.fill(Color("#FFFF44"))
        if white == 2:
            self.image.fill(Color("#4444FF"))
        if white == 3:
            self.image.fill(Color("#FF44FF"))
        if white == 4:
            self.image.fill(Color("#FFFFFF"))
        self.rect = Rect(x, y, 32, 32)



    def update(self):
        pass


class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y, 1)
        self.image.fill(Color("#0033FF"))


if __name__ == "__main__":
    main()
