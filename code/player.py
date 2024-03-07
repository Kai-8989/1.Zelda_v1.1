import pygame
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos, obstacles):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player/down/down_0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -30)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 5
        self.IsAttacking = False
        self.attack_cooldown = 400
        self.attack_timer = None

        self.obstacle_sprites = obstacles

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.rect.left

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
        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = +1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = pygame.image.load('../graphics/player/left/left_1.png').convert_alpha()
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
