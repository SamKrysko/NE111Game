from constants import *
from pygame import *


class Wall(sprite.Sprite):
    #initiallizing the walls
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x*TILESIZE, y*TILESIZE)
        self.x = x
        self.y = y

    #makes the wall coordinates into actual sprite properties
    def make_cam_pos(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE