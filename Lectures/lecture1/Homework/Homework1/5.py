# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


x1=float(input('What is the coordinate X for the first point: '))
y1=float(input('What is the coordinate Y for the first point: '))
x2=float(input('What is the coordinate X for the second point: '))
y2=float(input('What is the coordinate Y for the second point: '))

print (f'The distance between ({x1}, {y1} and ({x2},{y2}) is {pow(pow(x1-x2,2)+pow(y1-y2,2),0.5)}')