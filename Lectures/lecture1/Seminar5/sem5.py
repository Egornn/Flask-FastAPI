# Задача HARD SORT.
# Задайте двумерный массив из целых чисел.
# Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10
#
# задача 2 HARD необязательная. Сгенерировать массив
# случайных целых чисел размерностью m*n (размерность вводим с клавиатуры).
# Вывести на экран красивенько таблицей.
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно один раз переместился на другое место и потом не участвовал никак (возможно для этого удобно будет использование множества) и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

import random as r


def sort(arr):
    for k in range(len(arr)):
        min = k
        for i in range(k, len(arr)):
            if arr[i] < arr[min]:
                min = i
        arr[min], arr[k] = arr[k], arr[min]

    return arr


def median(arr):
    return arr[(len(arr)) // 2]


rows = 3  # int(input('Число строк в массиве '))
column = 3  # int(input('Число колонок в массиве '))
matrix = [[r.randint(-10, 10) for i in range(column)] for j in range(rows)]
temp = []


def print_dimentional(matrix):
    for lists in matrix:
        print(lists)
    print()


for i in range(rows):
    for j in range(column):
        temp.append(matrix[i][j])

sorted_temp = sort(temp)

# print()
# print(f'median {median(sorted_temp)}')

# print_dimentional(matrix)

for i in range(rows):
    for j in range(column):
        matrix[i][j] = sorted_temp[i * column + j]

# print_dimentional(matrix)


some_string = '5+4*6/12-4'
list_of_operators =['-', '+', '*', '/']

def split_into_arfim(some_sting, list_of_operators):
    operator=[]
    numbers=[]
    temp = ''
    for char in some_sting:
        if not char in list_of_operators:
            temp+=char
        else:
            operator.append(char)
            numbers.append(int(temp))
            temp=''
    numbers.append(int(temp))
    # print(numbers)
    # print(operator)
    #[5, 4, 6, 12, 4]
    #['+', '*', '/', '-']

    while len(numbers)>1:

        if '*' in operator:
            index=operator.index('*')
            temp=parser(numbers[index],numbers[index+1], '*')
            numbers[index]=temp
        elif '/' in operator:
            index = operator.index('/')
            temp = parser(numbers[index], numbers[index + 1], '/')
            numbers[index] = temp
        elif '+' in operator:
            index = operator.index('+')
            temp = parser(numbers[index], numbers[index + 1], '+')
            numbers[index] = temp
        elif '-' in operator:
            index = operator.index('-')
            temp = parser(numbers[index], numbers[index + 1], '-')
            numbers[index] = temp

        del (numbers[index+1])
        del (operator[index])
    return numbers[0]

    # print(numbers)
    # print(operator)

def parser (num1, num2, operator):
    if operator=='+':
        return  num1+num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 / num2


print(some_string)
print(split_into_arfim(some_string, list_of_operators))
    # for index in range(len(some_string)):
    #     if some_sting[index] in list_of_operators:
    #         positions.append(index)
    # # [1, 3, 5, 8]
    # numbers = [int(some_string[0:positions[0]])]
    # for i in positions:
    #     numbers.append(some_string[])
