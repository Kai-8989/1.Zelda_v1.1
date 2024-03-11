import pygame
import math
from code.config import TILE_SIZE
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, pos, sprite_type, surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        super().__init__(groups)
        
        self.sprite_type = sprite_type
        
        # invisible sprites
        if self.sprite_type == 'invisible':
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
            self.rect = self.image.get_rect(topleft=pos)
            self.hitbox = self.rect.inflate(0, -10)

        #fountain sprite
        elif self.sprite_type == 'fountain':
            # basic setup
            self.fountain_ImageSheet = pygame.image.load('../graphics/objects_0/fountains.png')
            self.image_width = TILE_SIZE * 2
            self.image_height = TILE_SIZE * 3
            self.animations = {
                    'water_fall' : [self.image_selector(1, i) for i in range(1, 5)]
            } 
            self.image = self.get_image(self.animations['water_fall'][0])
            self.rect = self.image.get_rect(topleft=pos)
            self.hitbox = self.rect.inflate(0, -90)
            
            # animation loop
            self.animation_start_loop = 0

        # black sprites (not determined)
        else:
            self.image = surface
            self.rect = self.image.get_rect(topleft=pos)
            self.hitbox = self.rect.inflate(0, -10)
    
    
    def get_image(self, pos):
        sprite = pygame.Surface((self.image_width, self.image_height))
        sprite.blit(self.fountain_ImageSheet, (0, 0), (pos[0], pos[1], self.image_width, self.image_height))
        sprite.set_colorkey('black')
        return sprite
    
    def image_selector(self, x, y, image_width, image_size, offset):
        offset = 5
        return ((self.image_width * (x-1)) , ((self.image_height * (y-1) + offset)))
    
    def animation(self):
        if self.sprite_type == 'fountain':
            self.image = self.get_image(self.animations['water_fall'][math.floor(self.animation_start_loop)])
            self.animation_start_loop += 0.1
            if self.animation_start_loop >= 4:
                self.animation_start_loop = 1
                
    def update(self):
        self.animation()
