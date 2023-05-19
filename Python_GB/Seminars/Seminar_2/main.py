import decimal
import string
from cmath import sqrt
from math import gcd
import fractions

decimal.getcontext().prec = 50

BASES = {"b": 2, "o": 8, "h": 16}
ALPHABET = list(string.ascii_lowercase)
PI = decimal.Decimal("3.14159265358979323846264338327950288419716939937510")
DEFAULT_BASE = 10


def dec_to_bases(number_to_convert: int, bases: dict) -> list:
    different_bases = []
    for base in bases:
        number = number_to_convert
        number_as_list = []
        while number >= bases[base]:
            number_as_list.append(str(number % bases[base]))
            number = number // bases[base]
        number_as_list.append(str(number))
        number_as_list.reverse()
        for i in range(len(number_as_list)):
            number = int(number_as_list[i])
            if number > DEFAULT_BASE:
                number_as_list[i] = ALPHABET[number - DEFAULT_BASE]
        different_bases.append(f'0{base}{"".join(number_as_list)}')
    return different_bases


def circle_area(radius: float, pi: decimal.Decimal) -> decimal.Decimal:
    return decimal.Decimal(radius) ** 2 * pi


def circle_length(radius: float, pi: decimal.Decimal) -> decimal.Decimal:
    return 2 * decimal.Decimal(radius) * pi


def solve_square_equation(a: complex, b: complex, c: complex) -> list:
    discriminant = b ** 2 - 4 * a * c
    root_1 = (-b - sqrt(discriminant)) / (2 * a)
    root_2 = (-b + sqrt(discriminant)) / (2 * a)
    return [root_1, root_2]


def simplify(fraction: list) -> list:
    common_divisor = gcd(fraction[0], fraction[1])
    fraction[0], fraction[1] = fraction[0] / common_divisor, fraction[1] / common_divisor
    return fraction


def fraction_sum(fraction_1: str, fraction_2: str) -> str:
    frac_1 = [int(x) for x in fraction_1.split("/")]
    frac_2 = [int(x) for x in list(fraction_2.split("/"))]
    frac_1[0], frac_2[0] = frac_1[0] * frac_2[1], frac_2[0] * frac_1[1]
    frac_1[1], frac_2[1] = frac_1[1] * frac_2[1], frac_2[1] * frac_1[1]
    fraction_result = [frac_1[0] + frac_2[0], frac_1[1]]
    return f"{fraction_result[0]}/{fraction_result[1]}"


def fraction_multiplication(fraction_1: str, fraction_2: str) -> str:
    frac_1 = [int(x) for x in fraction_1.split("/")]
    frac_2 = [int(x) for x in fraction_2.split("/")]
    fraction_result = [frac_1[0] * frac_2[0], frac_1[1] * frac_2[1]]
    return f"{fraction_result[0]}/{fraction_result[1]}"


def atm() -> None:
    def interest_on_balance(current_balance: float, count_of_dw: int) -> list:
        count_of_dw = (count_of_dw + 1) % interest_occurrence
        if count_of_dw == 0:
            current_balance = balance * (1 + interest)
        return [current_balance, count_of_dw]

    def current_balance_print(balances: float) -> None:
        print(f"Current balance is {balances}")

    def wealth_tax(current_balnce: float, thresh: float, tax_rate: float) -> float:
        if current_balnce > thresh:
            current_balnce = current_balnce * (1 - tax_rate)
        return current_balnce

    balance = 0
    threshhold = 5_000_000_000
    tax = .1
    withdrawal_fee = .015
    min_fee = 30
    max_fee = 600
    count_of_deposit_withdrawal = 0
    interest_occurrence = 3
    interest = .03
    while True:
        command = input('Available options are "Deposit", "Withdraw", "Exit": ').lower()
        match command:
            case "deposit":
                correct_input = False
                while not correct_input:
                    deposit = input("Please input multiple of 50 to deposit: ")
                    correct_input = deposit.isdigit() and (int(deposit) % 50 == 0) and int(deposit) > 0
                    balance = wealth_tax(balance, threshhold, tax)
                    if not correct_input:
                        print("Incorrect input")
                        current_balance_print(balance)
                balance += int(deposit)

                after_interest_list = interest_on_balance(balance, count_of_deposit_withdrawal)
                balance, count_of_deposit_withdrawal = after_interest_list[0], after_interest_list[1]
                current_balance_print(balance)

            case "withdraw":
                correct_input = False
                while not correct_input:
                    withdraw = input("Please input sum to withdraw: ")
                    balance = wealth_tax(balance, threshhold, tax)
                    correct_input = withdraw.isdecimal() and int(withdraw) > 0
                    if correct_input:
                        fee = min(max(min_fee, int(withdraw) * withdrawal_fee), max_fee)
                        if (int(withdraw) + fee < balance):
                            withdraw = int(withdraw) + fee
                        else:
                            correct_input = False
                    if not correct_input:
                        print("incorrect input")
                        current_balance_print(balance)
                balance -= int(withdraw)
                after_interest_list = interest_on_balance(balance, count_of_deposit_withdrawal)
                balance, count_of_deposit_withdrawal = after_interest_list[0], after_interest_list[1]
                current_balance_print(balance)

            case "exit":
                return

            case _:
                balance = wealth_tax(balance, threshhold, tax)
                print("Incorrect command")
                current_balance_print(balance)


print("Task 3: to Bin & Oct")
number_to_check = 11
print(dec_to_bases(number_to_check, BASES))
print([bin(number_to_check), oct(number_to_check), hex(number_to_check)])

print("Task 4: Area & Length of a Circle")
radius = 999
print(f"for Radius of {radius} - Length is {circle_length(radius, PI)}, Area is {circle_area(radius, PI)}")

print("Task 5: Square Equation")
first_coefficient, second_coefficient, third_coefficient = complex(2, 1), complex(-2, 1), complex(1, -1)
print(f"{first_coefficient}x^2+({second_coefficient})x+({third_coefficient})=0 has roots: \
{solve_square_equation(first_coefficient, second_coefficient, third_coefficient)}")
first_coefficient, second_coefficient, third_coefficient = 1, 1, 10
print(f"{first_coefficient}x^2+({second_coefficient})x+({third_coefficient})=0 has roots: \
{solve_square_equation(first_coefficient, second_coefficient, third_coefficient)}")

print("Task 6: ATM")
atm()

print("Task 7: to Hex")
number_to_check = 255
print(dec_to_bases(number_to_check, BASES))
print([bin(number_to_check), oct(number_to_check), hex(number_to_check)])

print("Task 8: Fraction")
fract_1 = "2/5"
fract_2 = "4/3"
print(fraction_sum(fract_1, fract_2), fraction_multiplication(fract_1, fract_2))
print(fractions.Fraction(fract_1) + fractions.Fraction(fract_2), \
      fractions.Fraction(fract_1) * fractions.Fraction(fract_2))
