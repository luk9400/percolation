from random import random
from math import sqrt


def init_matrix(L, p):
    return [1 if random() < p else 0 for _ in range(L * L)]


def print_matrix(matrix):
    L = int(sqrt(len(matrix)))
    for i in range(0, len(matrix), L):
        print(matrix[i : i + L])


def burn(matrix):
    def dfs(matrix, node, L):
        def up(i):
            return i - L if i >= L else None

        def down(i):
            return i + L if i <= L * L - L else None

        def right(i):
            return i + 1 if (i + 1) % L != 0 else None

        def left(i):
            return i - 1 if i % L != 0 else None

        if node > L * L - L:
            return True

        for neighbour in [up(node), down(node), right(node), left(node)]:
            if neighbour != None and matrix[neighbour] == 1:
                matrix[neighbour] = 2
                if dfs(matrix, neighbour, L):
                    return True

        return False

    L = int(sqrt(len(matrix)))

    return any([dfs(matrix, i, L) for i in range(L)])


L = 100
mat = init_matrix(L, 0.57)
print_matrix(mat)
print(burn(mat))

