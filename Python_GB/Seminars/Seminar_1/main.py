def is_leap(year):

    # year = int(input())
    leap_base=4
    leap_skip=100
    leap_new=400
    leap_start = 1582
    message=""
    if year<leap_start:
        message='No calendar yet'

    else:
        if year % leap_new == 0:
            message="Leap"
        elif year%leap_skip==0:
            message=('Not leap')
        elif year%leap_base==0:
            message="Leap"
        else:
            message=('Not leap')
    print(message)

def three_digit(number):
    result = 0
    first_bound=10
    second_bound=100
    third_bound = 1000
    if 0< number < first_bound:
        result=number**2
    elif number<second_bound:
        result=(number%10)*(number//10)
    elif number<third_bound:
        result = 100*(number%10)+10*((number//10)%10)+number//100
    print(result)

def draw_tree (n):
    for i in range(n):
        empty=" "*(n-1-i)
        star="*"*(2*(i)+1)
        print(empty+star+empty)

def multiplication_table():
    first_block=["2","3","4","5"]
    second_block=["6","7","8","9"]
    blocks=[first_block,second_block]
    indent="    "
    for block in blocks:
        for i in range (2, 11):
            i=str(i)
            line=""
            for n in block:
                multi=int(n)*int(i)
                if multi<10:
                    multi = f" {str(multi)}"
                else: multi = str(multi)
                if len(i)<2: i=" "+i
                line+=f"{n} X{i}={multi}"
                if n!=block[-1]:
                    line+=indent
            print(line)
        print()

def is_triangle(a,b,c):
    type='a regular'
    if a<=0 or b<=0 or c<=0:
        print("Triangle does not exists")
        return
    if a==b and b==c:
        type= 'an equiangular'
    elif a==b or b==c or c==a:
        type = "an isoscelar"

    if a>=(b+c) or b>=(a+c) or c>=(a+b):
        print('Triangle does not exists')
    else:
        print(f"Triangle exists and {type}")

def is_prime():
    is_input_correct=False
    while not is_input_correct:
        num=input("Input the number to check: ")
        try :
            num=int(num)
            if num<1 or num> 100_000:
                print("Please keep the number between 1 and 100 000")
                continue
            is_input_correct=True
        except:
            print("Incorrect input")
    for i in range(2,int(num**0.5)):
        if num%i==0:
            print("Not prime")
            return
    print('Prime')

def guess_the_number(limit_lower, limit_upper):
    import random as rnd
    goal=rnd.randint(limit_lower, limit_upper)
    guess_attempts=0
    is_solved=False
    while not is_solved:
        guess_attempts+=1
        guess=int((limit_upper+limit_lower)/2)
        print(f"#{guess_attempts} I guess {guess} since I know that number is in between {limit_lower} and {limit_upper}")
        if guess==goal:
            is_solved=True
        elif guess>goal:
            print(f"My number is smaller than {guess}")
            limit_upper=guess
        elif guess<goal:
            print(f"My number is bigger than {guess}")
            limit_lower = guess
    print(f"Your guess {guess} is correct! I thought of {goal} and it took you only {guess_attempts} tries!")




is_leap(int(input('Введите год: ')))
three_digit(int(input('Введите число от 1 до 999\n')))
draw_tree(int(input("How many lines in tree?: ")))
multiplication_table()
is_triangle(3,3,3)
is_prime()
guess_the_number(1,1000)