import inspect
from Seminars.Seminar_2.main import atm


def agrs_to_dict(**kwargs):
    dict_args = {}
    for key, val in kwargs.items():
        dict_args[key] = val
    return dict_args


def symbols(str_input: str) -> dict:
    answer = {}
    input_list = sorted(str_input.split())
    for i in range(int(input_list[0]), int(input_list[1]) + 1):
        answer[chr(i)] = i
    return answer


def bubble_sort(numbers_list: list) -> None:
    for j in range(len(list_to_sort) - 1, 0, -1):
        for i in range(0, j):
            if numbers_list[i] > numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]


def transform_s_variables():
    local_var = inspect.currentframe().f_back.f_locals
    updated_var = {}
    for name, val in local_var.items():
        if isinstance(val, str):
            if val.lower() == 's':
                pass
            if val.lower()[-1] == 's':
                updated_var[name[-1]] = val
                local_var[name] = None


# 2 symbols code
text = "sdfghjkl; a"
print((lambda x: sorted(map(ord, x)))(text))

# 3 symbols in middle
text = "32 41"
print(symbols(text))

# 4 Bubble sort
list_to_sort = [1111, 2, 34, 6, 7, 1, 5]
bubble_sort(list_to_sort)
print(list_to_sort)

# 5 names
names_list = ["Al", 'By']
payment_list = [10, 20]
bonus_list = ['10%', "12.1%"]
print((lambda x, y, z: {name: payment * float(bonus.split("%")[0]) / 100 for name, payment, bonus in zip(x, y, z)})(
    names_list, payment_list, bonus_list))

# 6 sum in between indexes
to_sum = [1, 2, 3, 4, 5]
min_index_1 = -3
max_index_1 = 46
min_index_2 = 3
max_index_2 = 1

print(
    (lambda num_list, ind_1, ind_2: sum(num_list[max(0, min(ind_1, ind_2)): max(len(num_list) - 1, max(ind_1, ind_2))]))
    (to_sum, min_index_1, max_index_1))
print(
    (lambda num_list, ind_1, ind_2: sum(num_list[max(0, min(ind_1, ind_2)): max(len(num_list) - 1, max(ind_1, ind_2))]))
    (to_sum, min_index_2, max_index_2))

# 7
companies = {"a": [1, 2, -4], "b": [-3, 1, 4]}
print(all(map((lambda val: sum(val) > 0), (companies.values()))))

# 8 S names
s = "some string"
abc = "another string"
test_var = "test"
xyzs = "xyz string"
number = 42

transform_s_variables()
print(locals())

# 9 dictionary
print(agrs_to_dict(cat=12, dog="spome stringk,", FU=3))

# 10 new ATM
atm()
