# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in range(8):
    x = i % 2 == 0
    y = i % 4 // 2 == 0
    z = i // 4 == 0
    print(f'For x={x}, y={y}, z=g{z} the required statement is {(not (x or y or z)) == (not x and not y and not z)}')
