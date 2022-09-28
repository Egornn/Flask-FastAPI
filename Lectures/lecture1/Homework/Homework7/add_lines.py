import os
from read_data import *
from keys import keys
import csv

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


def add_data_csv(data_path, path='data.csv'):

    data = input_csv(data_path)
    if os.path.getsize(path) == 0:
        with open(path, mode='w+') as cvs_headers:
            header_writer = csv.writer(cvs_headers, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            header_writer.writerow(i for i in data[0])
    new_data = only_new(data, path)
    with open(path, mode='w+') as csv_database:
        employee_writer = csv.writer(csv_database, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in new_data:
            employee_writer.writerow([row[i] for i in row])


add_data_csv('input.csv')