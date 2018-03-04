#https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/tutorial/
'''
5
1 2 3 4 5
4
1 1
1 2
1 3
2
'''

def max_heapify(arr, i):
    left = i * 2 + 1
    right = i * 2 + 2

    largest = i
    if left < len(arr) and arr[left] > arr[i]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        #swap with the larger children
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        # check down
        max_heapify(arr, largest)

def build_max_heap(arr):
    for i in range(len(arr)/2, -1, -1):
        max_heapify(arr, i)

def get_max(arr):
    return arr[0]

def insert_heap(arr, v):
    i = len(arr)
    arr.append(v)

    while i and arr[i] > arr[i/2]:
        temp = arr[i]
        arr[i] = arr[i/2]
        arr[i/2] = temp
        i /= 2



n = int(raw_input())
arr = map(int, raw_input().split())
q = int(raw_input())

build_max_heap(arr)

for _ in range(q):
    op = raw_input().split()
    if op[0] == '1':
        insert_heap(arr, int(op[1]))
    elif op[0] == '2':
        print get_max(arr)




