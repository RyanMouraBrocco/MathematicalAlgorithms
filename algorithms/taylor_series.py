# Function neperianX (e^x) with implementation of taylor series solution
def neperianX(number, iterateNumber):
    powNumber = 1 / number
    factorial = 1
    sumNumber = 0
    for i in range(iterateNumber + 1):
        powNumber = powNumber * number
        if(i > 0):
            factorial = factorial * i
        
        sumNumber =  sumNumber + (powNumber / factorial)

    return sumNumber

print("neperian number with iterate number = 5, e^3: " + str(neperianX(3, 5)))
print("neperian number with iterate number = 10, e^3: " + str(neperianX(3, 10)))