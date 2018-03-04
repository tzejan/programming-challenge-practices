lastN = 40000000000000001
#lastN = 10

evenfib = []

fib = [0,1]
i = 1
while fib[-1] < lastN:
    fn = fib[i]+fib[i-1]
    fib.append(fn)
    i += 1
    if fn % 2 == 0:
        evenfib.append(fn)
n=10
sumEvenFib = 0
for ef in evenfib:
    if ef < n:
        sumEvenFib += ef
    else:
        break
print fib
print evenfib
print sumEvenFib