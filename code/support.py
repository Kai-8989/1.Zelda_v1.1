from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrian_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            print(row)
            terrian_map.append(list(row))

        return terrian_map


def import_forlder(path):
    surface_list = []
    for _, __, data in walk(path):
        for image in data:
            full_path = path + '/' + image
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    return surface_list



