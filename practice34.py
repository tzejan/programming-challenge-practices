#https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/xsquare-and-double-strings-1/

def isDoubleString(s):
    letter_count = dict()
    for c in s:
        if c not in letter_count:
            letter_count[c] = 0
        letter_count[c] += 1

    to_remove = []
    for k, v in letter_count.iteritems():
        if v >= 2:
            return True

    return False





t = int(raw_input())

for _ in range(t):
    s = raw_input()
    if (isDoubleString(s)):
        print "Yes"
    else:
        print "No"