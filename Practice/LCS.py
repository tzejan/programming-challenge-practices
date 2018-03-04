#n, m = map(int, raw_input().split())
#a = map(int, raw_input().split())
#b = map(int, raw_input().split())
#9 10
#3 9 8 3 9 7 9 7 0
#3 3 9 9 9 1 7 2 0 6
ia = "3 9 8 3 9 7 9 7 0"
ib = "3 3 9 9 9 1 7 2 0 6"

a = map(int, ia.split())
#a = [3, 4, 1, 2, 1, 3]
b = map(int, ib.split())
n = len(a)
m = len(b)


mem = [[None] * m for i in xrange(n)]


def rgetLCS(i,j):

    if i == -1 or j == -1:
        return []

    print '(',i, j,')'
    if a[i] == b[j]:
        print "<>", i, j, b[j]
        result = rgetLCS(i-1, j-1)
        result.append(b[j])
        return result
    else:
        #split route here
        print "/"
        if (j == 0 and mem[i][j] == 1) or mem[i][j] == mem[i-1][j]:
            return rgetLCS(i-1, j)
        elif (i == 0 and mem[i][j] == 1) or mem[i][j] == mem[i][j-1]:
            return rgetLCS(i, j-1)
    # unlikely but for sanity sake
    return []
        
def rLCS(a, b, i, j):

    if i == -1 or j == -1:
        return 0

    if mem[i][j]:
        return mem[i][j]

    # calculate the LCS
    if a[i] == b[j]:
        mem[i][j] = rLCS(a, b, i-1, j-1) + 1
    else:
        mem[i][j] = max(rLCS(a, b, i-1, j), rLCS(a, b, i, j-1))

    return mem[i][j]
    
rLCS(a, b, n-1, m-1)


print a
zipmem = zip(*mem)
for j in xrange(m):
    print "\t".join(str(v) for v in zipmem[j])
print b

print " ".join(str(l) for l in rgetLCS(n-1, m-1))
#print mem

"""
    1   2   3   4   1
    -----------------
3   0   0   1   0   0
4   0   0   1   2   0
1   1   1   1   2   0
2   0   2   2   2   0
1   1   2   2   2   3
3   0   0   3   3   3
"""