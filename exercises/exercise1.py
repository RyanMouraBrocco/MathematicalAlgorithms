def sqrt(number, precisionRate, returnErroRate=False, logInformation=False):
    if(number >= 0 and precisionRate > 0):
        smallerLimit = calculate(0)
        biggerLimit = calculate(number)
        middlePoint = calculateMiddlePoint(smallerLimit, biggerLimit)
        errorRate = calculate(middlePoint)
        condition = isNegativeNumber(errorRate)
        for i in range(precisionRate):
            if(condition):
                smallerLimit = middlePoint
            else:
                biggerLimit = middlePoint

            middlePoint = calculateMiddlePoint(smallerLimit, biggerLimit)
            errorRate = calculate(middlePoint)
            lastCondition = condition
            condition = isNegativeNumber(errorRate)

            if(logInformation):
                print("SmallerLimit: " + str(smallerLimit) + " BiggerLimit: " + str(biggerLimit) + " MiddlePoint: " + str(middlePoint) + " ErrorRate: " +
                      str(errorRate) + " Condition: " + str(condition) + " Desision: " + ("SmallerLimit = MiddlePoint" if condition else "BiggerLimit = MiddlePoint"))

        if(returnErroRate):
            if(errorRate < 0):
                return errorRate * - 1
            else:
                return errorRate

        if(lastCondition):
            return smallerLimit
        else:
            return biggerLimit
    else:
        return 0


def calculate(number):
    return (number * number) - 2


def calculateMiddlePoint(numberA, numberB):
    return (numberA + numberB) / 2


def isNegativeNumber(number):
    if(number < 0):
        return True
    else:
        return False


# 1)
print("Exercise 1)")
print(sqrt(2, 15))

# 2)
print("\n\nExercise 2)")
print(sqrt(2, 7, logInformation=True))

# 3) and 4)
print("\n\nExercise 3) and 4)")
for i in range(1, 500):
    erroRate = sqrt(2, i, True)
    if(erroRate < 0.00000001):
        print("Error rate is smaller than 10^-8 in precision rate: " +
              str(i) + " if error rate: " + str(erroRate))
        break
