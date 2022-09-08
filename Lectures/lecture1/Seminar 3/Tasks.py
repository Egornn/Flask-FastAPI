# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time as timer

lower_bound = -50
upper_bound = 50


def random_int(lower, upper):
    lower, upper = min(lower, upper), max(lower, upper)
    seed = timer.time() * pow(10, 6)
    return (lower + int(seed % (upper - lower)))

    # [-50, 50] -> 12353 ->ширина диапазона 50-(-50)=100\
    # seed%100 <=> seed%(upper-lower) [0,99]-> -50 -> [-50, 49]

    # [50, 100) -> 12353 ->ширина диапазона 100-50=50 seed%50 <=> seed%(upper-lower) [0,49]-> 50 -> [50, 99]


# print(random_int(lower_bound, upper_bound))

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
my_list = ['ahjg8fda9', 'fhjrg46', '324', '342', 'list7']


def find_number(some_list, number):
    is_contain = False
    number = str(number)
    for string in some_list:
        if string.__contains__(number):
            return True
    return is_contain


print(find_number(my_list, 46))


# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def find_position(some_list, substring, repeat):
    position = 0
    for i in range(len(some_list)):
        if some_list[i] == substring:  # some_list[i].__contains__(substring):
            position += 1
            if position == repeat:
                return i
    return -1


new_string = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print('Позиция второго вхождения', find_position(new_string, 'йцу', 2))


# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
#
# Например:
#
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и
# содержащие записи, в которых фамилия начинается с соответствующей буквы.

# Например:
#
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# name="Анна Савельева"
# key = name.split(' ')[1][0]


def thesaurus(new_dict={}, *names):
    for name in names:

        key = name.upper()[0]
        if key in new_dict.keys():
            new_dict[key].append(name)
        else:
            new_dict[key] = [name]
    return new_dict


test = thesaurus({}, "Иван", "Мария", "Петр", "Илья", 'илюша')
print(test)


def thesaurus_adv(dictionary={}, *names):
    for name in names:
        key = name.split(' ')[1][0]
        if key in dictionary.keys():
            thesaurus(dictionary[key], name)
        else:
            dictionary[key] = {name.split()[0][0]: [name]}
    return dictionary


print(thesaurus_adv({}, "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
