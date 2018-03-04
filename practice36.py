#https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/a-needle-in-the-haystack-1/

def isPermutationDunno(p,s):

    p1=p[::-1]
    if p in s:
        print "YES"
    elif p1 in s:
        print "YES"
    else:
        print "NO"

def isPermutation(p, s):
    letter_count = [0] * 26
    total_count = len(p)

    for c in p:
        letter_count[ord(c)-97] += 1

    for c in s[:len(p)]:
        ci = ord(c)-97
        letter_count[ci] -= 1
        if letter_count[ci] >= 0:
            total_count -= 1
        else:
            total_count += 1    

    for i in range(len(s)-len(p)+1):
        if total_count == 0:
            return True

        ci = ord(s[i]) - 97
        letter_count[ci] += 1
        if letter_count[ci] > 0:
            total_count += 1
        else:
            total_count -= 1

 
        if i + len(p) < len(s):
            ci = ord(s[i + len(p)]) - 97
            letter_count[ci] -= 1
            if letter_count[ci] >= 0:
                total_count -= 1
            else:
                total_count += 1

    return False



def hashFn(d):
    hash_value = 0
    for k, v in d.iteritems():
        hash_value += (ord(k)-97) * v

    return hash_value

def isPermutationHash(p, s):
    p_dict = dict()
    s_dict = dict()
    distance = 0
    for c in p:
        if c not in p_dict:
            p_dict[c] = 0
        p_dict[c] += 1

    p_hash = hashFn(p_dict)

    for c in s[:len(p)]:
        if c not in s_dict:
            s_dict[c] = 0
        s_dict[c] += 1

    s_hash = hashFn(s_dict)

    for i in range(len(s)-len(p)+1):
        if p_hash == s_hash:
            for k in p_dict.keys():
                if p_dict[k] != s_dict[k]:
                    break
            else:
                return True

        s_hash -= ord(s[i]) - 97 
        s_dict[s[i]] -= 1
        if i + len(p) < len(s):
            new_char = s[i + len(p)]
            if new_char not in s_dict:
                s_dict[new_char] = 0
            s_dict[new_char] += 1

            s_hash += ord(new_char) - 97

    return False

print isPermutation("code", "eddy")
     
#exit(0)
with open("input-0900681.txt", 'r') as f:
    t = int(f.readline())

    for _ in range(t):
        p = f.readline().strip()
        s = f.readline().strip()

        if isPermutation(p, s):
            print "YES"
        else:
            print "NO"
        #break

exit(0)

t = int(raw_input())

for _ in range(t):
    p = raw_input().strip()
    s = raw_input().strip()

    if isPermutation(p, s):
        print "YES"
    else:
        print "NO"



