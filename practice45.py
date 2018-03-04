#https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/tutorial/


def getRoot(arr, x):
    root = x-1
    while arr[root] != root:
        root = arr[root]

    return root

def joinGraph(arr, x, y):
    x_root = getRoot(arr, x)
    y_root = getRoot(arr, y)
    if x_root < y_root:
        arr[y_root] = x_root
    else:
        arr[x_root] = y_root

def printGraph(arr):
    connCount = [0] * len(arr)
    sizeCount = [0] * (len(arr)+1)
    
    for i in range(len(arr)):
        parent = i
        count = 1
        while arr[parent] != parent:
            parent = arr[parent]
            count += connCount[parent]
            connCount[parent] = 0
        connCount[parent] = count

    #print connCount
    for i in range(len(connCount)):
        if connCount[i]:
            sizeCount[connCount[i]] += 1

    #print sizeCount

    for i in range(len(sizeCount)):
        for j in range(sizeCount[i]):
            print i,

    print ""


graph = [x for x in range(5)]
printGraph(graph)
joinGraph(graph, 1, 2)
printGraph(graph)
joinGraph(graph, 3, 4)
printGraph(graph)
joinGraph(graph, 4, 5)
printGraph(graph)
joinGraph(graph, 1, 3)
printGraph(graph)

exit(0)



n, m = map(int, raw_input().split())

graph = [x for x in range(n)]


for _ in range(m):
    x, y = map(int, raw_input().split())
    joinGraph(graph, x, y)
    printGraph(graph)
