# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('What is the quarter: '))

if quarter == 1:
    print('The possible range for x is (0, +∞) and or y is (0, +∞)')
elif quarter == 2:
    print('The possible range for x is (-∞, 0) and or y is (0, +∞)')
if quarter == 3:
    print('The possible range for x is (-∞, 0) and or y is (-∞, 0)')
elif quarter == 4:
    print('The possible range for x is (0, +∞) and or y is (-∞, 0)')
