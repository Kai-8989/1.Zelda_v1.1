import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)


# class Box(Tile):
#     def __init__(self, groups, pos):
#         super().__init__(groups, 'box', '../graphics/objects_0/box.png')
       
#         # Image setup
#         self.image_width = TILE_SIZE * 2 - 18
#         self.image_height = TILE_SIZE * 2
#         self.animations = {
#             'box_open': [image_selector(1, i, self.image_width, self.image_height, 10, 20) for i in range(1, 5)],
#         }

#         # Sprite setup
#         self.image = get_image(self, self.animations['box_open'][0])
#         self.rect = self.image.get_rect(topleft=pos)
#         self.hitbox = self.rect.inflate(0, -90)


# class NPC(Tile):
#     def __init__(self, groups, pos, npc_type):
#         super().__init__(groups, npc_type, '../graphics/objects_0/' + str(npc_type) + '.png')

#         # image set up
#         self.image_width = TILE_SIZE
#         self.image_height = TILE_SIZE * 2    
            
#         self.animations = {
#             'npc_1' : [image_selector(i, 2, self.image_width, self.image_height, 0, 0) for i in range(18, 24)],
#             'npc_2' : [image_selector(i, 2, self.image_width, self.image_height, 0, 0) for i in range(18, 24)]
#         }

#         # Sprite setup
#         self.image = get_image(self, self.animations[self.sprite_object][0])
#         self.rect = self.image.get_rect(topleft=pos)
#         self.hitbox = self.rect.inflate(0, 0)