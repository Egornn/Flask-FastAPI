import random as r
from PIL import Image, ImageDraw


# 1/Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def remove_str(input_file, output_file, removed_str):
    file = open(input_file, encoding='utf-8', mode='r')
    output = ' '.join([x for x in file.read().split() if not removed_str in x])
    file.close()
    file = open(output_file, encoding='utf-8', mode='w')
    file.write(output)
    file.close()


input_id = '1_in.txt'
output_id = '1_out.txt'
remove_strng = 'абв'
remove_str(input_id, output_id, remove_strng)

# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

candy = 51
max_candies = 28
print(f'To win the first one takes {candy % (max_candies + 1)} candies. ')


def pvp_candies(start, max_step):
    player_turn = r.randint(1, 3)
    turn = -1
    while start > 0:
        player_turn = player_turn % 2 + 1
        while not 0 < turn < max_step + 1:
            turn = int(input(
                f'{start} candies left. Player {player_turn}, how many candies do ' \
                f'you want to take? You cannot take more than {min(max_candies, start)} '))
        start -= turn
        turn = -1
    print(f"Congratulation to player {player_turn}! You've won!")


# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

def pve_candies(start, max_step):
    player_turn = r.randint(1, 3)
    turn = -1
    while start > 0:
        player_turn = player_turn % 2 + 1
        if player_turn == 1:
            while not 0 < turn < max_step + 1:
                turn = int(input(
                    f'{start} candies left. Human player, how many candies do ' \
                    f'you want to take? You cannot take more than {min(max_candies, start)} '))
        else:
            if start % (max_step + 1) == 0:
                turn = r.randint(1, max_step + 1)
            else:
                turn = start % (max_step + 1)
            print(f'There was {start} candies and the computer took {turn}.There is {start - turn} left.')
        start -= turn
        turn = -1
    if player_turn == 1:
        print("Congratulation to human player! You've won!")
    else:
        print("My condolences to human player! You've lost!")


def choose_mode(mode, candies, max_at_once):
    if mode == "pvp":
        pvp_candies(candies, max_at_once)
    elif mode == 'pve':
        pve_candies(candies, max_at_once)
    else:
        print('There is no such mode.')


choose_mode(input('Use "pvp" or "pve" for 2 players and against computer mode respectively '), candy, max_candies
# 3.Создайте программу для игры в ""Крестики-нолики"".
#def draw_board (current_position):


# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
