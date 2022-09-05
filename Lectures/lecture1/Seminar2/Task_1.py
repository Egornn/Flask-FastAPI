# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#    - Для N = 5: 1, -3, 9, -27, 81
n = int(input())
string = ""
for i in range(0, n-1):
    string += str((-3) ** i) + ", "
string += str(pow(-3,(n-1)))
print(string)

some_list = []
for i in range(n):
    some_list.append((-3) ** i)
print(*some_list, sep=', ')



