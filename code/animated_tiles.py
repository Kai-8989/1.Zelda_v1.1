import pygame
import math
from support import *
from config import *


class Animated_Tiles(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_object):
        super().__init__(groups)
        self.sprite_object = sprite_object
        
        # animation setup
        self.animation_start_loop = 0
        self.animation_status_loop = True  

    def animate(self):
        self.sprite_object.animate()    

    def update(self):
        self.animate()
        
    def get_image(self, pos):  # splits the an image from an ImageSheet according to x and y //// pos = (x, y)
        sprite = pygame.Surface((self.sprite_object.image_width, self.sprite_object.image_height))
        sprite.blit(self.sprite_object.ImageSheet, (0, 0), (pos[0], pos[1], self.sprite_object.image_width, self.sprite_object.image_height))
        sprite.set_colorkey('black')
        return sprite
    
    def image_selector(self, x, y, image_width, image_height, offset_x, offset_y):  # make it easier to locate an image in an ImageSheet. retruns the pos for the get_image function
        return ((image_width * (x-1) + offset_x), ((image_height * (y-1) + offset_y)))

class Object(Animated_Tiles):
    def __init__(self, groups, pos, name):
        super().__init__(groups, self)

        # object type
        self.name = name
        self.ImageSheet = None

        # Image setup
        if self.name == 'fountain':
            self.image_width = TILE_SIZE * 2
            self.image_height = TILE_SIZE * 3
            self.ImageSheet =  pygame.image.load('../graphics/objects/fountain.png')
            self.animations = [self.image_selector(i, 1, self.image_width, self.image_height, 0, 0) for i in range(1, 8)]
            
        
        elif self.name == 'big_tourch':
            self.image_width = TILE_SIZE * 1
            self.image_height = TILE_SIZE * 3
            self.ImageSheet =  pygame.image.load('../graphics/objects/big_tourch.png')    
            self.animations = [self.image_selector(i, 1, self.image_width, self.image_height, 0, 0) for i in range(1, 4)]
            
        
        # Sprite setup
        self.image = self.get_image(self.animations[0])
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -90)
        
    def animate(self):
        # Animate fountain sprite
        self.image = self.get_image(self.animations[math.floor(self.animation_start_loop)])
        self.animation_start_loop += 0.1
        if self.animation_start_loop >= len(self.animations):
            self.animation_start_loop = 0 
            
class NPC(Animated_Tiles):
    pass

class Terrian_Object(Animated_Tiles):
    pass
