import numpy as np


def newton(xValues, yValues):
    length = len(xValues)
    finalValues = np.zeros((length, length))
    for i in range(length):
        finalValues[i][0] = yValues[i]

    for i in range(1, length):
        for j in range(1, i + 1):
            xDiff = xValues[i] - xValues[i-j]
            if(xDiff == 0):
                finalValues[i][j] = 0
            else:
                finalValues[i][j] = (finalValues[i][j-1] - finalValues[i-1][j-1]) / xDiff

    return finalValues


print("Ex. 1")

xValues1 = [-2, -1, 0, 1, 2, 3]
yValues1 = [1, 4, 11, 16, 13, -4]

print(newton(xValues1, yValues1))

print("Ex. 2")

xValues2 = [-2, -1, 0, 1, 2]
yValues2 = [-1, 3, 1, -1, 3]

print(newton(xValues2, yValues2))
