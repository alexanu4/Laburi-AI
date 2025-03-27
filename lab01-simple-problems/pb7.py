def pb7(n,k,numere):  # complexitate timp O(n*log n ), spatiu teta(n)
    # n = int(input("n="))
    # k = int(input("k="))
    # linie = input("Introduceti numerele:\n")
    # numere = linie.split()
    numere.sort()
    return numere[-k]


assert(pb7(6,2,[7,4,6,3,9,1])==7)


# Varianta chatgpt

def kth_largest_element(nums, k):  # complexitate timp O(n log n) spatiu O(n)
    # Sortăm șirul în ordine descrescătoare
    nums.sort(reverse=True)

    # Returnăm al k-lea cel mai mare element
    return nums[k - 1]


# Testăm funcția
nums = [7, 4, 6, 3, 9, 1]
k = 2
print("Al", k, "-lea cel mai mare element este:", kth_largest_element(nums, k))




