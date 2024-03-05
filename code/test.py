import pygame
from config import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # init sprite attributes
        self.ground = None
        self.player = None
        self.tile = None

        # get the display surface
        self.display_surf = pygame.display.get_surface()

        # sprite groups setup
        self.visible_sprites = Custom_Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_sprites()

    def create_sprites(self):
        self.ground = Ground()
        self.player = Player([self.visible_sprites], (520, 300), self.obstacle_sprites)
        self.tile = Tile([self.visible_sprites, self.obstacle_sprites], (500, 500), 'invisib')

    def update(self):
        self.visible_sprites.update()
        self.obstacle_sprites.update()

    def draw(self):
        self.visible_sprites.custom_draw(self.player, self.ground)

    def run(self):
        self.draw()
        self.update()


class Custom_Group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.halfDisplayWidth = pygame.display.get_surface().get_size()[0] / 2
        self.halfDisplayHeight = pygame.display.get_surface().get_size()[1] / 2

    def center_camera_target(self, target):
        self.offset.x = self.halfDisplayWidth - target.rect.centerx
        self.offset.y = self.halfDisplayHeight - target.rect.centery

    def custom_draw(self, player, ground):
        self.center_camera_target(player)

        offset_pos_ground = self.offset + ground.rect.topleft
        pygame.display.get_surface().blit(ground.image, offset_pos_ground)

        for sprite in self.sprites():
            pos_sprite = self.offset + sprite.rect.topleft
            pygame.display.get_surface().blit(sprite.image, pos_sprite)


class Ground(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.image = pygame.image.load('../graphics/tilemap/Ground2.png')
        self.rect = self.image.get_rect(topleft=pos)
