from random import random
from math import sqrt
from sys import argv
import json


def init_matrix(L, p):
    return [1 if random() < p else 0 for _ in range(L * L)]


def print_matrix(matrix):
    L = int(sqrt(len(matrix)))
    for i in range(0, len(matrix), L):
        print(matrix[i : i + L])


def up(i, L):
    return i - L if i >= L else None


def down(i, L):
    return i + L if i < L * L - L else None


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
                left(s, L),
                right(s, L),
                down(s, L),
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


def test(L, T, p_0, p_k, dp):
    probabilities = [p_0]
    i = p_0 + dp
    while i <= p_k:
        probabilities.append(i)
        i += dp

    ave = []
    print(f"L: {L}, T: {T}")
    for p in probabilities:
        print(f"p: {p}")
        s_max = 0
        p_flow = 0
        clusters_dist = {}

        for _ in range(T):
            matrix = init_matrix(L, p)
            p_flow += int(burn(matrix))
            _, M = hoshen_kopelman(matrix)

            max_cluster = 0
            for value in M.values():
                if value > 0:
                    if value > max_cluster:
                        max_cluster = value

                    if value in clusters_dist:
                        clusters_dist[value] += 1
                    else:
                        clusters_dist[value] = 1
            s_max += max_cluster

        ave.append({"p": p, "p_flow": p_flow / T, "avg_s_max": s_max / T})
        with open(f"./tests/Dist_p{p}L{L}T{T}.txt", "w") as f:
            for key, value in sorted(clusters_dist.items()):
                f.write(f"{key}  {value}\n")

    with open(f"./tests/Ave_L{L}T{T}.txt", "w") as f:
        for i in ave:
            f.write(f"{i['p']}  {i['p_flow']}  {i['avg_s_max']}\n")


def matrix_to_csv(matrix, filename):
    with open(filename, "w") as f:
        L = int(sqrt(len(matrix)))
        for i in range(0, len(matrix), L):
            f.write(";".join(map(str, matrix[i : i + L])))
            f.write("\n")


if __name__ == "__main__":
    if len(argv) >= 2:
        with open(argv[1], "r") as file:
            config = json.loads(file.read())
            test(**config)

    # test(100, 10000, 0.592746, 0.6, 1  )

    # L = 10
    # p = 0.6
    # matrix = init_matrix(L, p)
    # print_matrix(matrix)
    # matrix_to_csv(matrix, f"./tests/clearL{L}p{p}.csv")
    # print(burn(matrix))
    # print_matrix(matrix)
    # matrix_to_csv(matrix, f"./tests/burntL{L}p{p}.csv")
    # print()
    # clusters, M = hoshen_kopelman(matrix)
    # print_matrix(clusters)
    # print(M)
    # matrix_to_csv(matrix, f"./tests/clustersL{L}p{p}.csv")
