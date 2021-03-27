import math as m

#bisection function, calculate any math system
def bisection(function, beginValue, endValue, errorRate, maxIteration):
    index = 0
    beginFunctionValue = function(beginValue)
    while index < maxIteration:
        middleValue = beginValue + (endValue - beginValue) / 2
        middleFunctionValue = function(middleValue)

        if(middleFunctionValue == 0 or abs(middleFunctionValue) < errorRate):
            return middleValue

        if(beginFunctionValue * middleFunctionValue > 0):
            beginFunctionValue = middleFunctionValue
            beginValue = middleValue
        else:
            endValue = middleValue

        index += 1

    raise Exception('not found with this iteration number')


print("exercice 2")


def e2(x):
    return x**3 + 4*x**2 - 10


print(bisection(e2, 1, 2, 0.1, 500))


print("exercice 3")
print("a)")


def e3A(x):
    return x - 2 ** (-x)


print(bisection(e3A, 0, 1, 0.001, 500))


print("b)")


def e3B(x):
    return m.exp(x) - x**2 + 3*x - 2


print(bisection(e3B, 0, 1, 0.001, 500))

print("c)")


def e3C(x):
    return 2*x*m.cos(2*x) - (x+1)**2


print(bisection(e3C, -3, -2, 0.001, 500))
print(bisection(e3C, -1, 0, 0.001, 500))

print("d)")


def e3D(x):
    return x * m.cos(x) - 2*(x**2) + 3*x - 1


print(bisection(e3D, 0.2, 0.3, 0.001, 500))
print(bisection(e3D, 1.2, 1.3, 0.001, 500))

print("exercice 4")

try:
    print(bisection(e3A, 0, 1, 0.001, 3))
except Exception as ex:
    print("error in solution, not found values in this max iteration number")

try:
    print(bisection(e3A, 0, 1, 0.001, 5))
except Exception as ex:
    print("error in solution, not found values in this max iteration number")

try:
    print(bisection(e3A, 0, 1, 0.001, 6))
except Exception as ex:
    print("error in solution, not found values in this max iteration number")

try:
    print(bisection(e3A, 0, 1, 0.001, 10))
except Exception as ex:
    print("error in solution, not found values in this max iteration number")