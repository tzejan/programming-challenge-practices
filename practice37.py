#https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/comrades-ii-6/

#generate a tree
#generate an array of siblings per level
#generate number of children per level
#handshakes = sum of siblings per level * children 
#fistbumps = sum of (siblings per level! / siblings per level) 


def getHandShakesAndFistBumps(n, soldiers):

    sup = dict()
    for i, s in enumerate(soldiers):
        if s not in sup:
            sup[s] = []
        sup[s].append(i+1)

    children_per_level = [0]

    toVisit = [(0,0)]

    for node, level in toVisit:
        if node not in sup:
            continue

        children_per_level[level] += len(sup[node])
        for c in sup[node]:
            toVisit.append((c, level+1))

        if level+1 == len(children_per_level):
            children_per_level.append(0)

    children = 0
    for i in range(len(children_per_level)-1, -1, -1):
        children_per_level[i] += children
        children = children_per_level[i]

    hs = sum(children_per_level[1:])
    fb = (n * (n-1)/2) - hs

    return hs, fb

print 1000 * 999/2 - 70445

print getHandShakesAndFistBumps(3, [0, 1, 1])
#exit(0)
with open ("input-fd14a5d.txt", 'r') as f:
#with open ("input-fcbdf06.txt", 'r') as f:
#with open ("input-fce7296.txt", 'r') as f:
    t = int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        soldiers = map(int, f.readline().split())

        hs, fb = getHandShakesAndFistBumps(n, soldiers)
        print hs, fb
exit(0)

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    soldiers = map(int, raw_input().split())

    hs, fb = getHandShakesAndFistBumps(n, soldiers)
    print hs, fb