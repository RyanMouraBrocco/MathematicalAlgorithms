import numpy as np
import timeit


# jacobi method
def jacobi(systemMatrix, errorRate, maxIteration, showTime=False):
    startTime = timeit.default_timer()
    systemLength = len(systemMatrix)
    error = 0
    index = 0
    oldXValues = np.zeros(systemLength)
    xValues = np.zeros(systemLength)
    systemMatrix = convertToValidMatrix(systemMatrix)
    while index < maxIteration:
        if index > 900:
            a = 2

        for i in range(systemLength):
            t = 1 / systemMatrix[i][i]
            sumValue = 0
            for j in range(systemLength):
                if(j != i):
                    sumValue += -(systemMatrix[i][j]) * oldXValues[j]

            t *= (sumValue + systemMatrix[i][systemLength])
            xValues[i] = t

        error = calculateErrorRate(xValues, oldXValues)

        if(error < errorRate):
            if(showTime == True):
                print("time to execute: " +
                      str((timeit.default_timer() - startTime)) + " seconds")

            return xValues

        for i in range(systemLength):
            oldXValues[i] = xValues[i]

        index += 1

    raise Exception('limited')


# calculate error rate to jacobi end execution
def calculateErrorRate(xValues, oldXValues):
    length = len(xValues)
    biggestDiffValue = 0.0
    for i in range(length):
        diff = abs(xValues[i] - oldXValues[i])
        if(i == 0 or biggestDiffValue < diff):
            biggestDiffValue = diff

    return biggestDiffValue

#convert a matrix to valid matrix in jacobi algorithm
def convertToValidMatrix(systemMatrix):
    systemLength = len(systemMatrix)
    for i in range(systemLength):
        if(systemMatrix[i][i] == 0):
            change = False
            for j in range(i, systemLength):
                if(systemMatrix[j][j] != 0 and systemMatrix[j][i] != 0):
                    systemMatrix = switchEquations(systemMatrix, i, j)
                    change = True
                    break

            if(change == False):
                for j in range(i):
                    if(systemMatrix[j][j] != 0 and systemMatrix[j][i] != 0):
                        systemMatrix = switchEquations(systemMatrix, i, j)
                        break

    return systemMatrix

# switch 2 lines of matrix
def switchEquations(matrix, lineA, lineB):
    length = len(matrix[lineA])
    for i in range(length):
        oldValue = matrix[lineA][i]
        matrix[lineA][i] = matrix[lineB][i]
        matrix[lineB][i] = oldValue

    return matrix


print("exercise 1")
matrix = [
    [2.0, 1.0,  2.0],
    [1.0, -2.0, -2.0],
]

print("test ex 1:")
print(jacobi(matrix, 0.000001, 200, True))


print("exercise 2")
try:
    matrix2 = [
        [15, 5, -5, 30],
        [4, 10, 1, 23],
        [2, -2, 8, -10]
    ]

    print("test ex 2:")
    print(jacobi(matrix2, 0.1, 10, True))
except Exception as ex:
    print("error in solution")

print("exercise 3")
print("a)")
try:
    matrix3a = [
        [1.0, -1.0, 3.0, 2.0],
        [3.0, -3.0, 1.0, -1.0],
        [1.0, 1.0, 0.0, 3.0]
    ]
    print(jacobi(matrix3a, 0.001, 200, True))
except Exception as ex:
    print("error in solution")


print("b)")
try:
    matrix3b = [
        [2.0, -1.5, 3.0, 1.0],
        [-1.0, 0.0, 2.0, 3.0],
        [4.0, -4.5, 5.0, 1.0]
    ]
    print(jacobi(matrix3b, 0.001, 200, True))
except Exception as ex:
    print("error in solution")


print("c)")
try:
    matrix3c = [
        [2.0, 0.0, 0.0, 0.0, 3.0],
        [1.0, 1.5, 0.0, 0.0, 4.5],
        [0.0, -3.0, 0.5, 0.0, -6.6],
        [2.0, -2.0, 1.0, 1.0, 0.8]
    ]
    print(jacobi(matrix3c, 0.001, 200, True))
except Exception as ex:
    print("error in solution")


print("d)")
try:
    matrix3d = [
        [1.0, 1.0, 0.0, 1.0, 2.0],
        [2.0, 1.0, -1.0, 1.0, 1.0],
        [4.0, -1.0, -2.0, 2.0, 0.0],
        [3.0, -1.0, -1.0, 2.0, -3.0]
    ]
    print(jacobi(matrix3d, 0.001, 200, True))
except Exception as ex:
    print("error in solution")
