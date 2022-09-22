x = 0
y = 0


def summa():
    global x
    global y
    return x + y


def calculator(a, b, operator):
    return operator(a, b)

def init(a, b):
    global x
    global y
    x = a
    y = b
