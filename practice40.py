#https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/

t = int(raw_input())
for _ in range(t):
    n, x = map(int, raw_input().split())
    a = map(int, raw_input().split())

    s = set(a)
    if len(s) > x:
        print "Average"
    elif len(s) == x:
        print "Good"
    else:
        print "Bad" 