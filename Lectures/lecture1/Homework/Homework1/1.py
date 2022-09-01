# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number=input('Write day of the week: ')
if number ==6 or number ==7:
    print('Weekend')
else:
    print('Workday')