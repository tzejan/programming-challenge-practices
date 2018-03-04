#project Euler #2
n = 4 * pow(10, 16)
n = 100

from math import sqrt, pow

root5 = sqrt(5)
phi = (1 + root5)/2

def fib(n):
    return int((pow(phi, n)/root5) + 0.5)

i = 0
fn = 1
sumeven = 0
while fn < n:    
    if fn % 2 == 0:
        sumeven += fn
        print fn, n
    fn = fib(i)
    i += 1

print sumeven