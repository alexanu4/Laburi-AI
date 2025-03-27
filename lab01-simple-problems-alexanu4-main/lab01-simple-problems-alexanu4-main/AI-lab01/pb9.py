def pb9(n, m, a, perechi):  # complexitate timp si spatiu teta(m*n)
    # n = int(input("n="))
    # m = int(input("m="))
    # a = []
    # print("Introduceti numerele:\n")
    # for i in range(n):  # citim matricea linie cu linie
    #     linie = input()
    #     a.append([int(x) for x in linie.split()])  # si convertim numerele la int

    # construim matricea de sume partiale si pentru a nu iesi din matrice calculam prima linie si prima coloana separat

    for j in range(1, m):
        a[0][j] += a[0][j - 1]

    for i in range(1, n):
        a[i][0] += a[i - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            a[i][j] = a[i][j] + a[i][j - 1] + a[i - 1][j] - a[i - 1][j - 1]
    s = []
    for i in range(len(perechi)):
        x1 = perechi[i][0]
        y1 = perechi[i][1]
        x2 = perechi[i][2]
        y2 = perechi[i][3]
        suma = a[x2][y2] - a[x2][y1 - 1] - a[x1 - 1][y2] + a[x1 - 1][y1 - 1]
        s.append(suma)
    return s


assert (pb9(5, 5, [[0, 2, 5, 4, 1],
                   [4, 8, 2, 3, 7],
                   [6, 3, 4, 6, 2],
                   [7, 3, 1, 8, 3],
                   [1, 5, 7, 9, 4]], [[1, 1, 3, 3], [2, 2, 4, 4]]) == [38, 44])

# Varianta chatgpt

# def precalc_sum(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     pre_sum = [[0] * cols for _ in range(rows)]
#
#     pre_sum[0][0] = matrix[0][0]
#
#     # Calculează suma pe prima linie
#     for j in range(1, cols):
#         pre_sum[0][j] = pre_sum[0][j - 1] + matrix[0][j]
#
#     # Calculează suma pe prima coloană
#     for i in range(1, rows):
#         pre_sum[i][0] = pre_sum[i - 1][0] + matrix[i][0]
#
#     # Calculează suma în restul matricei
#     for i in range(1, rows):
#         for j in range(1, cols):
#             pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1] + matrix[i][j]
#
#     return pre_sum
#
# def submatrix_sum(matrix, pairs):# O(n * m)
#     pre_sum = precalc_sum(matrix)
#     result = []
#
#     for pair in pairs:
#         (p, q), (r, s) = pair
#         if p == 0 and q == 0:
#             result.append(pre_sum[r][s])
#         elif p == 0:
#             result.append(pre_sum[r][s] - pre_sum[r][q - 1])
#         elif q == 0:
#             result.append(pre_sum[r][s] - pre_sum[p - 1][s])
#         else:
#             result.append(pre_sum[r][s] - pre_sum[r][q - 1] - pre_sum[p - 1][s] + pre_sum[p - 1][q - 1])
#
#     return result
#
# matrix = [
#     [0, 2, 5, 4, 1],
#     [4, 8, 2, 3, 7],
#     [6, 3, 4, 6, 2],
#     [7, 3, 1, 8, 3],
#     [1, 5, 7, 9, 4]
# ]
#
# pairs = [((1, 1), (3, 3)), ((2, 2), (4, 4))]
#
# print(submatrix_sum(matrix, pairs))
