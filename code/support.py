from os import walk
from csv import reader

def imoprt_layout(path):
    terrian = []
    with open(path) as layout_path:
        layout_list = reader(layout_path, delimiter=',')
        for row in layout_path:
            terrian.append(list(row))
            return terrian
    # print(reader(open(path), delimiter = ',')) 