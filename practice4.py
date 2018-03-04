#max heap

def print_heap(A):
    level = 0
    nextIndex = 0
    index = 0
    while index < len(A):
        nextIndex = index + pow(2, level)
        print A[index: nextIndex]
        index = nextIndex
        level += 1
    print ""


def max_heapify(A, i, m):
    leftChild = 2*i + 1
    rightChild = 2*i + 2

    #print i, leftChild, rightChild, m
    swapIndex = -1
    if leftChild <= m and A[leftChild] >= A[i]:
        swapIndex = leftChild

    if rightChild <= m and A[rightChild] >= A[i] and A[rightChild] >= A[leftChild]:
        swapIndex = rightChild

    if swapIndex != -1:
        temp = A[swapIndex]
        A[swapIndex] = A[i]
        A[i] = temp
        max_heapify(A, swapIndex, m)
    


def build_max_heap(A):
    for i in range(len(A) / 2, -1, -1):
        max_heapify(A, i, len(A)-1)

def extract_max(A, m):
    # swap root with smallest leaf
    temp = A[0]
    A[0] = A[m]
    A[m] = temp

    max_heapify(A, 0, m-1)
    return temp

        
def heapSort(A):
    build_max_heap(A)
    for i in range(len(A)-1, 0, -1):
        #print_heap(A)
        extract_max(A, i)

def BSearch(A, t):
    leftBound = 0
    rightBound = len(A)-1
    while leftBound <= rightBound:
        i = (leftBound + rightBound) / 2
        if A[i] == t:
            #found
            return i
        if A[i] > t:
            rightBound = i - 1
        else:
            leftBound = i + 1
    return -1


import random
random.seed("g")

A = [random.randrange(10) for _ in range(10)]

print(A)
heapSort(A)
print(A)
print BSearch(A, 3)
print BSearch(A, 5)

print_heap(A)
build_max_heap(A)
print_heap(A)
extract_max(A, len(A)-1)
print_heap(A)

