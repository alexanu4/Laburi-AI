def pb5(n,elemente):  # complexitate timp teta(n), spatiu teta(n)
    # n = int(input("Introduceti n:"))
    gauss = (n * (n - 1)) // 2  # calculam suma numerelor de la 1 la n-1
    # print("Introduceti sirul")
    # linie = input()
    # elemente = linie.split()
    for k in elemente:
        gauss -= int(k)  # scadem toate elementele din sir
    return -gauss  # la sfarsit ne ramane elementul care se repeta


assert (pb5(5,[1,2,3,4,2])==2)

# Varianta chatgpt

def gaseste_element_duplicat(arr):  # timp si spatiu O(n)
    frecventa = {}

    for element in arr:
        if element in frecventa:
            return element
        else:
            frecventa[element] = 1

    return None


# Exemplu de utilizare:
arr = [1, 2, 3, 4, 2]
print("Elementul duplicat este:", gaseste_element_duplicat(arr))

