from os import walk
from csv import reader

def imoprt_map(path):
    terrian = []
    with open(path) as file_path:
        tem_list = reader(path, delimiter=',')
        for row in tem_list:
            print(row)
    # print(reader(open(path), delimiter = ','))
    

imoprt_map('../map/map_Details.csv')