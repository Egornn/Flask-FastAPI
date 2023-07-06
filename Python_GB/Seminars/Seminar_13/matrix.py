class CustomException(Exception):
    pass


class LevelError(CustomException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Access restricted {self.value}'


class AccessError(CustomException):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f'User with id: {self.user_id} and name: {self.name} does not exist'


class SideError(CustomException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Length should be positive: {self.value}'


class TransparentError(CustomException):
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __str__(self):
        return f'Cannot transpose. It has {self.col} rows and {self.row} columns'
