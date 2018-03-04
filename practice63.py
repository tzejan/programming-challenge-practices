#search range

def searchRange(A, B):
    l = 0
    r = len(A) - 1
    
    start = 0
    end = 0
    while (l <= r):
        m = (l + r) / 2
        if A[m] == B:
            if m == 0 or (m > 0 and A[m-1] != B):
                start = m
                break
        if A[m] < B:
            l = m + 1
            continue
        if A[m] >= B:
            r = m - 1
    if l > r:
        return [-1, -1]


    l = start
    r = len(A) - 1
    while (l <= r):
        m = (l + r) / 2
        if A[m] == B:
            if m == len(A)-1 or (m < len(A)-1 and A[m+1] != B):
                end = m
                break
        if A[m] <= B:
            l = m + 1
            continue
        if A[m] > B:
            r = m - 1
    

    return [start, end]

print searchRange([3, 3, 3], 3)

res = [''] * 4
res[0] += 'l'
print res
