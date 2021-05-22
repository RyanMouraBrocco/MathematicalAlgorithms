def leastSquare(xValues, yValues):
    length = len(xValues)
    sumXValues = 0
    sumYValues = 0
    sumX2Values = 0
    sumXYValues = 0
    for i in range(length):
        sumXValues += xValues[i]
        sumYValues += yValues[i]
        sumX2Values += xValues[i] ** 2
        sumXYValues += xValues[i] * yValues[i]

    x = ((length * sumXYValues) - (sumXValues * sumYValues))/((length * sumX2Values) - (sumXValues ** 2))
    y = ((sumX2Values * sumYValues) - (sumXYValues * sumXValues))/((length * sumX2Values) - (sumXValues ** 2))

    if(y < 0):
        return str(x) + "x "+ str(y)
    else:
        return str(x) + "x +" + str(y)

xValues1 = [1.0, 1.1, 1.3, 1.5, 1.9, 2.1]
yValues1 = [1.84, 1.96, 2.21, 2.45, 2.94, 3.18]

print(leastSquare(xValues1, yValues1))

xValues2 = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
yValues2 = [102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.5, 326.72]

print(leastSquare(xValues2, yValues2))
    