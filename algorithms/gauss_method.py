import numpy as np


def triangule(systemMatrix):
    systemLength = len(systemMatrix)
    xValues = np.zeros(systemLength)
    for i in range(systemLength - 1, -1, - 1):
        value = systemMatrix[i, systemLength]

        sumValue = 0
        for j in range(i+1, systemLength):
            sumValue += systemMatrix[i, j] * xValues[j]

        if(sumValue != 0):
            value -= sumValue

        value /= systemMatrix[i, i]
        xValues[i] = value
    return xValues


def pivot(systemMatrix):
    systemLength = len(systemMatrix)
    for i in range(systemLength):
        smaller = 0
        for p in range(systemLength):
            if(systemMatrix[p][i] != 0):
                smaller = p
                break

        if(smaller == 0):
            return "Error"

        if(smaller != i):
            # fazer algo aqui

        for j in range(i + 1, systemLength + 1):
            const = systemMatrix[j][i] / systemMatrix[i][i]
            


matrix = [
    [3.0,  2.0,  4.0,   1.0],
    [0.0,  1/3,  2/3,   5/3],
    [0.0,  0.0,  -8.0,  0.0]
]

print(triangule(np.matrix(matrix)))

matrix2 = [
    [1,   1,   0,   3,    4],
    [0,  -1,  -1,  -5,   -7],
    [0,   0,   3,   13,  13],
    [0,   0,   0,  -13, -13]
]
print(triangule(np.matrix(matrix2)))
