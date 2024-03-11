import pygame
import math
from config import *



class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos, obstacles):
        super().__init__(groups)
        # prapering the image
        self.player_ImageSheet = pygame.image.load('../graphics/player/player3.png') # image sheet of the player 
        
        self.animations = {
            'right' : {
                'move': [self.image_selector(3, i) for i in range(1, 7)],
                'stand': [self.image_selector(2, i) for i in range(1, 7)],
                'attack': [self.image_selector(14, i) for i in range(1, 7)],
                },
            
            'up' : {
                'move': [self.image_selector(3, i) for i in range(7, 13)],
                'stand': [self.image_selector(2, i) for i in range(7, 13)],
                'attack': [self.image_selector(14, i) for i in range(7, 13)],
            },
            
            'left' : {
                'move': [self.image_selector(3, i) for i in range(13, 18)],    
                'stand': [self.image_selector(2, i) for i in range(13, 18)],
                'attack': [self.image_selector(14, i) for i in range(13, 18)],
            },
            
            'down' : {
                'move': [self.image_selector(3, i) for i in range(18, 24)],
                'stand': [self.image_selector(2, i) for i in range(18, 24)],
                'attack': [self.image_selector(14, i) for i in range(18, 24)],
            }   
        }
        self.status = 'down'    
        
        # basic setup
        self.image = self.get_image(self.image_selector(2, 18)) # get_image crops the required image 
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -30)

        # movement, attacking and reading
        self.direction = pygame.Vector2()
        self.speed = 5
        self.IsAttacking = False
        self.IsReading = False
        self.attack_cooldown = 400
        self.attack_timer = None
        self.obstacle_sprites = obstacles

        # animation 
        self.animation_start_loop = 1
        self.legs_speed = 0.2
        
    def update(self):
        self.animation()
        self.input()
        self.cooldowns()
        self.move(self.speed)
        
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('herizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        
    def input(self):

        keys = pygame.key.get_pressed()
        
        # movement input:
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'

        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
            self.status = 'down'

        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = +1
            self.status = 'right'
            
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        
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
    
    def collision(self, direction):
        if direction == 'herizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right= sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        elif direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                        
    def animation(self):
        for direction, dir_group in self.animations.items():
            if self.status == direction:
                if self.direction.x != 0 or self.direction.y != 0:
                        self.image = self.get_image(dir_group['move'][math.floor(self.animation_start_loop)])
                        self.animation_start_loop += self.legs_speed
                        if self.animation_start_loop >= 5:
                            self.animation_start_loop = 1 
                            
                elif self.IsAttacking:
                        self.image = self.get_image(dir_group['attack'][math.floor(self.animation_start_loop)])
                        self.animation_start_loop += 0.1
                        if self.animation_start_loop >= 5:
                            self.animation_start_loop = 1

                else:
                    self.image = self.get_image(dir_group['stand'][math.floor(self.animation_start_loop)])
                    self.animation_start_loop += 0.1
                    if self.animation_start_loop >= 5:
                        self.animation_start_loop = 1 
        
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.IsAttacking:
            if current_time - self.attack_timer >= self.attack_cooldown:
                self.IsAttacking = False

        # if self.IsReading:
        #     if current_time - self.attack_timer >= self.attack_cooldown:
        #         self.IsReading = False

    def get_image(self, pos):
        sprite = pygame.Surface((TILE_SIZE, TILE_SIZE * 2 - 20))
        sprite.blit(self.player_ImageSheet, (0, 0), (pos[0], pos[1], TILE_SIZE, TILE_SIZE+400))
        sprite.set_colorkey('black')
        return sprite
    
    def image_selector(self, y, x):
        return ( (TILE_SIZE * (x-1)), ((TILE_SIZE * (y-1) * 2) + 20) )
