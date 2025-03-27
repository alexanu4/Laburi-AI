import math

def pb2(x1, y1, x2, y2):  # complexitatea timp si spatiu este teta(1)
    # x1 = int(input("x1:\n"))
    # y1 = int(input("y1:\n"))
    # x2 = int(input("x2:\n"))
    # y2 = int(input("y2:\n"))
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # aplicam formula pentru distanta euclideana
    return d



assert (pb2(1, 5, 4, 1) == 5)

# Varianta chatgpt
def euclidean_distance(point1, point2):#timp spatiu O(1)
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Test
point1 = (1, 5)
point2 = (4, 1)
distance = euclidean_distance(point1, point2)
print("Distanța Euclidiană între", point1, "și", point2, "este:", distance)