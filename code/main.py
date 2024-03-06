import pygame
import sys
from settings import *
from level import Level
from support import *


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        pygame.display.set_caption('Zelda')
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        # objects
        self.level = Level()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.events()
            self.screen.fill('green')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
