some_string = '9*(0+(4-2.5)/(3-2))'
list_of_operators = ['-', '+', '*', '/']


def subdivide_by_brackets(some_string):
    if "(" in some_string:
        some_string = some_string.replace(some_string[some_string.index('('):],
                                          subdivide_by_brackets(some_string[some_string.index('(') + 1:]))
    if ")" in some_string:
        some_string = some_string.replace(some_string[0:some_string.index(')') + 1],
                                          str(split_into_arfim(some_string[0:some_string.index(')')])))
        return some_string
    return split_into_arfim(some_string)


def split_into_arfim(some_sting, list_of_operators=['-', '+', '*', '/']):
    operator = []
    numbers = []
    temp = ''
    for char in some_sting:
        if not char in list_of_operators:
            temp += char
        else:
            operator.append(char)
            try:
                numbers.append(float(temp))
            except:
                print('stupid symbol')
                exit()
            temp = ''
    numbers.append(float(temp))
    while len(numbers) > 1:
        if '*' in operator:
            index = operator.index('*')
            temp = parser(numbers[index], numbers[index + 1], '*')
            numbers[index] = temp
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
        del (numbers[index + 1])
        del (operator[index])
    return numbers[0]


def parser(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/':
            try:
                return num1 / num2
            except:
                print('Division by zero')
                exit()
    except:
        print('Unexpected vlaues')
        exit()


print(some_string)
print(subdivide_by_brackets(some_string))

# Задача 43: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

some_list = [1, 2, 3, 5, 1, 5, 3, 10]


def remove_repeated(myCuteUwUList):
    answer = {}
    for i in myCuteUwUList:
        answer[i] = answer.get(i, 0) + 1
    unic_list = []
    for i in answer:
        if answer[i] == 1:
            unic_list.append(i)
    return unic_list


print()
print(some_list)
print(remove_repeated(some_list))

# Задача FOOTBALL
print()
n = 3
inp = ['Спартак;9;Зенит;10', 'Локомотив;12;Зенит;3', 'Спартак;8;Локомотив;15']


def scoring(a, b):
    a, b = int(a), int(b)
    if a > b:
        return [1, 0, 0, 3]
    elif b > a:
        return [0, 0, 1, 0]
    elif a == b:
        return [0, 1, 0, 1]


def match_parser(match):
    one_match = match.split(';')
    return {one_match[0]: scoring(one_match[1], one_match[3]), one_match[2]: scoring(one_match[3], one_match[1]), }


def match_result(season, match):
    one_match = match_parser(match)
    for key in one_match:
        season[key] = [x+y for (x,y) in zip(season.get(key, [0,0,0,0]), one_match[key])]
    return season


def full_season(all_matches):
    season = {}
    for one_match in all_matches:
        season = match_result(season, one_match)
    return season


print(full_season(inp))
