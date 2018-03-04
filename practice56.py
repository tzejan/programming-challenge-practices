#primesum
#Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

#NOTE A solution will always exist. read Goldbach's conjecture

def primesum(A):
    primes = [True] * A
    primes[1] = True
    primes[2] = True
    for i in xrange(2, A):
        if not primes[i]:
            continue
        num = i + i
        while num < A:
            primes[num] = False
            num += i

    for i in xrange(2, A):
        if primes[i] and primes[A-i]:
            return i, A-i

    return 1, A

print primesum(16777214)