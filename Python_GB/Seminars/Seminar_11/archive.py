class Archive:
    """Save data in numbers(list) and values(list)."""
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """Redefine new to save args."""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        """Define method of initializing class."""
        self.number = number
        self.value = value

    def __repr__(self):
        """Output info for development"""
        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        """Redefine string form"""
        return f'#: {self.number}, value: "{self.value}"'


if __name__ == '__main__':
    a_1 = Archive(1, "One")
    a_2 = Archive(2, "Two")
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3, "Three")
    print(f'{a_3.numbers} {a_3.values}')
    help(a_1)
    print(a_1.__repr__())
    print(f'{a_1 = }')
    print(a_1)
