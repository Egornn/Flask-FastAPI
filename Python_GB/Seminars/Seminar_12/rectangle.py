class Rectangle:
    __slots__ = ('_a', '_b')

    def __init__(self, a: int, b: int = None):
        self._a = a
        self._b = b if b is not None else a

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError('Should be positive')

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError('Sides should be positive')

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        return f'Rectangle  {self.a} x {self.b}'


if __name__ == '__main__':
    rect_1 = Rectangle(2, 5)
    rect_2 = Rectangle(5, 10)
    print(rect_1.a)

print(rect_1.b)
rect_1.a = 10
print(rect_1)
print(rect_2)
print(f'{rect.perimeter()= } {rect.area()= }')
print(f'{rect_1.perimeter()= } {rect_1.area()= }')
res_sum = rect_1 + rect_2
print(res_sum.a, res_sum.b)
res_sub = rect_1 - rect_2
print(res_sub.a, res_sub.b)
