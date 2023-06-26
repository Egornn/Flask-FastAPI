class Matrix:
    """Matrix class with math operation over them."""

    def __init__(self, list_of_lists: list[list[int]]):
        """Initializing a  list[list[int]]."""
        self.list_of_lists = list_of_lists

    def __str__(self):
        """Output by lines."""
        result = ''
        for row in self.list_of_lists:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):
        """Redefine a method to compare matrix."""
        return True if self.list_of_lists == other.list_of_lists else False

    def __add__(self, other):
        """Sum of matrix. """
        result = []
        row = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_2 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)
    if matrix_1 == matrix_2:
        print('True')
    else:
        print('False')
