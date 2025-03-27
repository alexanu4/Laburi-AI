def pb4(cuvinte):  # complexitate timp O(n^2) (n numarul de cuvinte), spatiu Teta(n)
    # propozitie = input("Introduceti o propozitie:\n")
    # cuvinte = propozitie.split()  # impartim propozitia in cuvinte
    dictionar = {}
    for cuvant in cuvinte:
        if cuvant in dictionar.keys():
            dictionar[cuvant] += 1
        else:
            dictionar[cuvant] = 1
    unic = []
    for cuvant in dictionar.keys():
        if dictionar[cuvant] == 1:
            unic.append(cuvant)
    return unic

assert (pb4(["ana", "are", "ana", "are", "mere", "rosii", "ana"]) == ["mere", "rosii"])


# Varianta chatgpt

# def cuvinte_unice(text):  # timp spatiu O(n)
#     aparitii = {}
#     cuvinte = text.split()
#
#     # Numărăm aparițiile fiecărui cuvânt
#     for cuvant in cuvinte:
#         if cuvant in aparitii:
#             aparitii[cuvant] += 1
#         else:
#             aparitii[cuvant] = 1
#
#     # Selectăm cuvintele care apar o singură dată
#     cuvinte_unice = [cuvant for cuvant, aparitie in aparitii.items() if aparitie == 1]
#
#     return cuvinte_unice
#
#
# # Testăm funcția
# text = "ana are ana are mere rosii ana"
# rezultat = cuvinte_unice(text)
# print("Cuvintele unice din text sunt:", rezultat)

