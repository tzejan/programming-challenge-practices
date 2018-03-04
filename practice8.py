#happy numbers

def happyNumber(n):
    prevNum = set()
    totalSum = 0

    while n != 1 and n not in prevNum:
        prevNum.add(n)
        while n != 0:
            ones = n % 10
            totalSum += ones * ones
            n /= 10
        n = totalSum        
        totalSum = 0
        print n, prevNum

    if n == 1:
        return True #happy numbers

    return False

#for n in range(10):
#    print n, happyNumber(n)
print happyNumber(7)