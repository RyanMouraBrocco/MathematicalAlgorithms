import math as m

# newton method


def newton(function, derivativeFunction, beginPoint, errorRate, maxIteration=200, absoluteErrorRate=True):
    index = 0
    oldPoint = beginPoint
    while index < maxIteration:
        functionValue = function(oldPoint)
        derivativeFunctionValue = derivativeFunction(oldPoint)
        newPoint = oldPoint - (functionValue / derivativeFunctionValue)

        if absoluteErrorRate:
            if(abs(newPoint - oldPoint) < errorRate):
                return newPoint
        else:
            if(abs(newPoint - oldPoint) / abs(newPoint) < errorRate):
                return newPoint

        index += 1
        oldPoint = newPoint

    raise Exception('not found with this iteration number')


print("Ex.1")


def functionEx1A(x):
    return x**3 + 4*(x**2) - 10


def derivativeFunctionEx1A(x):
    return 3 * (x**2) + 8*x


print(" A) " + str(newton(functionEx1A, derivativeFunctionEx1A, 1, 0.1)))


def functionEx1B(x):
    return m.cos(x) - x


def derivativeFunctionEx1B(x):
    return -m.sin(x) - 1


print(" B) " + str(newton(functionEx1B, derivativeFunctionEx1B, 0.5, 0.001)))

print("Ex.2")


def functionEx2A(x):
    return x**3 + 4*(x**2) - 10


def derivativeFunctionEx2A(x):
    return 3 * (x**2) + 8*x


print(" A) " + str(newton(functionEx2A, derivativeFunctionEx2A, 1, 0.0001)))


def functionEx2B(x):
    return m.cos(x) - x


def derivativeFunctionEx2B(x):
    return -m.sin(x) - 1


print(" B) " + str(newton(functionEx2B, derivativeFunctionEx2B, 0, 0.0001)))


def functionEx2C(x):
    return x**3 - 2*(x**2) - 5


def derivativeFunctionEx2C(x):
    return 3 * (x**2) - 4*x


print(" C) " + str(newton(functionEx2C, derivativeFunctionEx2C, 1, 0.0001)))


def functionEx2D(x):
    return m.exp(x) - 3 * (x**2)


def derivativeFunctionEx2D(x):
    return m.exp(x) - 6 * x


print(" D.1) " + str(newton(functionEx2D, derivativeFunctionEx2D, 1, 0.0001)))
print(" D.2) " + str(newton(functionEx2D, derivativeFunctionEx2D, 3, 0.0001)))


print("Ex.3")

print(" A) " + str(newton(functionEx2A, derivativeFunctionEx2A,
                          1, 0.0001, absoluteErrorRate=False)))

print(" D.1) " + str(newton(functionEx2D, derivativeFunctionEx2D,
                            1, 0.0001, absoluteErrorRate=False)))
print(" D.2) " + str(newton(functionEx2D, derivativeFunctionEx2D,
                            3, 0.0001, absoluteErrorRate=False)))
