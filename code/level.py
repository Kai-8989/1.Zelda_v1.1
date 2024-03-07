import pygame
from support import *
from config import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # init sprite attributes
        self.ground = None
        self.player = None  # i have created this attribute in order to control the player sprite freely
        self.tile = None  # that applys at this sprite too

        # get the display surface
        self.screen = pygame.display.get_surface()  # call the screen to draw the objects/sprites on it
        """
        _in visible_groupe wird alle sprites, die ich auf dem Screen zeichnen möchte gespeichert
        _in obsticale is created for the objecte that will collide with the player like rocks, trees, etc.... (it helps
        with collosion a lot 
        """

        # sprite groups setup
        self.visible_group = Custom_Group()
        self.obsticale_group = pygame.sprite.Group()

        # sprite setup
        self.generate_sprites()  # create the map and the sprites

    def generate_sprites(self):
        layouts = {
            'boundary' : imoprt_layout('../map/map_FloorBlocks.csv')
        }
        for type, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if layout == 'boundary':
                            x = TILE_SIZE * col_index
                            y = TILE_SIZE * row_index
                            self.tile = Tile([self.visible_group, self.obsticale_group], (x, y), 'hi')
                         
        self.ground = Ground()
        self.player = Player([self.visible_group], (520, 320), self.obsticale_group)  # Player(gourps, pos, collision_groupe)

    def run(self):
        # update
        self.visible_group.update()
        self.obsticale_group.update()

        # draw
        self.visible_group.custom_draw(self.player, self.ground)


class Custom_Group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()  # the offset between the player and other sprites, here is seted to [0,0]
        self.offset = pygame.math.Vector2()
        self.halfDisplayWidth = pygame.display.get_surface().get_size()[0] / 2
        self.halfDisplayHeight = pygame.display.get_surface().get_size()[1] / 2

    def center_screen_target_offset(self, target):
        self.offset.x = self.halfDisplayWidth - target.rect.centerx
        self.offset.y = self.halfDisplayHeight - target.rect.centery

        """ center the target(player) on the middle of the screen, by adding an offset/ padding between the player 
        and other sprites. The padding here equales half the size of the screen vertically and herizontally """

    def custom_draw(self, player, ground):
        # functions
        self.center_screen_target_offset(player)

        # centering the player compared to ground
        offset_pos_ground = self.offset + ground.rect.topleft
        pygame.display.get_surface().blit(ground.image, offset_pos_ground)

        # centering the player compared to other sprites
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            sprites_pos_with_offset = self.offset + sprite.rect.topleft
            self.screen.blit(sprite.image, sprites_pos_with_offset)


"""
I created this custom class, which iherited from Group class in order to customise the drawing function in Group
The goal from this class is: 
1. custom draw the groupe
    a. so i can draw the ground separately from other sprites in visible_group 
    ( i want to do that becase the ground has a sprite and a rectangle in other words its a sprite that is visble so it
    must be in the visible group but it also has to be the first thing that renders (to be at the bottom of other
    sprites.)

    b. to make a group of sprites that update togather relativ to the player sprite in orderto give the illusion that the 
    player moving

2. to sort the list of sprite in this gourp so that they update gradually after eachother. Making this sorting list
adjusts the overlapping objects in the screen
"""


class Ground(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.image = pygame.image.load('../graphics/tilemap/Ground2.png')
        self.rect = self.image.get_rect(topleft=pos)
