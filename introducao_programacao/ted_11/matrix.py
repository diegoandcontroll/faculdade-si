import random

class Matrix:
    def __init__(self, size=10):
        self.size = size
        self.matrix = [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

    def sum_values(self):
        total = sum(sum(row) for row in self.matrix)
        print(f"Sum of all values in the matrix: {total}")
        return total

    def create_tripled_matrix(self):
        tripled_matrix = [[value * 3 for value in row] for row in self.matrix]
        return tripled_matrix

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def print_tripled_matrix(self, tripled_matrix):
        for row in tripled_matrix:
            print(row)

matrix = Matrix()
print("\nMatrix A:")
matrix.print_matrix()
matrix.sum_values()
tripled_matrix = matrix.create_tripled_matrix()
print("\nMatrix B (values of Matrix A * 3):")
matrix.print_tripled_matrix(tripled_matrix)
