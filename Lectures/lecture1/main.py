a = 123
b = 1.2
c = None
d = 'text'
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print(a, ' - ', b, ' - ', d)
print(f'{a} - {b} - {d}')

list = ['1', '2', '3']
print(list)

# print('Введите а: ')
# a=int(input())
# print('Введите b: ')
# b=int(input())
# print(a,"+",b,"=",a+b)


a = +12
b = -5
c = a + b
print(c)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = 1.3
b = 3
print(a * b)
print(round(a * b, 5))

print(a)
a += 5
print(a)

a = 1 > 4
print(a)

f = [1, 2, 3, 4]
print(f)
print(2 in f)
print(not 2 in f)
is_odd = not f[0] % 2 == 0
print(is_odd)

a = 2  # int(input())
b = 4  # int(input())
if a > b:
    print(a)
else:
    print(b)

if a < -100:
    print("negative")
elif a < 100:
    print('middle')
else:
    print('positive')

original = 12345
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original = original // 10
else:
    print(inverted)
    print('Enough')

# r = range(10)
# for i in range(5):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)
# for i in 'qwer - ty':
#     print (i)
text = "eat more of those sweet soft french breads and drink some tea"
print(len("even"))
print("and" in text)
# help (str)
print(text[5])
print(text[-1])
print(text[2:9])
print(text[9:-1])
numbers = [1, 2, 3, 4, 5]
print (f'{len(numbers)} len')
print (numbers)

numbers.append(6)
numbers.append(7)
print (numbers)
numbers.remove (1)
numbers.remove (2)
print (numbers)

def function_name(x):
    if x==1:
        return 'z'
    elif x==2.3:
        return 23
    else:
        return
arg=1
barg=2.3
carg=5
print (function_name(arg))
print (function_name(barg))
print (function_name(carg))
