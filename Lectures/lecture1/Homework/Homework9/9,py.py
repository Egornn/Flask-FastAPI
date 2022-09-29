import random as r
from PIL import Image, ImageDraw
import os as os
import random as rnd

board_path = 'tic-tac-toe.jpg'
size = 1500


def initial_setup(size):
    try:
        os.remove(board_path)
    except:
        pass
    im = Image.new('RGB', (size, size), (256, 256, 256))
    draw = ImageDraw.Draw(im)
    for i in range(size // 3, size, size // 3):
        draw.line((i, 0, i, size), fill=(0, 0, 0), width=10)
        draw.line((0, i, size, i), fill=(0, 0, 0), width=10)
    im.save(board_path, quality=100)
    return [[' ' for x in range(3)] for y in range(3)]


def get_input_coordinates(board, symbol):
    is_done = False
    coord = [-1, -1]
    while (not (0 <= coord[0] <= 2)) or (not (0 <= coord[1] <= 2)) or not is_done:
        coordinates = input(f'Enter the (row,column) to draw a {symbol} from 1 to 3) ')
        try:
            coord_given = list(map(int, coordinates.split(',')))
            coord = [coord_given[i] - 1 for i in range(len(coord_given))]
        except:
            pass
        if not len(coord) == 2:
            print('Write coordinates in a form "x,y"')
            coord = [-1, -1]

        # coord[0] = int(input(f'Enter the row to draw a {symbol} from 1 to 3): ')) - 1
        # coord[1] = int(input(f'Enter the column to draw a {symbol} from 1 to 3): ')) - 1
        try:
            correct = board[coord[0]][coord[1]] == " "
            if correct:
                is_done = True
            else:
                print('This space is already taken')
        except:
            pass
        print('')
    return coord


def coordinates_of_x(horizontal, vertical, left_or_right):
    center_x = vertical * size // 3 + size // 6
    center_y = horizontal * size // 3 + size // 6
    offset = size // 10
    if left_or_right == 'L':
        return (center_x - offset, center_y - offset, center_x + offset, center_y + offset)
    elif left_or_right == "R":
        return (center_x + offset, center_y - offset, center_x - offset, center_y + offset)


def coordinates_of_o(horizontal, vertical):
    center_x = vertical * size // 3 + size // 6
    center_y = horizontal * size // 3 + size // 6
    offset = size // 8
    return (center_x - offset, center_y - offset, center_x + offset, center_y + offset)


def draw_x_o(horizontal, vertical, x_or_o):
    im = Image.open(board_path)
    draw = ImageDraw.Draw(im)
    if x_or_o == 'X':
        draw.line(coordinates_of_x(horizontal, vertical, "L"), fill=(255, 0, 0), width=size // 30)
        draw.line(coordinates_of_x(horizontal, vertical, "R"), fill=(255, 0, 0), width=size // 30)
    elif x_or_o == 'O':
        draw.ellipse(coordinates_of_o(horizontal, vertical), fill=(255, 255, 255), outline=(0, 256, 0),
                     width=size // 30)
    im.save(board_path, quality=100)


def check_if_win(b, symbol):
    win = [symbol for x in range(3)]
    lines = [b[0], b[1], b[2], [b[i][0] for i in range(3)], [b[i][1] for i in range(3)], [b[i][2] for i in range(3)],
             [b[i][i] for i in range(3)], [b[i][-i - 1] for i in range(3)]]
    return win in lines


def play_cycle(board):
    turn = 0
    current_player = 1
    corresponding_symbols = {1: 'X', 2: 'O'}
    while not check_if_win(board, corresponding_symbols[current_player % 2 + 1]):
        if turn == 9:
            current_player = -1
            break
        coordinate = get_input_coordinates(board, corresponding_symbols[current_player])
        board[coordinate[0]][coordinate[1]] = corresponding_symbols[current_player]
        draw_x_o(coordinate[0], coordinate[1], corresponding_symbols[current_player])
        current_player = current_player % 2 + 1
        turn += 1
    if current_player == 1:
        print('Congratulations to O player')
    elif current_player == 2:
        print('Congratulations to the X player')
    elif current_player == -1:
        print("That's a tie")


def solve_tic_tac_toe():
    current_board = initial_setup(size)
    play_cycle(current_board)


# solve_tic_tac_toe()   #remove comment to play


# 3. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут
# соответствовать правилам задания ключей в словарях.
def to_dict(some_list):
    return {key: key for key in some_list}


print(to_dict(['1', 2, '34rf']))


# 4. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

def biggest_dict(**kwargs):
    for key in kwargs:
        my_dict[key] = kwargs[key]
    return my_dict


my_dict = {'first_one': "we can do it"}

print(biggest_dict(myCuteUwUParameter=32, secodn=2, third='fdfd', Biggest='D'))


# 5. Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа
# (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Д
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
def return_nth_dict(dictionary, index):
    i = 0
    for keys in dictionary:
        if i == index:
            return keys
        i += 1
    return None


def count_it(sequence):
    num_dict = {}
    for num in sequence:
        num_dict[int(num)] = num_dict.get(int(num), 0) + 1
    ordered_dict = {k: v for k, v in sorted(num_dict.items(), key=lambda i: i[1])}

    return [(return_nth_dict(ordered_dict,i), ordered_dict[return_nth_dict(ordered_dict,i)])
            for i in range(max(0,len(num_dict)-3), len(num_dict))]

def generate_little_random_sting_with_numbers(n):
    return ''.join(str(rnd.randint(0, 9)) for i in range(n))

some_str = '1234243287643262143216541291092403020975298492730274109231487320931'
strung=generate_little_random_sting_with_numbers(1000)
print(count_it(some_str))
print(strung)
print(count_it(strung))
