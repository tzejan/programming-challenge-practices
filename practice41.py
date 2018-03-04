#https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/tutorial/

def max_heapify(arr, i):
    left = i * 2 + 1
    right = i * 2 + 2

    largest = i
    if left < len(arr) and arr[left] > arr[i]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        max_heapify(arr, largest)


def build_max_heap(arr):
    for i in range(len(arr)/2, -1, -1):
        max_heapify(arr, i)

def insert_heap(arr, v):
    arr.append(v)
    i = len(arr) - 1

    while i and arr[i/2] < arr[i]:
        temp = arr[i/2]
        arr[i/2] = arr[i]
        arr[i] = temp
        i /= 2

def remove_max(arr):
    i = len(arr)-1
    temp = arr[0]
    arr[0] = arr[i]
    arr[i] = temp

    result = arr.pop()

    max_heapify(arr, 0)

    return result


a = [1, 2, 3, 4, 5 ,6, 7]
build_max_heap(a)
print a
insert_heap(a, 8)
print a
print remove_max(a)
print a