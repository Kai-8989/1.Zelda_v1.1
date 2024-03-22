import pygame
import sys
from config import *
# from level import Level
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.events()
            self.display_surface.fill('dark green')
            self.level.run()
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
