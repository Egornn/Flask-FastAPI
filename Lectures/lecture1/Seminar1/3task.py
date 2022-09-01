# 31. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#
#     *Примеры:*
#
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, , 4, 5
n = int(input("Введите N:"))
string = ''
for i in range(-n, n):
    string = string + str(i) + ', '
print(string + str(n))

# list = []
# for i in range(-n, n):
#   list.append (i)
#   print(i, end=", ")
# print(n)
