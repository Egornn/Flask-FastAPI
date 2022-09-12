import math as math

def pi_approx(todigit):
    k2 = 13591409
    k3 = 640320
    k4 = 100100025
    k1 = 545140134
    k5 = 327843840
    k6 = 53360
    pi = 0
    for i in range(int(math.log(todigit,10))):
        pi += (pow(-1, i) * (math.factorial(6 * i) * (k2 + i * k1)) / (
                pow(math.factorial(i), 3) * math.factorial(3 * i) * pow((8 * k4 * k5), i)))
    pi = (k6 * pow(k3, 0.5)) / pi
    return str(pi)[:todigit+2]
to_digit_N=10
print(f'С точностью до {pow(15,-to_digit_N)} значение pi равно этому значению {pi_approx(10)}')
print(f'Сравнение: сохраненное значение pi в библиотеке math. {str(math.pi)[:to_digit_N+2]}')
