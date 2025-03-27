def pb10(n, m, a):  # complexitate timp si spatiu, O(n*m)
    # n = int(input("n="))
    # m = int(input("m="))
    # a = []
    # for i in range(n):
    #     linie = input()
    #     a.append([int(x) for x in linie.split()])

    max = 0
    imax = 0
    for i in range(n):
        zerouri = 0
        for j in range(m):
            if a[i][j] == 0:  # numaram valorile de 0
                zerouri += 1
            else:
                break
        if max < m - zerouri:  # calculam prin scadere cate valori de 1 sunt pe linie
            max = m - zerouri
            imax = i
    return imax


assert (pb10(3, 5, [[0, 0, 0, 1, 1],
                    [0, 1, 1, 1, 1],
                    [0, 0, 1, 1, 1]]) == 1)

# Varianta chatgpt


# def linia_cu_cele_mai_multe_unu(matrice):# O(n* m)
#     # Initializam variabilele pentru retinerea indexului liniei cu cele mai multe unu
#     max_linie = 0
#     max_unu = 0
#
#     # Parcurgem matricea
#     for i in range(len(matrice)):
#         # Numaram cate unu sunt pe linie
#         numar_unu = sum(matrice[i])
#
#         # Daca numarul de unu este mai mare decat cel maxim gasit pana acum,
#         # actualizam variabilele
#         if numar_unu > max_unu:
#             max_linie = i
#             max_unu = numar_unu
#
#     return max_linie
#
#
# # Exemplu de utilizare
# matrice = [
#     [0, 0, 0, 1, 1],
#     [0, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1]
# ]
#
# print("Indexul liniei cu cele mai multe elemente de 1 este:", linia_cu_cele_mai_multe_unu(matrice))
