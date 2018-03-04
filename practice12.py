
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


fibDict = dict()

def fibm(n):
    if n <= 2:
        return 1
    if n in fibDict:
        return fibDict[n]

    result = fib(n-1) + fib(n-2)
    fibDict[n] = result
    return result

def fibi(n):
    result = 1
    prevResult = 0
    for i in range(1, n):
        sumf = result + prevResult
        prevResult = result
        result = sumf

    return result


print fib(10)
print fibm(10)
print fibi(10)