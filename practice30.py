#https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/the-football-fest-6/

t = int(raw_input())

for _ in range(t):
    n, current = map(int, raw_input().split())
    prev = current
    for p in range(n):
        ballpass = raw_input().split()
        if ballpass[0] == 'B':
            temp = current
            current = prev
            prev = temp
        else:
            passPlayerID = int(ballpass[1])
            prev = current
            current = passPlayerID

    print "Player", current 