def pb6(n,numere):  # complexitate timp si spatiu teta(n)
    # n = int(input("Introduceti n:"))
    # linie = input("Introduceti numerele:\n")
    # numere = linie.split()
    elem_majoritar = []
    for i in range(n):
        if len(elem_majoritar) == 0 or numere[i] == elem_majoritar[-1]:
            elem_majoritar.append(numere[i])
        else:
            elem_majoritar.pop()
    return elem_majoritar[0]


assert(pb6(11,[2,8,7,2,2,5,2,3,1,2,2])==2)



# Varianta chatgpt
def gaseste_majoritar(nums):  # O(n)
    majoritar_candidat = None
    count = 0

    for num in nums:
        if count == 0:
            majoritar_candidat = num
            count = 1
        elif majoritar_candidat == num:
            count += 1
        else:
            count -= 1

    # Verificăm dacă candidatul este majoritar
    count = 0
    for num in nums:
        if num == majoritar_candidat:
            count += 1
    if count > len(nums) // 2:
        return majoritar_candidat
    else:
        return None


# Exemplu de utilizare
nums = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
rezultat = gaseste_majoritar(nums)
if rezultat:
    print("Elementul majoritar este:", rezultat)
else:
    print("Nu există element majoritar în șirul dat.")

