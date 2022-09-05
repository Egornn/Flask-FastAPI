# Вводится количество чисел N, а потом все N чисел. Найти ср. арифм.
# с последней цифрой 7 и положительное число

n = int(input("Сколько чсел? "))
sum = 0
counter = 0
mylist = []
for i in range(0, n ):
    mylist.append(int(input(f'Введите {i} число ')))
    if (mylist[i] % 10 == 7) and (mylist[i] > 0):
        sum += mylist[i]
        counter += 1
print(mylist)
print(sum / counter)
