import csv
from typing import Callable
import random
import json
from functools import wraps


def setup_guessing_game(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        random_number = int(input('Number to guess: '))
        tries = int(input('Number of guesses: '))
        if random_number < 1 or random_number > 100:
            random_number = random.randint(1, 100)
        if tries < 1 or tries > 10:
            tries = random.randint(1, 10)
        return func(random_number, tries)

    return wrapper


def json_logging(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(func.__name__, 'a', encoding='utf-8') as f_write:
            dictionary = {'args': args}
            for k, v in kwargs.items():
                dictionary[k] = v
            json.dump(dictionary, f_write)
            result = func(*args, **kwargs)
        return result

    return wrapper


@json_logging
def calculate_something(*args, **kwargs):
    res = sum(args)
    res = res + sum(kwargs.values())
    print(res)


def count(num: int):
    def repeat_decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
            return

        return wrapper

    return repeat_decorator


@count(10)
def print_something(text):
    print(text)


@count(2)
@json_logging
@setup_guessing_game
def guess_number(random_number, tries):
    """Guessing game"""
    is_guessed = False
    while tries > 0 and not is_guessed:
        guess = int(input('Guess a number: '))
        tries -= 1
        is_guessed = guess == random_number
    return is_guessed


def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if a == 0:
        x_1 = -c / b
        x_2 = x_1
        return x_1, x_2
    if discriminant < 0:
        return None, None
    else:
        x_1 = (-b - discriminant ** 0.5) / (2 * a)
        x_2 = (-b + discriminant ** 0.5) / (2 * a)
        return x_1, x_2


def save_them(func: Callable):
    def wrapper(*args):
        data = func(*args)
        with open('results.txt', mode='w', newline='', encoding='utf-8') as file_write:
            json.dump(data)

    return wrapper


def solve_them(func: Callable):
    def wrapper(*args):
        data = []
        with open(*args, 'r', encoding='utf-8') as csv_read:
            reader = csv.reader(csv_read)
            for row in reader:
                data.append([row, solve_quadratic(*map(int, row))])

        return data

    return wrapper


@save_them
@solve_them
def generate_csv(path):
    with open(path, "w", encoding='utf-8', newline='') as file_write:
        writer = csv.writer(file_write)
        for row in range(random.randint(1, 10)):
            writer.writerow([random.randint(-100, 100) for _ in range(3)])


if __name__ == "__main__":
    # result = guess_number()
    # print(result)
    # calculate_something(1, 2, 3, 4, 5, one=3, two=5, four=342)
    # print_something("random text")
    # print(guess_number())
    # print(solve_quadratic(11, 5, 1))
    # generate_csv("csv_data.csv")
    print(generate_csv('csv_data.csv'))
