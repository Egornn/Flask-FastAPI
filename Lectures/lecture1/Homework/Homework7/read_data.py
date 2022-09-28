import csv
from keys import keys
import csv


def input_read(path):
    try:
        f = open(path, "r", encoding='UTF8')
    except:
        print('Input does not exist')
        exit()
    temp = f.read().split('\n')
    f.close()
    lines = []
    for elem in temp:
        temp_dict = {}
        person = elem.split(' ')
        for i in range(len(person)):
            temp_dict[keys[i]] = person[i]
        lines.append(temp_dict)
    return lines


def input_csv(path):
    with open(path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='\n')
        lines = []
        for row in csvreader:
            lines.append({'LastName' if k == 'п»їLastName' else k: v for k, v in row.items()})
    return lines

#print(input_csv("input.csv"))
