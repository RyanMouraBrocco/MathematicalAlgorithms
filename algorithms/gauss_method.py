import numpy as np

def triangule(systemMatrix):
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
          systemMatrix =  switchEquations(systemMatrix, smaller, i)

        for j in range(i + 1, systemLength):
            multiplyFactor = systemMatrix[j][i] / systemMatrix[i][i]
            systemMatrix = subEquations(systemMatrix, j, i, multiplyFactor)
    
    if(systemMatrix[systemLength - 1][systemLength - 1] == 0):
        raise Exception('no unique solution exists')
    
    return systemMatrix
            

def subEquations(matrix, lineResult, line, multiplyFactor):
    length = len(matrix[lineResult])
    for i in range(length):
        matrix[lineResult][i] -= multiplyFactor * matrix[line][i]
    
    return matrix

def switchEquations(matrix, lineA, lineB):
    length = len(matrix[lineA])
    for i in range(length):
        oldValue = matrix[lineA][i]
        matrix[lineA][i] = matrix[lineB][i]
        matrix[lineB][i] = oldValue
    
    return matrix

def gauss(systemMatrix):
    return triangule(pivot(systemMatrix))



matrix = [
    [3.0,  2.0,  4.0,   1.0],
    [0.0,  1.0/3.0,  2.0/3.0,   5.0/3.0],
    [0.0,  0.0,  -8.0,  0.0]
]

print(triangule(matrix))

matrix2 = [
    [1.0,   1.0,   0.0,   3.0,    4.0],
    [0.0,  -1.0,  -1.0,  -5.0,   -7.0],
    [0.0,   0.0,   3.0,   13.0,  13.0],
    [0.0,   0.0,   0.0,  -13.0, -13.0]
]
print(triangule(matrix2))


matrix3 = [
    [9.0, 6.0,  -3.0,  3.0, 12.0],
    [6.0, 20.0, 2.0, 22.0, 64.0],
    [-3.0, 2.0, 6.0, 2.0, 4.0],
    [3.0, 22.0, 2.0, 28.0, 82.0]
]

print(pivot(matrix3))
print(gauss(matrix3))

try:
    matrix4a = [
        [1.0, -1.0, 3.0, 2.0],
        [3.0, -3.0, 1.0, -1.0],
        [1.0, 1.0, 0.0, 3.0]
    ]
    print(gauss(matrix4a))
except Exception as ex:
    print("error: " + ex.message)

try:
    matrix4b = [
        [2.0, -1.5, 3.0, 1.0],
        [-1.0, 0.0, 2.0, 3.0],
        [4.0, -4.5, 5.0, 1.0]
    ]
    print(gauss(matrix4b))
except Exception as ex:
    print("error: " + ex.message)

try:
    matrix4c = [
        [2.0, 0.0, 0.0, 0.0, 3.0],
        [1.0, 1.5, 0.0, 0.0, 4.5],
        [0.0, -3.0, 0.5, 0.0, -6.6],
        [2.0, -2.0, 1.0, 1.0, 0.8]
    ]
    print(gauss(matrix4c))
except Exception as ex:
    print("error: " + ex.message)

try:
    matrix4d = [
        [1.0, 1.0, 0.0, 1.0, 2.0],
        [2.0, 1.0, -1.0, 1.0, 1.0],
        [4.0, -1.0, -2.0, 2.0, 0.0],
        [3.0, -1.0, -1.0, 2.0, -3.0]
    ]
    print(gauss(matrix4d))
except Exception as ex:
    print("error: " + ex.message)