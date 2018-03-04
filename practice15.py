def mergeSort(ar):
    if len(ar) == 1:
        return ar

    leftar = mergeSort(ar[:len(ar)/2])
    rightar = mergeSort(ar[len(ar)/2:])

    merged = []
    li = 0
    ri = 0

    while li < len(leftar) and ri < len(rightar):
        if leftar[li] < rightar[ri]:
            merged.append(leftar[li])
            li += 1
        else:
            merged.append(rightar[ri])
            ri += 1
    while li < len(leftar):
        merged.append(leftar[li])
        li += 1
    while ri < len(rightar):
        merged.append(rightar[ri])
        ri += 1

    return merged

import random
random.seed("g")

a = [random.randrange(100) for _ in range(10)]
print a
print mergeSort(a)