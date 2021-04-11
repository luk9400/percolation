from random import random
from math import sqrt


def init_matrix(L, p):
    return [1 if random() < p else 0 for _ in range(L * L)]


def print_matrix(matrix):
    L = int(sqrt(len(matrix)))
    for i in range(0, len(matrix), L):
        print(matrix[i : i + L])


def up(i, L):
    return i - L if i >= L else None


def down(i, L):
    return i + L if i <= L * L - L else None


def right(i, L):
    return i + 1 if (i + 1) % L != 0 else None


def left(i, L):
    return i - 1 if i % L != 0 else None


def burn(matrix):
    def dfs(matrix, node, L):
        path = [node]

        while len(path):
            s = path[-1]
            if s > L * L - L:
                return True

            path.pop()

            if matrix[s] != 2:
                matrix[s] = 2

            for neighbour in [
                up(s, L),
                down(s, L),
                right(s, L),
                left(s, L),
            ]:
                if neighbour != None and matrix[neighbour] == 1:
                    path.append(neighbour)

        return False

    L = int(sqrt(len(matrix)))

    for node in range(L):
        if matrix[node] == 1:
            if dfs(matrix, node, L):
                return True

    return False


def hoshen_kopelman(matrix):
    L = int(sqrt(len(matrix)))
    M = {}
    k = 3

    for i in range(len(matrix)):
        if matrix[i] == 1 or matrix[i] == 2:
            nb_up = up(i, L)
            nb_left = left(i, L)

            k_up = matrix[nb_up] if nb_up != None else 0
            k_left = matrix[nb_left] if nb_left != None else 0

            if k_up == 0 and k_left == 0:
                matrix[i] = k
                M[k] = 1
                k += 1
            elif k_up != 0 and k_left != 0:
                k_1, k_2 = (k_up, k_left) if M[k_up] > 0 else (k_left, k_up)

                M_1 = M[k_1]
                while M_1 < 0:
                    k_1 = -M_1
                    M_1 = M[-M_1]

                M_2 = M[k_2]
                while M_2 < 0:
                    k_2 = -M_2
                    M_2 = M[-M_2]

                if k_1 != k_2:
                    matrix[i] = k_1

                    M[k_1] = M_1 + M_2 + 1
                    M[k_2] = -k_1
                else:
                    matrix[i] = k_1
                    M[k_1] = M_1 + 1
            elif k_up != 0 or k_left != 0:
                k_0 = k_up if k_up != 0 else k_left

                M_0 = M[k_0]
                while M_0 < 0:
                    k_0 = -M_0
                    M_0 = M[-M_0]

                matrix[i] = k_0

                M[k_0] = M_0 + 1

    return (matrix, M)


L = 10
mat = init_matrix(L, 0.57)
print_matrix(mat)
print(burn(mat))
print_matrix(mat)
print()

clusters, M = hoshen_kopelman(mat)
print_matrix(clusters)
print(sum(0 if i == 0 else 1 for i in mat))
print(sum(0 if i < 0 else i for i in M.values()))
print(M)
