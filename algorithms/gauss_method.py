import numpy as np

# Function to resolve a triangular system of variables and save the result in xValues array
def triangulate(systemMatrix):
    systemLength = len(systemMatrix)
    xValues = np.zeros(systemLength)
    for i in range(systemLength - 1, -1, - 1):
        value = systemMatrix[i][systemLength]

        sumValue = 0
        for j in range(i+1, systemLength):
            sumValue += systemMatrix[i][j] * xValues[j]

        if(sumValue != 0):
            value -= sumValue

        value /= systemMatrix[i][i]
        xValues[i] = value
    return xValues

# Function to pivot a system of variables
def pivot(systemMatrix):
    systemLength = len(systemMatrix)
    for i in range(systemLength):
        smaller = 0
        isFound = False
        for p in range(i, systemLength):
            if(systemMatrix[p][i] != 0):
                isFound = True
                smaller = p
                break

        if(isFound == False):
            raise Exception('no unique solution exists')

        if(smaller != i):
            systemMatrix = switchEquations(systemMatrix, smaller, i)

        for j in range(i + 1, systemLength):
            multiplyFactor = systemMatrix[j][i] / systemMatrix[i][i]
            systemMatrix = subEquations(systemMatrix, j, i, multiplyFactor)

    if(systemMatrix[systemLength - 1][systemLength - 1] == 0):
        raise Exception('no unique solution exists')

    return systemMatrix


# Function to sub a line for other (Ej - M * Ei) -> (Ej)
def subEquations(matrix, lineResult, line, multiplyFactor):
    length = len(matrix[lineResult])
    for i in range(length):
        matrix[lineResult][i] -= multiplyFactor * matrix[line][i]

    return matrix

# Function to switch 2 lines Ej <-> Ei
def switchEquations(matrix, lineA, lineB):
    length = len(matrix[lineA])
    for i in range(length):
        oldValue = matrix[lineA][i]
        matrix[lineA][i] = matrix[lineB][i]
        matrix[lineB][i] = oldValue

    return matrix

#Function to calculate a system of variables with gauss method
def gauss(systemMatrix):
    return triangulate(pivot(systemMatrix))


print("exercise 1:")
print("test 1")
matrix = [
    [3.0,  2.0,  4.0,   1.0],
    [0.0,  1.0/3.0,  2.0/3.0,   5.0/3.0],
    [0.0,  0.0,  -8.0,  0.0]
]

print(triangulate(matrix))

print("test 2")
matrix2 = [
    [1.0,   1.0,   0.0,   3.0,    4.0],
    [0.0,  -1.0,  -1.0,  -5.0,   -7.0],
    [0.0,   0.0,   3.0,   13.0,  13.0],
    [0.0,   0.0,   0.0,  -13.0, -13.0]
]
print(triangulate(matrix2))

print("exercise 2 and 3")
matrix3 = [
    [9.0, 6.0,  -3.0,  3.0, 12.0],
    [6.0, 20.0, 2.0, 22.0, 64.0],
    [-3.0, 2.0, 6.0, 2.0, 4.0],
    [3.0, 22.0, 2.0, 28.0, 82.0]
]

print("test ex 2:")
print(np.matrix(pivot(matrix3)))
print("test ex 3:")
print(gauss(matrix3))


print("exercise 4:")
print("a)")
try:
    matrix4a = [
        [1.0, -1.0, 3.0, 2.0],
        [3.0, -3.0, 1.0, -1.0],
        [1.0, 1.0, 0.0, 3.0]
    ]
    print(gauss(matrix4a))
except Exception as ex:
    print("error in solution")


print("b)")
try:
    matrix4b = [
        [2.0, -1.5, 3.0, 1.0],
        [-1.0, 0.0, 2.0, 3.0],
        [4.0, -4.5, 5.0, 1.0]
    ]
    print(gauss(matrix4b))
except Exception as ex:
    print("error in solution")


print("c)")
try:
    matrix4c = [
        [2.0, 0.0, 0.0, 0.0, 3.0],
        [1.0, 1.5, 0.0, 0.0, 4.5],
        [0.0, -3.0, 0.5, 0.0, -6.6],
        [2.0, -2.0, 1.0, 1.0, 0.8]
    ]
    print(gauss(matrix4c))
except Exception as ex:
    print("error in solution")


print("d)")
try:
    matrix4d = [
        [1.0, 1.0, 0.0, 1.0, 2.0],
        [2.0, 1.0, -1.0, 1.0, 1.0],
        [4.0, -1.0, -2.0, 2.0, 0.0],
        [3.0, -1.0, -1.0, 2.0, -3.0]
    ]
    print(gauss(matrix4d))
except Exception as ex:
    print("error in solution")
