from csv import reader
from os import walk
from imageio import get_reader
from matplotlib.image import imread
from PIL import Image
import numpy as np
import pygame


def import_csv_layout(path):
    terrian_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')   
        for row in layout:
            terrian_map.append(list(row))
        return terrian_map     


def import_files_forlder(path): # import files from the folder_path
    surface_list = []
    for _, __, data in walk(path):
        for image in data:
            full_path = path + '/' + image
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    return surface_list


    


# def get_gif_frames_list(gif_path):
#     gif_frames = imread(gif_path)
#     gif = imread(gif_path) 
#     return  gif_frames

# test_array = [[1, 2, 3, 4, [3, 3, 3]], [1, 2, 3, 4, [4, 4, 4]], [1, 2, 3, 4, [5, 5, 5]]]
# tupel = ('adfa', [], [1, 2, 3, 4])
# # for _, __, n, ___, ____, in test_array:
#     print(n)

# def new_func():
#     for _, n, __ in walk('../graphics'):
#         if not n:  # Check if the list 'n' is empty
#             continue
#         else:
#             print(n)

# new_func()

# img = Image.open('../graphics/objects_0/box.png')
# print(img)