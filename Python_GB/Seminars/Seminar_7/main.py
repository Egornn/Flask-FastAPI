import random
import string
from random import randint, uniform, choice, shuffle
import os
import shutil
from pathlib import Path


def random_numbers(pairs: int, file_name: str):
    with open(file=file_name, mode='a', encoding="UTF-8") as f:
        for i in range(pairs):
            f.write(f"{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n")
    f.close()


def pseudo_names_generator(file_name: str, number_created: int):
    min_length = 4
    max_length = 7
    vowels = ['a', 'e', 'i', "o", 'u', 'y']
    generated_list = []
    for i in range(number_created):
        new_word = ''
        has_vowel = False
        for j in range(randint(min_length, max_length)):
            new_word += choice(string.ascii_lowercase)
            if new_word[j] in vowels:
                has_vowel = True
        if not has_vowel:
            new_word = new_word[:-1] + choice(vowels)
            list_words = list(new_word)
            shuffle(list_words)
            new_word = "".join(list_words)
        new_word = new_word.capitalize()
        generated_list.append(new_word)
    with open(file=file_name, mode='a', encoding='UTF-8') as fi:
        for line in generated_list:
            fi.writelines(f"{line}\n")
        fi.close()


def multiply_files(file_num: str, file_names: str, output: str):
    with \
            open(file_num, encoding="UTF-8", mode='r') as f_num, \
            open(file_names, encoding="UTF-8", mode='r') as f_name, \
            open(output, encoding="UTF-8", mode='w') as out:
        is_end_1 = True
        is_end_2 = True
        next_numbers = f_num.readline()
        name_to_write = f_name.readline()
        while is_end_1 or is_end_2:
            numbers = next_numbers.split(sep='|')
            mult = float(numbers[0]) * float(numbers[1])
            if mult >= 0:
                out.writelines(f'{name_to_write[:-2].upper()}:{round(mult)}\n')
            else:
                out.writelines(f'{name_to_write[:-2].lower()}:{abs(mult)}\n')
            next_numbers = f_num.readline()
            name_to_write = f_name.readline()
            if next_numbers == "":
                is_end_1 = False
                f_num.seek(0)
                next_numbers = f_num.readline()
            if name_to_write == "":
                is_end_2 = False
                f_name.seek(0)
                name_to_write = f_name.readline()
        f_num.close()
        f_name.close()
        out.close()


def generate_name(min_name, max_name):
    random_name = ""
    for j in range(min_name, max_name + 1):
        random_name += choice(string.ascii_lowercase)
    return random_name


def random_files(extension, folder='random_4', min_name=6, max_name=30, min_length=256, max_length=4096,
                 files_number=42):
    already_created = [""]
    for i in range(files_number):
        random_name = ""
        while random_name in already_created:
            random_name = generate_name(min_name, max_name)
        already_created.append(random_name)
        random_name += f'.{extension}'
        random_byte = bytearray(random.getrandbits(8) for _ in range(randint(min_length, max_length + 1)))
        if not os.path.isdir(folder + '/'):
            os.makedirs(folder, exist_ok=True)
        with open(file=f"{folder}/" + random_name, mode='wb') as random_file:
            random_file.write(random_byte)
            random_file.close()


def free_files(dictionary_files: dict, path='random_5'):
    for ext, num in dictionary_files.items():
        random_files(ext, files_number=num, folder=path)


def sor_files(folder_path: str):
    ext_dir_dict = {'png': 'Image', 'jpeg': 'Image', 'txt': 'Text', 'ini': 'Text', 'avi': 'Video', 'mp4': 'Video'}
    file_list = os.listdir(folder_path)
    for code in ext_dir_dict:
        if not os.path.isdir(folder_path + '/' + ext_dir_dict[code]):
            os.makedirs(folder_path + '/' + ext_dir_dict[code], exist_ok=True)
    for file_name in file_list:
        if os.path.isfile(folder_path + '/' + file_name):
            extent = file_name.split('.')[-1]
            if extent in ext_dir_dict.keys():
                shutil.move(os.path.join(folder_path, file_name),
                            os.path.join(folder_path + "/" + ext_dir_dict[extent], file_name))
            print(file_name)


def rename_files(count_nums: int, extension_start: str, extension_final: str,
                 name_min: int, name_max: int, name_final: Path = '') -> None:
    p = Path(Path().cwd())
    serial_number = int('1' + ('0' * (count_nums - 1)))
    try:
        for obj in p.iterdir():
            print(obj)
            full_name = str(obj).split('\\')[-1]
            file_name, file_extension = full_name.split('.')
            if file_extension == extension_start:
                Path(full_name).rename(
                    f'{_name_clipping(file_name, name_min, name_max)}{name_final}{serial_number}.{extension_final}')
                serial_number += 1
    except:
        print('Not all file are correctly named')


def _name_clipping(current_name: str, name_min: int, name_max: int) -> str:
    return current_name[name_min:name_max]


def test_func():
    return int('1' + ('0' * 5))


if __name__ == "__main__":
    random_numbers(100, "pairs.txt")
    pseudo_names_generator("list of names.txt", 100)
    multiply_files("pairs.txt", 'list of names.txt', 'output_task_3.txt')
    random_files('txt', 6, 10, 10, 20, 2)
    free_files({'txt': 5, "ini": 3})
    free_files({'txt': 5, "ini": 3}, path="random_6/random_6")
    sor_files("C:/Users/Егор/PycharmProjects/Python_GB/Seminars/Seminar_7/Seven")
    pass
