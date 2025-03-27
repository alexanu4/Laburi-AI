def reprezentare_binara(n):  # determina reprezentarea binara a unui numar
    # complexitate timp teta(log n), spatiu teta(1)
    if n != 0:
        return n % 2 + 10 * reprezentare_binara(n // 2)
    return n % 2

def pb8(n):  # complexitate timp teta(n*log n), spatiu O(1)
    # n = int(input("n="))
    numbers = []
    for i in range(1, n + 1):
        numbers.append(reprezentare_binara(i))
    return numbers



assert(pb8(4)==[1,10,11,100])


# Varianta chatgpt

# def generate_binary_numbers(n):  # timp spatiu  O(n * log n)
#     binary_numbers = []
#     for i in range(1, n + 1):
#         binary_numbers.append(bin(i)[2:])
#     return binary_numbers
#
#
# n = int(input("Introduceti valoarea lui n: "))
# binary_numbers = generate_binary_numbers(n)
# print("Numerele binare până la", n, "sunt:", binary_numbers)

