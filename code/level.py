import pygame
from config import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        self.player = None
        self.tile = None
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.display_surf = pygame.display.get_surface()
        self.creating_sprites()

    def creating_sprites(self):
        self.tile = Tile([self.visible_sprites, self.obstacle_sprites], (500, 100), 'invisible')
        self.player = Player([self.visible_sprites, self.obstacle_sprites], (520, 300))

    def update(self):
        self.visible_sprites.update()

    def draw(self):
        self.visible_sprites.draw(self.display_surf)

    def run(self):
        self.draw()
        self.update()
