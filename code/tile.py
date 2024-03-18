import pygame
import math
from support import *
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_object,  ImageSheet):
        super().__init__(groups)
        self.ImageSheet =  pygame.image.load(ImageSheet)
        self.sprite_object = sprite_object
        self.animation_start_loop = 0
        self.animation_status_loop = True  
        

    def animate(self):
        # Animate based on sprite type
        self.sprite_object.animate()
        
    # def _animate_box(self):
    #     # Animate box sprite
    #     self.image = get_image(self, self.animations['box_open'][math.floor(self.animation_start_loop)])
    #     if self.animation_status_loop:
    #         self.animation_start_loop += 0.03
    #         if self.animation_start_loop >= len(self.animations['box_open']) - 1:
    #             self.animation_start_loop = 3
    #             self.animation_status_loop = False
    #     else:
    #         self.animation_start_loop -= 0.03
    #         if self.animation_start_loop <= 0:
    #             self.animation_start_loop = 0
    #             self.animation_status_loop = True

    # def _animate_npc(self):
        # Animate npc sprite    
        self.image = get_image(self, self.animations[self.sprite_object][math.floor(self.animation_start_loop)])
        self.animation_start_loop += 0.1
        if self.animation_start_loop >= len(self.animations[self.sprite_object]) - 1:
            self.animation_start_loop = 1

    def update(self):
        self.animate()


class Fountain(Tile):
    def __init__(self, groups, pos):
        super().__init__(groups, self, '../graphics/objects_0/fountains.png')

        # Image setup
        self.image_width = TILE_SIZE * 2
        self.image_height = TILE_SIZE * 3
        self.animations = {
            'water_fall': [image_selector(1, i, self.image_width, self.image_height, 0, 0) for i in range(1, 5)]
            }
        # Sprite setup
        self.image = get_image(self, self.animations['water_fall'][0])
        self.frames = get_gif_frames_list('../graphics/objects_0/fountain1.gif')
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -90)
        
    def _animate_fountain(self):
        # Animate fountain sprite
        self.image = get_image(self, self.animations['water_fall'][math.floor(self.animation_start_loop)])
        self.animation_start_loop += 0.1
        if self.animation_start_loop >= len(self.animations['water_fall']): 
