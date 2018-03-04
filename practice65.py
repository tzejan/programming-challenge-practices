"""
Remove Element

Given an array and a value, remove all the instances of that value in the array. 
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1, 
then new length is 3, and A is now [4, 2, 3]

Try to do it in less than linear additional space complexity.
"""

def removeElement_(A, B):
    l = 0
    r = 1
    s = 0
   

    while r < len(A):
        while l < len(A) and A[l] != B:
            l += 1
        
        r = l + 1
        while r < len(A) and A[r] == B:
            r += 1

        if r < len(A):
            A[l], A[r] = A[r], A[l]
            s += 1
        print l, r, s

    return " ".join([str(a) for a in A[:l]])

def removeElement_(A, B):
    r = []
    for a in A:
        if a != B:
            r.append(a)

    A[:] = list(r)
    return len(r)


A = "3 3 0 2 1 2 1 0 0 2 0 2 1 3 0 1 2 0 0 1 3 2 0 2 0 3 2 3 3 1 3 0 3 0 0 2 1 3 0 2 0 1 2 1 3 3 1 2 3 2 3 1 2 3 3 2 1 2 1 2 1 2 2 0 1 2 3 0 2 0 0 1 3 1 1 0 1 2 2 3 3 1 2 3 1 1 0 0 1 1 2 2 2 1 2 1 0 3 2 2 1 3 3 2 1 1 1 1 0 2 1 1 0 0 0 3 2 3 0 0 0 2 3 2 3 2 0 2 0 2 3 1 1 3 1 0 1 0 2 0 1 3 1 1 1 0 1 1 0 2 0 0 0 0 1 0 3 2 3 2 3 0 0 0 3 2 1 1 2 3 2 2 3 3 2 3 1 1 2 0 2 2 2 0 0 0 1 0 2 0 0 2 3 2 2 3 1 0 2 2 2 3 3 1 3 3 1 1 0 0 1 2 1 1 2 3 0 2 1 1 2 3 0 3 0 0 3 1 0 3 2 0 3 0 1 1 1 2 2 1 3 2 3 1 1 1 0 2 2 3 2 0 0 0 1 2 0 3 1 2 0 0 3 0 0 0 1 1 1 0 3 2 3 1 1 3 1 0 3 3 0 1 2 3 0 1 1 2 2 0 1 1 3 3 0 1 1 3 0 3 1 0 0 2 2 0 3 1 3 0 0 2 3 3 2 0 0 2 2 3 2 2 3 1 0 1 2 3 2 1 0 3 3 0 1 1 3 1 3 2 3 0 3 3 0 2 3 1 3 1 1 1 0 1 3 0 1 0 1 1 0 0 3 1 1 3 2 2 1 1 2 0 0 1 1 1 1 3 2 2 1 0 3 0 0 2 3 1 1 1 2 0 1 0 1 2 3 3 3 1 0 3 2 0 0 1 0 0 2 0 3 3 3 1 2 1 1 3 3 0 1 2 3 2 2 1 3 2 2 1 3 2 2 2 2 2 1 2 0 2 2 2 0 0 1 2 2 2 2 0 1 2 0 3 0 2 0 3 2 2 2 1 1 0 2 0 2 3 0 3 1 2 0 0 1 2 1 0 0 0 3 3 2 0 3 1 0 2 3 1 3 0 1 0 2 0 2 0 1 2 0 2 3 2 1 3 1 3 1 0 3 0 1 0 2 0 3 1 1 0 1 1 3 2 0 1 3 0 0 1 3 2 0 1 0 3 1 1 0 1 0 3 2 2 3 2 0 2 3 1 2 0 1 1 3 0 0 2 1 0 2 3 3 1 1 0 3 3 1 2 2 3 2 0 2 1 2 3 0 0 1 3 2 0 1 0 1 2 0 0 1 0 1 2 1 3 1 3 3 1 1 2 0 0 2 0 1 1 3 2 1 3 1 0 3 2 2 3 3 0 3 2 3 0 2 0 1 3 1 0 0 2 2 0 1 3 2 2 3 2 2 2 3 3 3 0 1 2 0 1 0 0 0 2 0 0 1 1 0 2 1 0 3 0 3 1 1 1 1 0 2 2 2 1 3 1 1 1 3 1 3 3 3 0 1 2 2 2 3 1 2 1 0 1 3 3 2 0 1 2 0 3 1 0 0 3 3 1 1 0 1 1 0 0 3 0 0 3 1 1 2 0 0 1 1 3 0 3 1 0 2 3 1 3 2 3 3 1 3 0 1 0 2 0 1 2 0 0 0 0 1 3 1 1 0 2 2 1 3 3 2 1 3 2 3 2 1 0 0 3 0 2 2 1 1 1 0 0 2 1 2 2 2 3 1 0 1 0 1 3 1 2 1 3 1 2 1 1 0 0 1 0 0 1 1 3 2 0 1 1 2 2 3 0 1 1 1 0 3 0 1 0 1 2 2 2 2 1 1 2 3 2 0 3 2 2 2 0 1 3 0 3 2 3 0 1 ".split()
print removeElement(A, '0')
print A