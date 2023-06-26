import time


class MyString(str):
    """Expandable class str."""

    def __new__(cls, value: str, name: str):
        """Extend with value & name."""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance

    def __str__(self):
        """String representation"""
        return self + " " + f'{self.name} {self.created_at}'


if __name__ == '__main__':
    mystr = MyString('SOME string', 'aadditional parameter')
    print(mystr.name)
    print(mystr.created_at)
    print(mystr)
    print(mystr.upper())
    help(mystr)
    help(MyString)
