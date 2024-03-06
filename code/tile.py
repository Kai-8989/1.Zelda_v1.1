import pygame
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, pos, sprite_type, surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        if self.sprite_type == 'invisible':
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
            self.rect = self.image.get_rect(topleft=pos)

        elif self.sprite_type == 'tree':
            self.image = pygame.image.load('../graphics/objects/04.png')
            self.rect = self.image.get_rect(topleft=pos)
            self.hitbox = self.rect.inflate(0, -60)

        else:
            self.image = surface
            self.rect = self.image.get_rect(topleft=pos)

