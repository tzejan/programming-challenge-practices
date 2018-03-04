from math import sqrt

n = 10000000
def listSieve(n):

    sieve = [True] * n

    i = 2
    nroot = int(sqrt(n)+1)
    lastNum = 2
    while i < nroot:
        if sieve[i]:
            lastNum = i*2
            while lastNum < n:
                sieve[lastNum] = False
                lastNum += i
        i += 1
    return sieve

def setSieve(n):
    sieve = set([i for i in range(n)])

    i = 2
    nroot = int(sqrt(n)+1)
    lastNum = 2
    while i < nroot:
        if i in sieve:
            lastNum = i*2
            while lastNum < n:
                if lastNum in sieve:
                    sieve.remove(lastNum)
                lastNum += i
        i += 1
    return sieve

#primeSet = setSieve(n)
#primeList = listSieve(n)
#print 101 in primeSet
print sqrt(1000000000000)
#print primeList[101]