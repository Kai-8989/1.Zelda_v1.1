import pygame
from config import *



class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos, obstacles):
        super().__init__(groups)
        # prapering the image
        self.player_ImageSheet = pygame.image.load('../graphics/player/player0.png') # image sheet of the player 
        self.facing = {
            'down' : ((TILE_SIZE * 3, 25)),
            'right' : ((0, 25)),
            'left' : ((TILE_SIZE * 2, 25)),
            'up' : ((TILE_SIZE, 25))
        }
        
        # basic setup
        self.image = self.get_image(self.facing['down']) # get_image crops the required image 
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -30)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 5
        self.IsAttacking = False
        self.attack_cooldown = 400
        self.attack_timer = None

        self.obstacle_sprites = obstacles
        
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
            self.image = self.get_image(self.facing['up'])
        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
            self.image = self.get_image(self.facing['down'])
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = +1
            self.image = self.get_image(self.facing['right'])
            
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = self.get_image(self.facing['left'])
        else:
            self.direction.x = 0

        # attack input:
        if keys[pygame.K_SPACE] and not self.IsAttacking:
            self.IsAttacking = True
            self.attack_timer = pygame.time.get_ticks()
            print('attack!')

        # magic input:
        if keys[pygame.K_e] and not self.IsAttacking:
            self.IsAttacking = True
            self.attack_timer = pygame.time.get_ticks()
            print('magic')

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
        self.input()
        self.cooldowns()
        self.move(self.speed)
