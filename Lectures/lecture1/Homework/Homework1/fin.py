# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('Please give a coordinate X:'))
y = float(input('Please give a coordinate Y:'))

if x > 0 and y > 0:
    print('The point in the 1 quarter')
elif x < 0 and y > 0:
    print('The point in the 2 quarter')
elif x < 0 and y < 0:
    print('The point in the 3 quarter')
else:
    print('The point in the 4 quarter')
