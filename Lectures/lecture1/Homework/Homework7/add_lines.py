import os
from read_data import *
from keys import keys

def add_data(data_path='input.txt', path='data.txt'):
    data = input_read(data_path)
    if os.path.getsize(path) == 0:
        temp = ''
    else:
        temp = "\n"
    f = open(path, "a", encoding='UTF8')
    new_data = only_new(data)
    for line in new_data:
        for element in line:
            temp += str(line[element]) + ' '
        temp = temp[:-1] + '\n'
    f.write(temp[:-1])
    f.close()


def only_new(data, path='data.txt'):
    already_exists = input_read(path)
    return [element for element in data if element not in already_exists]
