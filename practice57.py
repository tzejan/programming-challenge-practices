#Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
def isPower(A):
    def pow(n, p):
        result = n
        for i in xrange(p-1):
            result *= n
        return result
    if A == 1:
        return True

    p = 2
    n = 2
    power = pow(n, p)
    while power < A and p == 2:
        while power < A:
            p += 1
            power = pow(n, p)
        if power == A:
            return True
        n += 1
        p = 2
        power = pow(n, p)


    if power == A:
        return True
    return False


for i in xrange(30):
    print i, isPower(i)
"""
2 2
2 3
2 4

3 2
3 3

4 2

5 2
"""
