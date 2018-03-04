from math import sqrt


def makeSieve(n):
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

def isPrime(sieve, n):
    prime = True
    nroot = int(sqrt(n) + 1)

    for i in range(2, nroot):
        if n % i == 0:
            prime = False
            break
        
    return prime

#t = int(raw_input())
t=1
#narr = [int(raw_input()) for _ in range(t)]
narr=[13195]
maxn = max(narr)
sieve = makeSieve(int(sqrt(maxn)+1))

for n in narr:
    lp = 0
    nroot = int(sqrt(n)+1)
    for i in range(2, nroot):
        if n%i == 0:
            d = n/i
            if isPrime(sieve, d):
                lp = d
                break
            else:
                if lp < i and sieve[i]:
                    lp = i
    if lp == 0:
        lp = n
    print lp