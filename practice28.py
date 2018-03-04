#https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/monk-and-inversions-arrays-strings/

def inversion(n, arr):
    inv = 0
    for i in range(n):
        for j in range(n):
            for p in range(i, n):
                for q in range(j, n):
                    if arr[i][j] > arr[p][q]:
                        inv += 1
    return inv



t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    arr = []
    for r in range(n):
        arr.append(map(int, raw_input().split()))

    print inversion(n, arr)


