import json
import csv
import pickle
import time
import os


def txt_to_json(input_path, output_path):
    dictionary = {}
    with open(input_path, 'r', encoding='utf-8') as f_read:
        with open(output_path, 'w', newline='', encoding='utf-8') as f_write:
            for line in f_read:
                text_line = line.split(':')
                dictionary[text_line[0].capitalize()] = text_line[1][:-2]
            json.dump(dictionary, f_write, indent=2)


def id_name():
    output_path = 'Output_2.txt'
    is_continue = True
    current_data: dict = read_json(output_path)
    while is_continue:
        name = input('Please give a name: ')
        id = input('Please provide ID: ') + str(time.time())
        access = input('Please provide access (1 to 7): ')
        to_cont = input('Wanna exit(y)? ')
        if to_cont == 'y':
            is_continue = False
        if access in current_data.keys():
            current_data[access].update({id: name})
        else:
            current_data[access] = {id: name}
        with open(output_path, 'w') as f:
            json.dump(current_data, f, indent=2)
        with open(output_path + ".csv", 'w') as csv_write:
            csv_dictionary = csv.writer(csv_write, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            csv_dictionary.writerow(('access', 'id', 'name'))
            for k, v in current_data.items():
                for k_2, v_2 in v.items():
                    csv_dictionary.writerow((k, k_2, v_2))


def read_json(path):
    with open(path, 'r') as f_read:
        return json.load(f_read)


def json_to_pickle(path_to_transform):
    files = os.listdir(path_to_transform)
    for name in files:
        print(name)
        if name.split('.')[-1] == 'json':
            with open(name, 'r') as f_read:
                dictionary = json.load(f_read)
            name = name[:-4] + "pickle"
            with open(name, 'wb') as f_write:
                pickle.dump(dictionary, f_write)


def pickle_to_csv(path_to_pickle):
    with open(path_to_pickle, 'rb') as f_read:
        dictionary = pickle.load(f_read)
        with open(path_to_pickle[:-6] + ".csv", 'w') as f_write:
            csv_dictionary = csv.writer(f_write, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            for k, v in dictionary.items():
                csv_dictionary.writerow([k, v])


def print_pickle(path_to_pickle):
    with open(path_to_pickle, 'rb') as f_read:
        text = pickle.load(f_read)
        print(pickle.dumps(text))


def get_dirs_json(curr_dir):
    sum_dirs = 0
    dict_dir = {}
    types = ['file', 'folder']
    for i, file in enumerate(os.listdir(curr_dir), 1):
        path = os.path.join(curr_dir, file)
        item_dict = {'name': path.split('\\')[-1], 'parent': path.split('\\')[-2], 'type': None, 'size': None}
        dict_dir[i] = item_dict
        if os.path.isfile(path):
            item_dict['size'] = f'{os.path.getsize(path)} b'
            item_dict['type'] = types[0]
        elif os.path.isdir(path):
            sum_dirs += os.path.getsize(path)
            item_dict['size'] = f'{sum_dirs} b'
            item_dict['type'] = types[1]
            dict_dir.update(get_dirs_json(path))
    return dict_dir


def write_json(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_csv(file, data: dict[int:{str: str | int}]) -> None:
    with open('dir_info_csv.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerow(('id', 'name', 'parent', 'type', 'size'))
        for k, v in data.items():
            writer.writerow((k, v['name'], v['parent'], v['type'], v['size']))


def write_pickle(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'wb') as f:
        pickle.dump(data, f)


# txt_to_json('../Seminar_7/output_task_3.txt', 'output_1.json.jso')
# id_name()
# json_to_pickle("../Seminar_8")
# pickle_to_csv('output_1.pickle')
# print_pickle("output_1.pickle")
dict_json = get_dirs_json('../../Seminars')
write_json('dir_info_json.json', dict_json)
write_csv('dir_info_csv.csv', dict_json)
write_pickle('dir_info_picle.pickle', dict_json)
