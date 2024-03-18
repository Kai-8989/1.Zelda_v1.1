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

def get_image(object, pos):  # splits the an image from an ImageSheet according to x and y //// pos = (x, y)
    sprite = pygame.Surface((object.image_width, object.image_height))
    sprite.blit(object.ImageSheet, (0, 0), (pos[0], pos[1], object.image_width, object.image_height))
    sprite.set_colorkey('black')
    return sprite
    
def image_selector(x, y, image_width, image_height, offset_x, offset_y):  # make it easier to locate an image in an ImageSheet. retruns the pos for the get_image function
    return ((image_width * (x-1) + offset_x), ((image_height * (y-1) + offset_y)))

def get_gif_frames_list(gif_path):
    gif_frames = imread(gif_path)
    gif = imread(gif_path) 
    return  gif_frames

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

img = Image.open('../graphics/objects_0/box.png')
print(img)