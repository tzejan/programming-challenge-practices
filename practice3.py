#Breath first search

def BFS(G, v, t):
    q = [v]
    discovered = set()
    while q:
        print q
        n = q.pop(0)

        if n in discovered:
            continue

        print n, n%8, n/8, G[n]
        if (G[n] == t):
            #found            
            return n

        discovered.add(n)

        #add all the connected nodes
        col = n % 8
        row = n / 8

        if col != 0:
            q.append(n-1)
        if col != 7:
            q.append(n+1)
        if row != 0:
            q.append(n-8)
        if row != 7:
            q.append(n+8)

def printG():
    for i in range(8):
        print G[i*8:i*8+8]


import random
random.seed("g")
G = []
for i in range(64):
    G.append(random.randrange(10, 99))
printG()

BFS(G, 0, 47)
