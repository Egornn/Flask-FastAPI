import re
from long import very_long_string


def remove_duplicates(any_list: list):
    new_list = []
    for el in any_list:
        if not (el in new_list):
            new_list.append(el)
    return new_list


def strange_convert(user_input: str):
    is_negative = False
    if user_input[0] == "-":
        is_negative = True
    if user_input.isdigit() or (user_input[1:].isdigit() and is_negative):
        if int(user_input) > 0:
            return int(user_input)
        else:
            return float(user_input)
    if user_input.isdecimal():
        return float(user_input)
    elif not user_input.lower() == user_input:
        return user_input.lower()
    else:
        return user_input.upper()


def process_tuple(any_tuple: tuple) -> dict:
    type_value_dict = {}
    for element in any_tuple:
        if type(element) in list(type_value_dict):
            type_value_dict[type(element)].append(element)
        else:
            type_value_dict[type(element)] = [element]
    return type_value_dict


def remove_twice_repeated(any_list: list) -> list:
    values_set = set(any_list)
    for element in values_set:
        if any_list.count(element) == 2:
            any_list.remove(element)
            any_list.remove(element)
    return any_list


def print_words(any_string: str) -> None:
    words_list = re.split("[!,.\s?]", any_string)
    words_list.sort()
    while words_list.count("") > 0:
        words_list.remove("")
    max_length = 0
    for word in words_list:
        max_length = max(max_length, len(word))
    for i in range(len(words_list)):
        extra_space = len(str(len(words_list))) - len(str(i + 1))
        if extra_space == 0:
            extra_space = ""
        else:
            extra_space = " " * extra_space
        print(f"{i + 1}{extra_space}{' ' * (max_length - len(words_list[i]) + 1)}{words_list[i]}")


def count_letters(any_string: str) -> dict:
    counted_letters = {}
    for i in range(len(any_string)):
        if any_string[i] in list(counted_letters):
            counted_letters[any_string[i]] += 1
        else:
            counted_letters[any_string[i]] = 1
    return counted_letters


def count_letters_using_count(any_string: str) -> dict:
    counted_letters = {}
    for letter in set(list(any_string)):
        counted_letters[letter] = any_string.count(letter)
    return counted_letters


def print_unique(bags: dict) -> None:
    def all_items(bag: dict) -> list:
        for name in list(bag):
            if name == list(bag)[0]:
                result = bag[name]
            else:
                result = result.union(bag[name])
        return result

    def all_have(bag: dict) -> list:
        for name in list(bag):
            if name == list(bag)[0]:
                result = bag[name]
            else:
                result = result.intersection(bag[name])
        return result

    def transform_sets(bag):
        bags_transformed = {}
        for name in bag:
            bags_transformed[name] = set(bag[name])
        return bags_transformed

    # def all_but_one(bag: dict) -> list:

    bags = transform_sets(bags)
    print(f"Full list {all_items(bags)}")
    print(f'All have {all_have(bags)}')


def get_list_of_twice(any_list: list) -> list:
    counter = {}
    for name in any_list:
        counter[name] = counter.setdefault(name, 0) + 1
    return [key for key in list(counter) if counter[key] == 2]


def words_counter(long_string: str) -> list:
    counter = {}
    long_string = long_string.lower()
    words_list = re.split("[!,:;\-.\s?\n]", long_string)
    for word in words_list:
        counter[word] = counter.setdefault(word, 0) + 1
    sorted_words = sorted(counter.items(), key=lambda x: x[1])
    sorted_words.pop()
    return sorted_words


def all_bags(options: dict, weight: int) -> list:
    option = []
    for i in range(2 ** len(list(options))):
        number_as_list = list(bin(i)[2:])
        for j in range(len(bin(2 ** len(list(options)))) - len(bin(i)) - 1):
            number_as_list.insert(0, '0')
        total_weight = 0
        this_option = []
        for j in range(len(number_as_list)):
            total_weight += int(number_as_list[j]) * options[list(options)[j]]
            if number_as_list[j] == "1":
                this_option.append(list(options)[j])
        if total_weight <= weight:
            option.append(this_option)
    return option


# # 1. Remove duplicate
my_list = [1, 1, 1, 2, 3, 4, 2, 1, 2, 4, 3, 2, 322]
print(remove_duplicates(my_list))
print(list(set(my_list)))

# 3. Convert input
print(strange_convert(input('Input something to convert: ')))

# 4. Elements of a tuple
my_tuple = (1, 2.3, "f", [2], 2)
print(process_tuple(my_tuple))

# 5 remove doubles
my_list = [1, 1, 1, 2, 3, 4, 2, 1, 322, 4, 3, 2, 322]
print(remove_twice_repeated(my_list))

# 5 Numerate odd
my_list = [1, 1, 1, 2, 3, 4, 2, 1, 322, 4, 3, 2, 322]
print([i + 1 for i in range(len(my_list)) if my_list[i] % 2 == 1])

# 6 Print words
my_string = "Hello, my dearest friend. Are you OK? I hope we will meet again! 66"
print_words(my_string)

# 7 Count letters
my_string = "Hello, my dearest friend. Are you OK? I hope we will meet again! 66"
print(count_letters(my_string))
print(count_letters_using_count(my_string))

# 8 Friends bags
friend_bags = {
    'John': ("Water", "Tent"),
    'Jim': ("Food", "Tent"),
    'Jam': ("Water", "Tent"),
}
print_unique(friend_bags)

# 9 All twice repeating
my_list = [1, 1, 1, 2, 3, 4, 2, 1, 322, 4, 3, 2, 322]
print(get_list_of_twice(my_list))

# 10 most often words
print(words_counter(very_long_string)[-10:])

# 11 Hiking
menu = {
    'water': 2,
    "tent": 10,
    "food": 4,
}
max_weight = 8
print(all_bags(menu, max_weight))
