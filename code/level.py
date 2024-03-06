import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import import_csv_layout, import_forlder


class Level:
    def __init__(self):
        # get the display surface
        self.player = None
        self.tile = None
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = Custom_visible_group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map/map_FloorBlocks_FloorBlocks.csv')
        }
        graphics = {
            'grass': import_forlder('../graphics/grass')
        }
        # for style, layout in layouts.items():
        #     for row_index, row in enumerate(layout):
        #         for col_index, col in enumerate(row):
        #             if col != '-1':
        #                 x = col_index * TILESIZE
        #                 y = row_index * TILESIZE
        #                 if style == 'boundary':
        #                     Tile((x, y), [self.obstacle_sprites], 'invisible')

        self.player = Player((520, 300), [self.visible_sprites], self.obstacle_sprites)

    def draw(self):
        self.visible_sprites.custom_draw(self.player)

    def update(self):
        self.visible_sprites.update()

    def run(self):
        self.draw()
        self.update()


class Custom_visible_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset_pos = None
        self.display_surface = pygame.display.get_surface()
        self.off_set = pygame.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.ground_surf = pygame.image.load('../graphics/tilemap/Ground2.png')
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # self.offset_pos = sprite.rect.topleft
        self.off_set.x = player.rect.centerx - self.half_width
        self.off_set.y = player.rect.centery - self.half_height

        floor_offset_pos = self.ground_rect.topleft - self.off_set
        self.display_surface.blit(self.ground_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.offset_pos = sprite.rect.topleft - self.off_set
            self.display_surface.blit(sprite.image, self.offset_pos)
