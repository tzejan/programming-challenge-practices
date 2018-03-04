# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

largestPrime = 2
primeNum = [largestPrime]

def isPrime(n):
    prime = True
    root = sqrt(n) + 1

    for i in primeNum:
        if i > root:
            break
        if n % i == 0:
            prime = False
            break
        
    return prime

#t = int(raw_input())
t = 1
for _ in range(t):
    #n = int(raw_input())
    n = 10000000
    
    #populate prime numbers
    primeCandidate = largestPrime + 1  
    while n > largestPrime:             
        
        if isPrime(primeCandidate):
            largestPrime = primeCandidate
            primeNum.append(largestPrime)
        primeCandidate += 1

    print "done populating"
    lp = n
    for i in range(2, n/2):
        if n%i == 0:
            d = n/i
            if isPrime(d):
                lp = d
                break
    print lp
    #print primeNum
    