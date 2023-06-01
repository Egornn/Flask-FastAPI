from math import sqrt

# 1 input to dict
a, b, c, *d = input("Write 4+ numbers divided by /:  ").split('/')
d = tuple(d)
print({b: a, c: d})

# 2 text to dict
text = "Random text is here"
dict_text = {letter: ord(letter) for letter in text}
print(dict_text)

# 3 Iterators
iter_list = iter(dict_text.items())
for i in range(5):
    print(next(iter_list))

# 4 Generator of evens
even_numbers = (n for n in range(101) if n % 2 == 0 and n % 8 != 0)


# 5 FizzBuzz generator
def fizz_buzz(num):
    for n in num:
        str_output = ""
        if n % 3 == 0:
            str_output += "Fizz"
        if n % 5 == 0:
            str_output += "Buzz"
        if str_output == '':
            str_output = str(n)
        yield str_output


for fizzbuzz in fizz_buzz(range(101)):
    print(fizzbuzz)


# 6 Multiplication table
def mult_table():
    lower = 2
    upper = 10
    column = 4
    print(' ', end='')
    print(*(f'{k:>} x {j:>2} = {k * j:>2}\n\n' if j == upper and k == i + column - 1 else \
                f'{k:>} x {j:>2} = {k * j:>2}\n' if k == i + column - 1 else \
                    f'{k:>} x {j:>2} = {k * j:>2}\t\t' \
            for i in range(lower, upper, column)
            for j in range(lower, upper + 1)
            for k in range(i, i + column)))


mult_table()


# 7 Primes
def prime_generator(num_generated):
    num = 2
    while num_generated > 0:
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            num_generated -= 1
            yield num
        num += 1


for i, num in enumerate(prime_generator(10), start=1):
    print(f'{i} prime -> {num}')

# 8 Unpack path

path = "C:/Users/Egor/Desktop/SNAP.lnk"


def path_conversion(path):
    *full_path, file = path.split('/')
    name, extent = file.split('.')
    return ("/".join(full_path), name, extent)


print(path_conversion(path))

# 9
names = ["Ann", "Bob"]
salary = [1000, 2020]
bonus = ["12%", "5.05%"]
print(bonus[0][:-1])

payments = {i: j * float(k[:-1]) / 100 for i, j, k in zip(names, salary, bonus)}
print(payments)


# 10 Fibo
def fibo(num_range):
    n_2, n_1 = 1, 1
    for i in range(1, num_range):
        if i == 1 or i == 2:
            yield 1
        else:
            yield n_2 + n_1
            n_2, n_1 = n_1, n_1 + n_2


for i, num in enumerate(fibo(10), start=1):
    print(f'{i} Fibo -> {num}')
