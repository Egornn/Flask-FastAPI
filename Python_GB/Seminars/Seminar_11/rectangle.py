class Rectangle:
    """Rectangular class with perimeter and area."""

    def __init__(self, a: int, b: int = None):
        """Initialize a rectangle a x b."""
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        """Perimeter."""
        return 2 * (self.a + self.b)

    def area(self):
        """Method to get an area."""
        return self.a * self.b

    def __add__(self, other):
        """Redefined method of sum of two rectangle."""
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        """Redefined method of sub of two rectangle."""
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        """String representation"""
        return f'Rectangle {self.a} x {self.b}'


if __name__ == '__main__':
    rect_1 = Rectangle(2, 5)
    rect_2 = Rectangle(5, 10)
    print(rect_2)
    print(f'{rect.perimeter()= } {rect.area()= }')
    print(f'{rect_1.perimeter()= } {rect_1.area()= }')
    res_sum = rect_1 + rect_2
    print(res_sum.a, res_sum.b)
    res_sub = rect_1 - rect_2
    print(res_sub.a, res_sub.b)
