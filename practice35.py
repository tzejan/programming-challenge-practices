#https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/alien-language/

def isSubString(s, p):
    p_dict = dict()

    for c in p:
        if c not in p_dict:
            p_dict[c] = True

    for c in s:
        if c in p_dict:
            return True

    return False

def hashfn(s):
    h = 0
    for c in s:
        h += ord(c)-97
    return h

def isSubString_Rabin_karp(s, p):
    p_len = len(p)
    s_len = len(s)

    current_hash = hashfn(s[:p_len])
    pattern_hash = hashfn(p)

    for i in range(s_len-p_len+1):
        if current_hash == pattern_hash:
            for j in range(p_len):
                if s[i+j] != p[j]:
                    break
            else:
                return True

        current_hash -= ord(s[i]) - 97
        if i+p_len < s_len:
            current_hash += ord(s[i+p_len]) - 97

    return False

with open("input-8b23b7a.txt", 'r') as f:
    t = int(f.readline())
    for _ in range(t):
        s = f.readline().strip()
        p = f.readline().strip()
        #print s, p
        if isSubString(s, p):
            print "YES"
        else:
            print "NO"

t = int(raw_input())

for _ in range(t):
    s = raw_input().strip()
    p = raw_input().strip()
    if isSubString(s, p):
        print "YES"
    else:
        print "NO"