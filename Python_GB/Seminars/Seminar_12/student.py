import csv
from statistics import mean


class NameValidator:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self._validate_name(value)
        setattr(obj, self.private_name, value)

    def _validate_name(self, value):
        if not isinstance(value, str):
            raise AttributeError('Name should be in text format')
        if not value.isalpha():
            raise AttributeError('Name should be of letters')
        if not value.istitle():
            raise AttributeError('Name should be capitalized')


class ItemValidator:

    def __init__(self, min_value: int = None, max_value: int = None):
        self._min_value = min_value
        self._max_value = max_value

    def __set_name__(self, owner, name):
        self.private_item = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_item)

    def __set__(self, obj, value: dict):
        self._validate_range(value)
        self._validate_items(value)

        setattr(obj, self.private_item, value)

    def _validate_range(self, value: dict):
        for value in value.values():
            for value_tuple in value:
                if not isinstance(value_tuple, int):
                    raise TypeError(f'Value {value_tuple} should be int')
                if value_tuple is not None and value_tuple < self._min_value:
                    raise ValueError(f'Value {value_tuple} Should be greater or equal than {self._min_value}')
                if value_tuple is not None and value_tuple > self._max_value:
                    raise ValueError(f'value {value_tuple} should be lower or equal than {self._max_value}')

    def _validate_items(self, value: dict):
        data = self._load_data()
        valid = 0
        for d in data:
            for v in value:
                if d == v:
                    valid += 1
        if valid != len(value):
            raise AttributeError(f'No item')

    def _load_data(self):
        data = {}
        file_name = 'school_items.csv'
        i = 0
        with open(file_name, encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for item in csv_reader:
                res = ''.join(item).strip()
                i += 1
                if i != 1:
                    data[res] = None
        return data


class Student:
    first_name: str = NameValidator()
    last_name: str = NameValidator()
    grades: dict = ItemValidator(2, 5)
    tests: dict = ItemValidator(0, 100)

    def __init__(self):
        self._first_name: str = ''
        self._last_name: str = ''
        self._grades: dict[str: tuple] = {}
        self._tests: dict[str: tuple] = {}

    def __str__(self):
        grades = '\n'.join(f'{k}: {v}' for k, v in self._grades.items())
        tests = '\n'.join(f'{k}: {v}' for k, v in self._tests.items())
        avg_test_results = '\n'.join(f'{k}: {v}' for k, v in self._avg_tests().items())
        avg_grades_result = '\n'.join(f'{k}: {v}' for k, v in self._avg_grades().items())
        return f'Student:\n{self._first_name} {self._last_name}' \
               f'\n\nGrades by subjects:\n{grades}' \
               f'\n\nGrades by tests:\n{tests}' \
               f'\n\nAverage test grade:\n{avg_test_results}' \
               f'\n\nTotal average:\n{avg_grades_result}'

    def _avg_tests(self):
        avg_results = dict()
        for key, value in self._tests.items():
            avg_results[key] = round(mean(value), 1)
        return avg_results

    def _avg_grades(self):
        avg_result = 0
        for values in self._grades.values():
            avg_result += mean(values)
        return {'Total average': round(avg_result / len(self._grades.values()), 1)}


if __name__ == '__main__':
    student = Student()
    student.first_name = 'John'
    student.last_name = 'Jameson'
    student.grades = {'Math': (4, 5, 3), 'Physics': (3, 3, 4, 5), 'Biology': (3, 5, 5, 5)}
    student.tests = {'English': (20, 40, 100), 'Chemistry': (0, 50, 80)}
    print(student)
