import pygame
import math
from config import *



class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos, obstacles):
        super().__init__(groups)
        # prapering the image
        self.player_ImageSheet = pygame.image.load('../graphics/player/player0.png') # image sheet of the player 
        self.facing = {
            'right' : (self.image_selector(1, 1)),
            'up'    : (self.image_selector(1, 2)),
            'left'  : (self.image_selector(1, 3)),
            'down'  : (self.image_selector(1, 4))
        }
        self.status = 'down'
        # basic setup
        self.image = self.get_image(self.facing[self.status]) # get_image crops the required image 
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -30)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 5
        self.IsAttacking = False
        self.attack_cooldown = 400
        self.attack_timer = None
        self.obstacle_sprites = obstacles

        # animation 
        self.animation_start_loop = 1
        
        
    def image_selector(self, y, x):
        return ( (TILE_SIZE * (x-1)), ((TILE_SIZE * (y-1) * 2) + 25) )
    
    def animation(self):
        self.image = self.get_image(self.facing[self.status])
        
        animation_right = [self.image_selector(3, 1), 
                          self.image_selector(3, 2), 
                          self.image_selector(3, 3),
                          self.image_selector(3, 4),
                          self.image_selector(3, 5),
                          self.image_selector(3, 6),
                          ]    
        animation_up    = [self.image_selector(3, 7), 
                          self.image_selector(3, 8), 
                          self.image_selector(3, 9),
                          self.image_selector(3, 10),
                          self.image_selector(3, 11),
                          self.image_selector(3, 12),
                          ]
        animation_left  = [self.image_selector(3, 13), 
                          self.image_selector(3, 14), 
                          self.image_selector(3, 15),
                          self.image_selector(3, 16),
                          self.image_selector(3, 17),
                          self.image_selector(3, 18),
                          ]
        animation_down    = [self.image_selector(3, 19), 
                          self.image_selector(3, 20), 
                          self.image_selector(3, 21),
                          self.image_selector(3, 22),
                          self.image_selector(3, 23),
                          self.image_selector(3, 24),
                          ]
        
        if self.status == 'right' and self.direction.x != 0:
            self.image = self.get_image(animation_right[math.floor(self.animation_start_loop)])
            self.animation_start_loop += 0.2
            if self.animation_start_loop >= 5:
                self.animation_start_loop = 1
                
        elif self.status == 'up' and self.direction.y != 0:
            self.image = self.get_image(animation_up[math.floor(self.animation_start_loop)])
            self.animation_start_loop += 0.2
            if self.animation_start_loop >= 5:
                self.animation_start_loop = 1
                
        elif self.status == 'left' and self.direction.x != 0:
            self.image = self.get_image(animation_left[math.floor(self.animation_start_loop)])
            self.animation_start_loop += 0.2
            if self.animation_start_loop >= 5:
                self.animation_start_loop = 1
                
        elif self.status == 'down' and self.direction.y != 0:
            self.image = self.get_image(animation_down[math.floor(self.animation_start_loop)])
            self.animation_start_loop += 0.2
            if self.animation_start_loop >= 5:
                self.animation_start_loop = 1
                 
         
    def get_image(self, pos):
        sprite = pygame.Surface((TILE_SIZE, TILE_SIZE * 2 - 25))
        sprite.blit(self.player_ImageSheet, (0, 0), (pos[0], pos[1], TILE_SIZE, TILE_SIZE+400))
        sprite.set_colorkey('black')
        return sprite
    
    def collision(self, direction):
        if direction == 'herizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right= sprite.rect.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.rect.right

        elif direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.rect.bottom

    def input(self):

        # movement input:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
            # self.image = self.get_image(self.facing[self.status])
        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
            self.status = 'down'
            # self.image = self.get_image(self.facing[self.status])
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = +1
            self.status = 'right'
            # self.image = self.get_image(self.facing['right'])
            
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
            # self.image = self.get_image(self.facing['left'])
        else:
            self.direction.x = 0

        # attack input:
        if keys[pygame.K_SPACE] and not self.IsAttacking:
            self.IsAttacking = True
            self.attack_timer = pygame.time.get_ticks()


        # magic input:
        if keys[pygame.K_e] and not self.IsAttacking:
            self.IsAttacking = True
            self.attack_timer = pygame.time.get_ticks()


    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.IsAttacking:
            if current_time - self.attack_timer >= self.attack_cooldown:
                self.IsAttacking = False

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('herizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def update(self):
        self.animation()
        self.input()
        self.cooldowns()
        self.move(self.speed)
