
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in range(8):
    if i%2==0:
        x=False
    else:
        x=True
    if i%4//2==0:
        y=False
    else:
        y=True
    if i//4==0:
        z=False
    else:
        z=True
    print (f'For x={x}, y={y}, z=g{z} the required statement is {(not (x or y or z)) == (not x and not y and not z) }')
