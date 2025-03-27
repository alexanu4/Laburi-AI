def pb1(cuvinte):  # complexitate timp si spatiu - teta(n)
    # text = input("Introduceti un text\n")
    # text = text.lower()  # transformam textul in litere mici
    # cuvinte = text.split()  # despartim textul in cuvinte dupa caracterul spatiu
    ultim = cuvinte[0]  # initializam ultim
    for cuvant in cuvinte:
        if cuvant > ultim:  # daca gasim un cuvant mai mare lexicografic actualizam valoarea lui ultim
            ultim = cuvant
    return ultim


cuvinte = ["Ana", "are", "mere", "rosii", "si", "galbene"]
assert (pb1(cuvinte) == "si")


# Varianta chatgpt

# def ultimul_cuvant(text):  # timp O(n log n) spatiu O(n)
#     cuvinte = text.split()  # Se separă cuvintele din text
#     cuvinte.sort()  # Se sortează alfabetic
#     return cuvinte[-1]  # Se returnează ultimul cuvânt
#
#
# # Exemplu de utilizare
# text = "Ana are mere rosii si galbene"
# ultimul = ultimul_cuvant(text)
# print("Ultimul cuvant este:", ultimul)


