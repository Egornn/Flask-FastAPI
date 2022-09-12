import random as rnd
import math as math
import sympy as s
import os as os


# Вычислить число c заданной точностью. Для удобства ввода с клавиатуры - указать число знаков после запятой (эквивалент -log(10, input())
def pi_approx(todigit):
    k2 = 13591409
    k3 = 640320
    k4 = 100100025
    k1 = 545140134
    k5 = 327843840
    k6 = 53360
    pi = 0
    for i in range(int(math.log(todigit, 10))):
        pi += (pow(-1, i) * (math.factorial(6 * i) * (k2 + i * k1)) / (
                pow(math.factorial(i), 3) * math.factorial(3 * i) * pow((8 * k4 * k5), i)))
    pi = (k6 * pow(k3, 0.5)) / pi
    return str(pi)[:todigit + 2]


to_digit_N = 10
print(f'С точностью до {pow(15, -to_digit_N)} значение pi равно этому значению {pi_approx(10)}')
print(f'Сравнение: сохраненное значение pi в библиотеке math. {str(math.pi)[:to_digit_N + 2]}')


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def all_prime_dividers(number):
    all_numbers = [i for i in range(2, number // 2 + 1)]
    all_numbers.append(number)
    is_prime = [True for x in range(len(all_numbers))]
    for i in range(len(all_numbers)):
        if is_prime[i]:
            for j in range(i + 1, len(all_numbers)):
                if is_prime[j]:
                    is_prime[j] = all_numbers[j] % all_numbers[i] > 0
    return [all_numbers[i] * is_prime[i] for i in range(len(is_prime)) if is_prime[i]]


def split_into_primes(number):
    prime_split = []
    possible = all_prime_dividers(number)
    for divider in possible:
        if number % divider == 0:
            prime_split.append(divider)
    return prime_split


print(split_into_primes(13))
print(split_into_primes(30))


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def remove_dupl(some_list):
    clean_list = []
    for number in some_list:
        if not number in clean_list:
            clean_list.append((number))
    return clean_list


random_list = [rnd.randint(-10, 11) for i in range(10)]

print('Оргинальный лист и далее два способа')
print(random_list)
non_repeated = set(random_list)
print(non_repeated)
print(remove_dupl(random_list))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
up = 10
down = -10
k = rnd.randint(1, 101)


def non_zero_int(lower, upper):
    lower, upper = min(lower, upper), max(lower, upper)
    if lower == (upper - 1):
        return lower
    number = 0
    while number == 0:
        number = rnd.randint(lower, upper)
    return number


def get_random_equation(k):
    equation = '0'
    new_element = 0
    if k == 0:
        return equation
    elif k == 1:
        return str(non_zero_int(down, up))
    else:
        equation = f'{non_zero_int(down, up)}x^{k - 1} '
        for i in range(k - 1):
            new_element = rnd.randint(down, up)
            if new_element > 0:
                equation += f'+{new_element}x^{k - 2 - i} '
            elif new_element < 0:
                equation += f'{new_element}x^{k - 2 - i} '
    equation = equation.replace("x^1", 'x')
    equation = equation.replace('x^0', '')
    if equation[0] == '+':
        equation = equation[1:]
    return equation


x = s.symbols('x')
expr = non_zero_int(down, up) * x ** (k - 1)
for i in range(k - 1):
    expr += rnd.randint(down, up) * x ** (k - 2 - i)
os.remove('33.txt')
f = open("33.txt", "x")
f.writelines(get_random_equation(k) + '\n')
f.writelines(str(expr))
f.close()

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
f = open("35-1.txt", "r")
first = s.sympify(f.read())
f.close()
f = open('35-2.txt', 'r')
second = s.sympify(f.read())
f.close()
print(first)
print(second)
print (first+second)


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
