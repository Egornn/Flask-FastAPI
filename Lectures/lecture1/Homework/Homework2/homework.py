import random


# 15. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def SumInt(number):
    number = number // 1
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return int(sum)


n = (input('Input a float '))
number = float(n) * pow(10, len(n) - n.find('.') - 1)
sum = SumInt(number)
print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Factorial to N: '))
myCuteUwUList = []
if n > 0:
    myCuteUwUList.append(1)
for i in range(2, n + 1):
    myCuteUwUList.append(i * myCuteUwUList[i - 2])
print(myCuteUwUList)

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input('input up to which n '))
dict = {}
for i in range(1, n + 1):
    dict[i] = pow(1 + 1 / i, i)
print(dict)

# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input())
answer = []
for i in range(n):
    answer.append(random.randint(-n, n))
text = open('text.txt', 'r')
mult = 1

for i in text.read():
    mult = mult * answer[int(i)]
print(answer)  # 1 2 4
print(mult)

#18. перемешать список