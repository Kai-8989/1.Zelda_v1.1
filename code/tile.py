import pygame
from support import *
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, pos, surface = pygame.Surface((48, 48))):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate((0, 0))