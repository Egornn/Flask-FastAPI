import random

n = 10
m = 4
my_list = [random.randint(-10, 10) for x in range(n)]
my_float = [random.uniform(-10, 10) for x in range(m)]
print('Integer list', my_list)
print('Float list', my_float)


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def sum_of_odds(big_list):
    sum_odds = 0
    for i in range(0, len(big_list), 2):
        sum_odds += big_list[i]
    return sum_odds


print(sum_of_odds(my_list))


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiply_pairs(some_list):
    return [some_list[i] * some_list[-i - 1] for i in range(len(some_list) // 2)]


print(multiply_pairs(my_list))


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def after_the_dot(float_list):
    return [float_list[i] % 1 for i in range(len(float_list))]


temp_list = after_the_dot(my_float)
print(max(temp_list) - min(temp_list))


# Alternatively without min and max
def max_or_min_of_float(fraction_list, max_min="max"):
    min_float = 1
    max_float = 0
    for i in range(len(fraction_list)):
        if max_float < fraction_list[i]:
            max_float = fraction_list[i]
        if min_float > fraction_list[i]:
            min_float = fraction_list[i]
    if max_min == "max":
        return max_float
    elif max_min == 'min':
        return min_float
    else:
        return -1


print(max_or_min_of_float(temp_list, 'max') - max_or_min_of_float(temp_list, 'min'))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def dec_2_bin(dec_number):
    binary_list = []
    binary = 0
    while dec_number > 0:
        binary_list.append(dec_number % 2)
        dec_number = dec_number // 2
    binary_list.reverse()
    for i in range(len(binary_list)):
        binary = 10 * binary + binary_list[i]
    return binary


print(n, "-> to binary", dec_2_bin(n))


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#

def fib_both_direct(both_limits):
    if both_limits == 0:
        return [0]
    fib_list = [1, 0]
    for i in range(both_limits):
        fib_list.append(fib_list[len(fib_list) - 2] - fib_list[len(fib_list) - 1])
    fib_list.reverse()
    for i in range(both_limits - 1):
        fib_list.append(fib_list[len(fib_list) - 2] + fib_list[len(fib_list) - 1])
    return fib_list


print(fib_both_direct(n))
