from random import randint

def create_matrix(matrix):
    i = int(input("Kol-vo stolbov: "))
    j = int(input("Kol-vo strok: "))
    for y in range(i):
        matrix.append([])
        for x in range(j):
            num = int(input("Number"))
            matrix[y].append(num)
    return matrix

def create_random_matrix(matrix):
    i = int(input("Kol-vo stolbov: "))
    j = int(input("Kol-vo strok: "))
    for y in range(j):
        matrix.append([])
        for x in range(i):
            matrix[y].append(randint(-100, 100))
    return matrix
def matrix_print(matrix):
    for y in range(len(matrix)):
        print()
        for x in range(len(matrix[y])):
            print(matrix[y][x], end=" ")

def minusSignOut(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] = -1 * matrix[y][x]

def multipOnNumber(matrix, number):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] = number * matrix[y][x]

def transp(matrix):
    matrix2 = matrix
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            pass
