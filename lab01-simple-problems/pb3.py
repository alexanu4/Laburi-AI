def pb3(vec1, vec2):  # complexitate timp si spatiu teta(m*n) (n-numarul de elemente de pe o linie)
    # m1 = int(input("Introduceti dimensiunile primului vector m1="))
    # m2 = int(input("Introduceti dimensiunile celui de al doilea vector m2="))
    # if m1 != m2:
    #     print("Nu se poate realiza produsul scalar")
    # else:
    #     print("Introduceti elementele primului vector")
    #     vector = []  # citim primul vector linie cu linie
    #     for i in range(m1):
    #         linie = input()
    #         linie = linie.split()  # despartim elementele dupa spatiu
    #         vector.append(linie)
    #     prod_scalar = 0
    #     print("Introduceti elementele celui de al doilea vector")
    #     for i in range(m2):  # citim al doilea vector fara a il mai retine si tot calculam produsul scalar
    #         linie = input()
    #         linie = linie.split()
    #         for j in range(len(linie)):
    #             prod_scalar += int(vector[i][j]) * int(linie[j])
    # prod_scalar = 0
    # for i in range(len(vec1)):
    #         prod_scalar += vec1[i] * vec2[i]
    # return prod_scalar
    prod_scalar = 0
    if (isinstance(vec1, list)):
        for i in range(len(vec1)):
            prod_scalar += pb3(vec1[i], vec2[i])
    else:
        prod_scalar += vec1 * vec2
    return prod_scalar


assert (pb3([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4)
assert (pb3([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]], [[0, 2, 5, 4, 1],
                                                                  [4, 8, 2, 3, 7],
                                                                  [6, 3, 4, 6, 2]]) == 37)


# Varianta chatgpt
def sparse_dot_product(vec1, vec2):  # timp O(n) spatiu O(1)
    # Verificăm dacă dimensiunile vectorilor sunt aceleași
    if len(vec1) != len(vec2):
        return "Dimensiunile vectorilor nu coincid."

    # Inițializăm produsul scalar
    dot_product = 0

    # Iterăm prin elementele vectorului și le înmulțim
    for i in range(len(vec1)):
        # Dacă unul dintre elementele corespunzătoare este zero, trecem peste el
        if vec1[i] == 0 or vec2[i] == 0:
            continue
        else:
            # Înmulțim elementele și adăugăm la produsul scalar
            dot_product += vec1[i] * vec2[i]

    return dot_product


# Test
vector1 = [1, 0, 2, 0, 3]
vector2 = [1, 2, 0, 3, 1]
result = sparse_dot_product(vector1, vector2)
print("Produsul scalar al celor doi vectori este:", result)
